-- Consider the following relations for Pizza Ordering System:
-- CUSTOMER ( cust_id ,cust_name, address, phone)
-- PIZZA (pizza_id, pizza_type, unit_price)
-- ORDERS (order_no, cust_id, order_date ,delv_date, total_amt)
-- ORDER_LIST (order_no, pizza_id, qty)
-- Write a PL/SQL trigger and implement the following constraints:
-- Note:
-- a. Choose appropriate event(s) to ensure the constraint.

-- 1. Ensure that the pizza can be delivered on same day or on the next day
-- only.

CREATE OR REPLACE TRIGGER check_delivery_dates_trigger
BEFORE UPDATE OR INSERT ON ORDERS
FOR EACH ROW
DECLARE
	diff_dates NUMBER := 0;
BEGIN
	diff_dates := :NEW.delv_date - :NEW.order_date;
	
	IF diff_dates NOT IN (0,1) THEN
		RAISE_APPLICATION_ERROR(-20001, 'ERROR BRO');
	END IF;
END check_delivery_dates_trigger;
/

INSERT INTO ORDERS (order_no, cust_id, order_date, delv_date, total_amount)
VALUES ('TEST2', 'c002', SYSDATE, SYSDATE + 2, 1500);

INSERT INTO ORDERS (order_no, cust_id, order_date, delv_date, total_amount)
VALUES ('TEST1', 'c001', SYSDATE, SYSDATE + 1, 1500);

-- Update the total_amt in ORDERS while entering an order in
-- ORDER_LIST.

CREATE OR REPLACE TRIGGER update_total_amt_trigger
AFTER UPDATE OR INSERT ON ORDER_LIST
FOR EACH ROW
DECLARE
BEGIN
    -- Update total_amt in ORDERS for the corresponding order_no
	DBMS_OUTPUT.PUT_LINE(DBMS_UTILITY.FORMAT_CALL_STACK);
    UPDATE ORDERS
    SET total_amount = (
        SELECT SUM(p.unit_price * ol.qty)
        FROM PIZZA p
        JOIN ORDER_LIST ol ON p.pizza_id = ol.pizza_id
        WHERE ol.order_no = :NEW.order_no
    )
    WHERE order_no = :NEW.order_no;
    
    COMMIT;
END update_total_amt_trigger;
/


-- To give preference to all customers in delivery of pizzas’, a threshold is
-- set on the number of orders per day per customer. Ensure that a
-- customer can not place more than 5 orders per day.

CREATE OR REPLACE TRIGGER check_order_limit_trigger
BEFORE INSERT ON ORDERS
FOR EACH ROW
DECLARE
   orders_count NUMBER;
BEGIN
   -- Check the number of orders placed by the customer on the given day
   SELECT COUNT(*)
   INTO orders_count
   FROM ORDERS
   WHERE cust_id = :NEW.cust_id
      AND TRUNC(order_date) = TRUNC(SYSDATE);

   -- If the customer has already placed 5 orders on the same day, raise an error
   IF orders_count >= 5 THEN
      RAISE_APPLICATION_ERROR(-20201, 'A customer cannot place more than 5 orders per day.');
   END IF;
END check_order_limit_trigger;
/