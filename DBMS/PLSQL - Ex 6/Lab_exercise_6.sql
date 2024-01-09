SET SERVEROUTPUT ON;
SET LINESIZE 400;
SET PAGESIZE 50;
SET NULL 'Null';
-- Write a stored procedure to display the total number of pizza's ordered by
-- the given order number. (Use IN, OUT)


CREATE OR REPLACE PROCEDURE total_pizzas 
( order_num IN order_list.order_no%TYPE , total_num OUT NUMBER)
IS
	CURSOR total_num_pizzas
	IS
	SELECT COUNT(qty) FROM order_list
	GROUP BY order_no
	HAVING order_no = order_num;
BEGIN
	OPEN total_num_pizzas;
	FETCH total_num_pizzas INTO total_num;
	CLOSE total_num_pizzas;
END;
/

-- Executing by EXECUTE
VAR total_num NUMBER;
EXECUTE total_pizzas('&order_num', :total_num);
PRINT total_num;	
-- Can also execute by PL/SQL block
DECLARE
   v_total_num NUMBER; --Declare a variable for storing
BEGIN
   total_pizzas('OP100', v_total_num);
   DBMS_OUTPUT.PUT_LINE('Total Pizzas: ' || v_total_num);
END;
/

-- For the given order number, calculate the Discount as follows:
-- For total amount > 2000 and total amount < 5000: Discount=5%
-- For total amount > 5000 and total amount < 10000: Discount=10%
-- For total amount > 10000: Discount=20%
-- Calculate the total amount (after the discount) and update the same in
-- orders table. Print the order as shown below:
-- ************************************************************
-- Order Number:OP104 Customer Name: Hari
-- Order Date :29-Jun-2015 Phone: 9001200031
-- ************************************************************
-- SNo Pizza Type Qty Price Amount
-- 1. Italian 6 200 1200
-- 2. Spanish 5 260 1300
-- ------------------------------------------------------
-- Total = 11 2500
-- ------------------------------------------------------
-- Total Amount :Rs.2500
-- Discount (5%) :Rs. 125
-- -------------------------- ----
-- Amount to be paid :Rs.2375
-- -------------------------- ----
-- Great Offers! Discount up to 25% on DIWALI Festival Day...
-- *************************************************************

CREATE SEQUENCE serial_num
START WITH 1
MAXVALUE 5
INCREMENT BY 1
CYCLE
CACHE 4;

SET SERVEROUTPUT ON;

-- Add TOTAL_AMOUNT column to the ORDERS table
ALTER TABLE ORDERS ADD TOTAL_AMOUNT NUMBER;

-- Recreate the procedure with the updated ORDERS table
CREATE OR REPLACE PROCEDURE calculate_discount_and_print
( p_order_no IN VARCHAR2 )
IS
   v_customer_name VARCHAR2(100);
   v_order_date    DATE;
   v_phone         VARCHAR2(15);
   v_total_amount  NUMBER := 0;
   v_discount      NUMBER := 0;

   CURSOR order_details_cur IS
      SELECT
         c.cust_name,
         o.order_date,
         c.phone,
         p.pizza_type,
         ol.qty,
         p.unit_price
      FROM
         orders o
         JOIN customer c ON o.cust_id = c.cust_id
         JOIN order_list ol ON o.order_no = ol.order_no
         JOIN pizza p ON ol.pizza_id = p.pizza_id
      WHERE
         o.order_no = p_order_no;

BEGIN
   -- Fetch order details
   FOR order_rec IN order_details_cur LOOP
      DBMS_OUTPUT.PUT_LINE(serial_num.NEXTVAL || '. ' || order_rec.pizza_type || ' ' || order_rec.qty || ' ' || order_rec.unit_price);
      v_total_amount := v_total_amount + (order_rec.qty * order_rec.unit_price);
   END LOOP;

   -- Apply discount based on total amount
   IF v_total_amount > 2000 AND v_total_amount < 5000 THEN
      v_discount := 0.05;
   ELSIF v_total_amount >= 5000 AND v_total_amount < 10000 THEN
      v_discount := 0.1;
   ELSIF v_total_amount >= 10000 THEN
      v_discount := 0.2;
   END IF;

   -- Update the orders table with the calculated total amount
   UPDATE orders SET total_amount = v_total_amount * (1 - v_discount) WHERE order_no = p_order_no;
   COMMIT;

   -- Fetch additional order information
   SELECT cust_name, order_date, phone INTO v_customer_name, v_order_date, v_phone
   FROM customer c
   JOIN orders o ON c.cust_id = o.cust_id
   WHERE o.order_no = p_order_no;

   -- Print the order details
   DBMS_OUTPUT.PUT_LINE('************************************************************');
   DBMS_OUTPUT.PUT_LINE('Order Number: ' || p_order_no || ' Customer Name: ' || v_customer_name);
   DBMS_OUTPUT.PUT_LINE('Order Date: ' || TO_CHAR(v_order_date, 'DD-Mon-YYYY') || ' Phone: ' || v_phone);
   DBMS_OUTPUT.PUT_LINE('************************************************************');
   DBMS_OUTPUT.PUT_LINE('SNo Pizza Type Qty Price Amount');
   
   -- Fetch and print order details again
   FOR order_rec IN order_details_cur LOOP
      DBMS_OUTPUT.PUT_LINE(order_rec.qty || '. ' || order_rec.pizza_type || ' ' || order_rec.qty || ' ' || order_rec.unit_price);
   END LOOP;

   DBMS_OUTPUT.PUT_LINE('------------------------------------------------------');
   DBMS_OUTPUT.PUT_LINE('Total = ' || v_total_amount);
   DBMS_OUTPUT.PUT_LINE('------------------------------------------------------');
   DBMS_OUTPUT.PUT_LINE('Total Amount : Rs.' || v_total_amount);
   DBMS_OUTPUT.PUT_LINE('Discount (' || TO_CHAR(v_discount * 100) || '%) : Rs. ' || TO_CHAR(v_total_amount * v_discount));
   DBMS_OUTPUT.PUT_LINE('-------------------------- ----');
   DBMS_OUTPUT.PUT_LINE('Amount to be paid : Rs.' || TO_CHAR(v_total_amount * (1 - v_discount)));
   DBMS_OUTPUT.PUT_LINE('-------------------------- ----');
   DBMS_OUTPUT.PUT_LINE('Great Offers! Discount up to 25% on DIWALI Festival Day...');
   DBMS_OUTPUT.PUT_LINE('*************************************************************');
END calculate_discount_and_print;
/

SHOW ERRORS PROCEDURE calculate_discount_and_print;
-- Execute the procedure for a specific order number
EXECUTE calculate_discount_and_print('OP100');

-- Write a stored function to display the customer name who ordered
-- highest among the total number of pizzas for a given pizza type.

CREATE OR REPLACE FUNCTION highest_pizzas
(p_pizza_type IN pizza.pizza_type%TYPE)
RETURN customer.cust_name%TYPE
IS
	highest_qty NUMBER;
	v_cust_name Customer.cust_name%TYPE;
	CURSOR highest_pizza_member
	IS
	SELECT c.cust_name, SUM(qty) as total_qty
	FROM order_list ol
	JOIN orders o ON ol.order_no = o.order_no
	JOIN Customer c ON o.cust_id = c.cust_id
	JOIN pizza p ON p.pizza_id = ol.pizza_id
	WHERE p.pizza_type = p_pizza_type
	GROUP BY (c.cust_name)
	ORDER BY total_qty DESC;
BEGIN
	OPEN highest_pizza_member;
	FETCH highest_pizza_member INTO v_cust_name, highest_qty;
	DBMS_OUTPUT.PUT_LINE(v_cust_name || highest_qty || p_pizza_type);
	CLOSE highest_pizza_member;
	RETURN v_cust_name;
END;
/


-- Implement Question (2) using stored function to return the amount to be
-- paid and update the same, for the given order number

-- For the given order number, calculate the Discount as follows:
-- For total amount > 2000 and total amount < 5000: Discount=5%
-- For total amount > 5000 and total amount < 10000: Discount=10%
-- For total amount > 10000: Discount=20%
-- Calculate the total amount (after the discount) and update the same in
-- orders table. Print the order as shown below:
-- ************************************************************
-- Order Number:OP104 Customer Name: Hari
-- Order Date :29-Jun-2015 Phone: 9001200031
-- ************************************************************
-- SNo Pizza Type Qty Price Amount
-- 1. Italian 6 200 1200
-- 2. Spanish 5 260 1300
-- ------------------------------------------------------
-- Total = 11 2500
-- ------------------------------------------------------
-- Total Amount :Rs.2500
-- Discount (5%) :Rs. 125
-- -------------------------- ----
-- Amount to be paid :Rs.2375
-- -------------------------- ----
-- Great Offers! Discount up to 25% on DIWALI Festival Day...
-- *************************************************************

-- Recreate the procedure with the updated ORDERS table
CREATE OR REPLACE FUNCTION calculate_discount_and_print_fxn
( p_order_no IN VARCHAR2 )
RETURN NUMBER 
IS 
   v_customer_name VARCHAR2(100);
   v_order_date    DATE;
   v_phone         VARCHAR2(15);
   v_total_amount  NUMBER := 0;
   v_discount      NUMBER := 0;
	return_amt NUMBER;
   CURSOR order_details_cur IS
      SELECT
         c.cust_name,
         o.order_date,
         c.phone,
         p.pizza_type,
         ol.qty,
         p.unit_price
      FROM
         orders o
         JOIN customer c ON o.cust_id = c.cust_id
         JOIN order_list ol ON o.order_no = ol.order_no
         JOIN pizza p ON ol.pizza_id = p.pizza_id
      WHERE
         o.order_no = p_order_no;

BEGIN
   -- Fetch order details
   FOR order_rec IN order_details_cur LOOP
      DBMS_OUTPUT.PUT_LINE(serial_num.NEXTVAL || '. ' || order_rec.pizza_type || ' ' || order_rec.qty || ' ' || order_rec.unit_price);
      v_total_amount := v_total_amount + (order_rec.qty * order_rec.unit_price);
   END LOOP;

   -- Apply discount based on total amount
   IF v_total_amount > 2000 AND v_total_amount < 5000 THEN
      v_discount := 0.05;
   ELSIF v_total_amount >= 5000 AND v_total_amount < 10000 THEN
      v_discount := 0.1;
   ELSIF v_total_amount >= 10000 THEN
      v_discount := 0.2;
   END IF;
	
	return_amt := v_total_amount * (1 - v_discount);
   -- Update the orders table with the calculated total amount
   UPDATE orders SET total_amount = v_total_amount * (1 - v_discount) WHERE order_no = p_order_no;
   COMMIT;

   -- Fetch additional order information
   SELECT cust_name, order_date, phone INTO v_customer_name, v_order_date, v_phone
   FROM customer c
   JOIN orders o ON c.cust_id = o.cust_id
   WHERE o.order_no = p_order_no;

   -- Print the order details
   DBMS_OUTPUT.PUT_LINE('************************************************************');
   DBMS_OUTPUT.PUT_LINE('Order Number: ' || p_order_no || ' Customer Name: ' || v_customer_name);
   DBMS_OUTPUT.PUT_LINE('Order Date: ' || TO_CHAR(v_order_date, 'DD-Mon-YYYY') || ' Phone: ' || v_phone);
   DBMS_OUTPUT.PUT_LINE('************************************************************');
   DBMS_OUTPUT.PUT_LINE('SNo Pizza Type Qty Price Amount');
   
   -- Fetch and print order details again
   FOR order_rec IN order_details_cur LOOP
      DBMS_OUTPUT.PUT_LINE(order_rec.qty || '. ' || order_rec.pizza_type || ' ' || order_rec.qty || ' ' || order_rec.unit_price);
   END LOOP;

   DBMS_OUTPUT.PUT_LINE('------------------------------------------------------');
   DBMS_OUTPUT.PUT_LINE('Total = ' || v_total_amount);
   DBMS_OUTPUT.PUT_LINE('------------------------------------------------------');
   DBMS_OUTPUT.PUT_LINE('Total Amount : Rs.' || v_total_amount);
   DBMS_OUTPUT.PUT_LINE('Discount (' || TO_CHAR(v_discount * 100) || '%) : Rs. ' || TO_CHAR(v_total_amount * v_discount));
   DBMS_OUTPUT.PUT_LINE('-------------------------- ----');
   DBMS_OUTPUT.PUT_LINE('Amount to be paid : Rs.' || TO_CHAR(v_total_amount * (1 - v_discount)));
   DBMS_OUTPUT.PUT_LINE('-------------------------- ----');
   DBMS_OUTPUT.PUT_LINE('Great Offers! Discount up to 25% on DIWALI Festival Day...');
   DBMS_OUTPUT.PUT_LINE('*************************************************************');
   
   RETURN return_amt;
END calculate_discount_and_print_fxn;
/

SHOW ERRORS FUNCTION calculate_discount_and_print_fxn;

-- Anonymous Block to Execute the Procedure
DECLARE
   v_order_no VARCHAR2(20) := 'OP100'; -- Replace with the desired order number
	return_amt NUMBER;
BEGIN
   return_amt := calculate_discount_and_print_fxn(v_order_no);
   DBMS_OUTPUT.PUT_LINE(return_amt);
END;
/
