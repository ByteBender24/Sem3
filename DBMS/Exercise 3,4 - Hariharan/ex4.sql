SET ECHO ON;

REM: Author : Harishraj S
REM: Date : 24-10-2023


REM:  Views and Sequences

DROP VIEW PIZZA_200_250;
DROP VIEW PIZZA_TYPE_ORDER;
DROP VIEW SPANISH_CUSTOMERS;
DROP SEQUENCE Order_No_Seq;

REM: 1. An user is interested to have list of pizza’s in the range of Rs.200-250.
REM: Create a view Pizza_200_250 which keeps the pizza details that has the
REM: price in the range of 200 to 250.

CREATE VIEW PIZZA_200_250 AS
SELECT * FROM PIZZA
WHERE unit_price BETWEEN 200 AND 250;

SELECT * FROM PIZZA_200_250;

REM: 2. Pizza company owner is interested to know the number of pizza types
REM: ordered in each order. Create a view Pizza_Type_Order that lists the
REM: number of pizza types ordered in each order.

CREATE VIEW PIZZA_TYPE_ORDER AS
SELECT OL.order_no,COUNT(DISTINCT P.pizza_type) AS PIZZA_COUNT FROM ORDER_LIST OL
JOIN PIZZA P ON P.pizza_id=OL.pizza_id
GROUP BY OL.order_no;

SELECT * FROM PIZZA_TYPE_ORDER;

REM: 3. To know about the customers of Spanish pizza, create a view
REM: Spanish_Customers that list out the customer id, name, order_no of
REM: customers who ordered Spanish type.

CREATE VIEW SPANISH_CUSTOMERS AS 
SELECT C.cust_id, C.cust_name, O.order_no FROM CUSTOMER C
JOIN ORDERS O ON O.cust_id = C.cust_id
JOIN PIZZA P ON P.pizza_type = 'spanish'
GROUP BY C.cust_id, C.cust_name, O.order_no;

SELECT * FROM SPANISH_CUSTOMERS;

REM: 4. Create a sequence named Order_No_Seq which generates the Order
REM: number starting from 1001, increment by 1, to a maximum of 9999.
REM: Include options of cycle, cache and order. Use this sequence to populate
REM: the rows of Order_List table.

DROP SEQUENCE Order_No_Seq;

CREATE SEQUENCE Order_No_Seq 
START WITH 1001
INCREMENT BY 1
MAXVALUE 9999
CYCLE
CACHE 10;

INSERT INTO ORDERS
VALUES('OP1001', 'c001','12-JUN-2023','12-JUN-2023');

INSERT INTO Order_List (order_no, pizza_id, qty)
VALUES ('OP' || TO_CHAR(Order_No_Seq.NEXTVAL), 'p001', 3);