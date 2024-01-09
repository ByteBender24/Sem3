REM| Consider the following relations for Pizza Ordering System:

REM| CUSTOMER ( cust_id (PK) ,cust_name, address, phone)
REM| PIZZA (pizza_id (PK), pizza_type, unit_price)
REM| ORDERS (order_no(PK), cust_id, order_date, delv_date)
REM| ORDER_LIST (order_no(PK), pizza_id (PK), qty)

REM| a) Draw schema diagram for Pizza database.

REM| b)Create tables with appropriate data types and integrity constraints in
REM| order to populate tables from the Pizza_DB.sql file.

REM| c) Include constraint : The quantity ordered for a pizza cannot be null.


REM| Dropping tables

DROP TABLE CUSTOMER CASCADE CONSTRAINTS;
DROP TABLE PIZZA CASCADE CONSTRAINTS;
DROP TABLE ORDERS CASCADE CONSTRAINTS;
DROP TABLE ORDER_LIST CASCADE CONSTRAINTS;

REM| Creation of table for Pizza Ordering System

-- Table CUSTOMER
CREATE TABLE CUSTOMER (
	cust_id varchar(30),
	cust_name varchar(40),
	address varchar(255),
	phone int,
	CONSTRAINT PK_Customer PRIMARY KEY (cust_id)
	);
	
-- Table PIZZA
CREATE TABLE PIZZA (
	pizza_id varchar(20),
	pizza_type varchar(40),
	unit_price int,
	CONSTRAINT PK_Pizza PRIMARY KEY (pizza_id)
	);

-- TABLE ORDERS
CREATE TABLE ORDERS (
	order_no varchar(30),
	cust_id varchar(30),
	order_date DATE,
	delv_date DATE,
	CONSTRAINT PK_Order PRIMARY KEY (order_no)
	);

-- TABLE ORDER_LIST 
CREATE TABLE ORDER_LIST (
	order_no varchar(30),
	pizza_id varchar(20),
	qty int,
	CONSTRAINT PK_OrderList PRIMARY KEY (order_no, pizza_id)
	);

ALTER TABLE ORDER_LIST
MODIFY qty int NOT NULL;

ALTER TABLE ORDERS
ADD CONSTRAINT FK_Orders_cust_id FOREIGN KEY (cust_id) REFERENCES CUSTOMER(cust_id);

ALTER TABLE ORDER_LIST
ADD CONSTRAINT FK_Orderlist_order_no FOREIGN KEY (order_no) REFERENCES ORDERS(order_no);

ALTER TABLE ORDER_LIST
ADD CONSTRAINT FK_Orderlist_pizza_id FOREIGN KEY (pizza_id) REFERENCES PIZZA(pizza_id);

