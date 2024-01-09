-- Check whether the given pizza type is available. If available display its
-- unit price. If not, display “The pizza is not available / Invalid pizza type”.
SET SERVEROUTPUT ON;
SET LINESIZE 400;
SET PAGESIZE 50;

DECLARE 
	p_pizza_type PIZZA.pizza_type%TYPE := '&pizza_type';
	p_unit_price int;
	CURSOR pizza_type_cursor 
	IS 
	SELECT unit_price FROM pizza WHERE pizza_type = p_pizza_type;
BEGIN
	
	OPEN pizza_type_cursor;
	FETCH pizza_type_cursor into p_unit_price;
	
	IF pizza_type_cursor%NOTFOUND THEN
		DBMS_OUTPUT.PUT_LINE('Not the type is present here');
	ELSE
	DBMS_OUTPUT.PUT_LINE(p_unit_price || ' ' || p_pizza_type);
	END IF;
	CLOSE pizza_type_cursor;
END;
/

-- For the given customer name and a range of order date, find whether a
-- customer had placed any order, if so display the number of orders placed
-- by the customer along with the order number(s).

SET SERVEROUTPUT ON;
SET LINESIZE 400;
SET PAGESIZE 50;

DECLARE
	p_cust_name CUSTOMER.cust_name%TYPE := '&Customer_name';
	start_date DATE := '&start_date';
	end_date DATE := '&end_date';
	num_orders NUMBER:= 0;
	CURSOR find_order
	IS 
	SELECT * FROM orders o 
	JOIN CUSTOMER c ON o.cust_id = c.cust_id
	WHERE c.cust_name = p_cust_name AND 
	(o.order_date BETWEEN start_date AND end_date);
BEGIN
	
	FOR order_rec in find_order LOOP
		DBMS_OUTPUT.PUT_LINE('Order_no :' || order_rec.order_no || ' BY ' || order_rec.cust_name);
		num_orders := num_orders +1;
	END LOOP;
	DBMS_OUTPUT.PUT_LINE('Number of orders between given dates : ' || num_orders);
END;
/


-- Display the customer name along with the details of pizza type and its
-- quantity ordered for the given order number. Also find the total quantity
-- ordered for the given order number as shown below:
--
-- SQL> /
-- Enter value for oid: OP100
-- old 11: oid:='&oid';
-- new 11: oid:='OP100';
-- Customer name: Hari
-- Ordered Following Pizza
-- PIZZA TYPE QTY
-- Pan 3
-- Grilled 2
-- Italian 1
-- Spanish 5
--  --------------------
-- Total Qty: 11

SET SERVEROUTPUT ON;
SET LINESIZE 400;
SET PAGESIZE 50;

DECLARE 
	p_order_no ORDERS.order_no%TYPE := '&Order_number';
	p_cust_name Customer.cust_name%TYPE;
	p_pizza_type VARCHAR2(40);
	p_qty NUMBER;
	p_qty_total NUMBER := 0;
	
	CURSOR order_finder
	IS 
	SELECT c.cust_name, p.pizza_type, ol.Qty FROM orders o 
	JOIN customer c ON c.cust_id = o.cust_id
	JOIN order_list ol ON o.order_no = ol.order_no
	JOIN pizza p ON p.pizza_id = ol.pizza_id
	WHERE o.order_no = p_order_no;
BEGIN
	OPEN order_finder;
	FETCH order_finder INTO p_cust_name, p_pizza_type, p_qty ;
	DBMS_OUTPUT.PUT_LINE('Cust_name : ' || p_cust_name);
	CLOSE order_finder;
	DBMS_OUTPUT.PUT_LINE('PIZZA TYPE' || '  ' || 'QTY');
	FOR order_rec IN order_finder LOOP
		DBMS_OUTPUT.PUT_LINE(order_rec.pizza_type || '  ' || order_rec.qty);
		p_qty_total := p_qty_total + order_rec.qty;
	END LOOP;
	DBMS_OUTPUT.PUT_LINE('Total: ' || p_qty_total);
END;
/


-- Display the total number of orders that contains one pizza type, two pizza
-- type and so on.

-- Number of Orders that contains
-- Only ONE Pizza type 8
-- Two Pizza types 3
-- Three Pizza types 2
-- ALL Pizza types 1

SET SERVEROUTPUT ON;
SET LINESIZE 400;
SET PAGESIZE 50;

DECLARE
	CURSOR pizza_type_order
	IS 
	SELECT 
		CASE
      WHEN pizza_type_count = 1 THEN 'Only ONE Pizza type'
      WHEN pizza_type_count = 2 THEN 'Two Pizza types'
      WHEN pizza_type_count = 3 THEN 'Three Pizza types'
      ELSE 'ALL Pizza types'
   END AS order_category,
		COUNT(order_no) AS order_count
	FROM (
		SELECT order_no, COUNT(DISTINCT pizza_id) AS pizza_type_count FROM order_list GROUP BY order_no)
	GROUP BY pizza_type_count
	ORDER BY pizza_type_count;
BEGIN
	DBMS_OUTPUT.PUT_LINE('ORDER_CATEGORY      ORDER_COUNT');
	DBMS_OUTPUT.PUT_LINE('------------------- -----------');
	FOR rec in pizza_type_order LOOP
		DBMS_OUTPUT.PUT_LINE(rec.order_category ||'     '|| rec.order_count);
	END LOOP;
END;
/
-- Normal SQL query
SELECT
   CASE
      WHEN pizza_type_count = 1 THEN 'Only ONE Pizza type'
      WHEN pizza_type_count = 2 THEN 'Two Pizza types'
      WHEN pizza_type_count = 3 THEN 'Three Pizza types'
      ELSE 'ALL Pizza types'
   END AS order_category,
   COUNT(order_no) AS order_count
FROM (
   SELECT
      order_no,
      COUNT(DISTINCT pizza_id) AS pizza_type_count
   FROM order_list
   GROUP BY order_no
)
GROUP BY pizza_type_count
ORDER BY pizza_type_count;
