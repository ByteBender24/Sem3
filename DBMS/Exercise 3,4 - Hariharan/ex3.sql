SET ECHO ON;
REM: Author : Harishraj S
REM: Date : 16-10-2023


REM:  Advanced DML – using Joins, Sub queries, Set Operations
REM: Pizza Ordering System

REM: Dropping the tables

DROP TABLE ORDER_LIST CASCADE CONSTRAINTS;
DROP TABLE ORDERS CASCADE CONSTRAINTS;
DROP TABLE PIZZA CASCADE CONSTRAINTS;
DROP TABLE CUSTOMER CASCADE CONSTRAINTS;

REM: Creating the tables

CREATE TABLE CUSTOMER(
cust_id varchar(10),
cust_name varchar(50),
address varchar(50),
phone int,
CONSTRAINT pk_cust_id PRIMARY KEY(cust_id)
);

CREATE TABLE PIZZA(
pizza_id varchar(10),
pizza_type varchar(10),
unit_price int,
CONSTRAINT pk_pizza_id PRIMARY KEY(pizza_id)
);

CREATE TABLE ORDERS(
order_no varchar(10),
cust_id varchar(10),
order_date DATE,
delv_date DATE,
CONSTRAINT pk_order_no PRIMARY KEY(order_no)
);

CREATE TABLE ORDER_LIST(
order_no varchar(10),
pizza_id varchar(10),
qty int,
PRIMARY KEY(order_no,pizza_id)
);

ALTER TABLE ORDERS
ADD CONSTRAINT fk_cust_id FOREIGN KEY(cust_id) REFERENCES CUSTOMER(cust_id);

ALTER TABLE ORDER_LIST
ADD CONSTRAINT fk_order_no FOREIGN KEY(order_no) REFERENCES ORDERS(order_no)
ADD CONSTRAINT fk_pizza_id FOREIGN KEY(pizza_id) REFERENCES PIZZA(pizza_id)
MODIFY qty int NOT NULL;

REM customer (cust_id, cust_name, address, phone)

insert into customer values('c001','Hari','32 RING ROAD,ALWARPET',9001200031);
insert into customer values('c002','Prasanth','42 bull ROAD,numgambakkam',9444120003);
insert into customer values('c003','Neethu','12a RING ROAD,ALWARPET',9840112003);
insert into customer values('c004','Jim','P.H ROAD,Annanagar',9845712993);
insert into customer values('c005','Sindhu','100 feet ROAD,vadapalani',9840166677);
insert into customer values('c006','Brinda','GST ROAD, TAMBARAM', 9876543210);
insert into customer values('c007','Ramkumar','2nd cross street, Perambur',8566944453);

REM pizza (pizza_id, pizza_type, unit_price)

insert into pizza values('p001','pan',130);
insert into pizza values('p002','grilled',230);
insert into pizza values('p003','italian',200);
insert into pizza values('p004','spanish',260);
insert into pizza values('p005','supremo',250);

REM orders(order_no, cust_id, order_date ,delv_date)

insert into orders values('OP100','c001','28-JUN-2015','28-JUN-2015');
insert into orders values('OP200','c002','28-JUN-2015','29-JUN-2015');

insert into orders values('OP300','c003','29-JUN-2015','29-JUN-2015');
insert into orders values('OP400','c004','29-JUN-2015','29-JUN-2015');
insert into orders values('OP500','c001','29-JUN-2015','30-JUN-2015');
insert into orders values('OP600','c002','29-JUN-2015','29-JUN-2015');

insert into orders values('OP700','c005','30-JUN-2015','30-JUN-2015');
insert into orders values('OP800','c006','30-JUN-2015','30-JUN-2015');

REM order_list(order_no, pizza_id, qty)

insert into order_list values('OP100','p001',3);
insert into order_list values('OP100','p002',2);
insert into order_list values('OP100','p003',2);
insert into order_list values('OP100','p004',5);
insert into order_list values('OP100','p005',4);

insert into order_list values('OP200','p003',2);
insert into order_list values('OP200','p001',6);
insert into order_list values('OP200','p004',8);

insert into order_list values('OP300','p003',3);

insert into order_list values('OP400','p001',3);
insert into order_list values('OP400','p004',1);

insert into order_list values('OP500','p003',6);
insert into order_list values('OP500','p004',5);
insert into order_list values('OP500','p001',null);

insert into order_list values('OP600','p002',3);
insert into order_list values('OP600','p003',2);

REM: 1.For each pizza, display the total quantity ordered by the customers.

SELECT PIZZA.pizza_id,PIZZA.pizza_type,ORDER_LIST.qty FROM PIZZA
JOIN ORDER_LIST ON PIZZA.pizza_id=ORDER_LIST.pizza_id;

REM: 2.Find the pizza type(s) that is not delivered on the ordered day.

SELECT PIZZA.pizza_id,PIZZA.pizza_type,ORDERS.order_date,ORDERS.delv_date FROM PIZZA
JOIN ORDERS ON ORDERS.order_date!=ORDERS.delv_date;

REM: 3.Display the number of order(s) placed by each customer whether or not he/she placed the order.

SELECT CUSTOMER.cust_id,CUSTOMER.cust_name,COUNT(ORDERS.order_no) FROM CUSTOMER
JOIN ORDERS ON CUSTOMER.cust_id=ORDERS.cust_id
GROUP BY CUSTOMER.cust_id,CUSTOMER.cust_name;

REM: 4.Find the pairs of pizzas such that the ordered quantity of first pizza type is more than the second for the order OP100.

SELECT OL1.pizza_id AS first_pizza_id, OL2.pizza_id AS second_pizza_id FROM ORDER_LIST OL1
JOIN ORDER_LIST OL2 ON OL1.order_no=OL2.order_no
WHERE OL1.order_no='OP100' AND OL1.qty>OL2.qty;

REM: 5.Display the details (order number, pizza type, customer name, qty) of the pizza with ordered quantity more than the 
REM: average ordered quantity of pizzas.

SELECT OL.order_no, P.pizza_type, C.cust_name, OL.qty
FROM PIZZA P
JOIN ORDER_LIST OL ON OL.pizza_id = P.pizza_id
JOIN ORDERS O ON OL.order_no = O.order_no
JOIN CUSTOMER C ON O.cust_id = C.cust_id
WHERE OL.qty > (SELECT AVG(qty) FROM ORDER_LIST);

REM: 6.Find the customer(s) who ordered for more than one pizza type in each order.

SELECT C.cust_id, C.cust_name, O.order_no
FROM CUSTOMER C
JOIN ORDERS O ON C.cust_id = O.cust_id
WHERE O.order_no IN (
    SELECT OL.order_no
    FROM ORDER_LIST OL
    WHERE OL.order_no = O.order_no
    GROUP BY OL.order_no
    HAVING COUNT(DISTINCT OL.pizza_id) > 1
);

REM: 7.Display the details (order number, pizza type, customer name, qty) of the pizza with ordered quantity more than the 
REM: average ordered quantity of each pizza type.

SELECT O.order_no, P.pizza_type, C.cust_name, OL.qty
FROM ORDER_LIST OL
JOIN ORDERS O ON O.order_no = OL.order_no
JOIN CUSTOMER C ON C.cust_id = O.cust_id
JOIN PIZZA P ON P.pizza_id = OL.pizza_id
WHERE OL.qty > (SELECT AVG(OL2.qty) FROM ORDER_LIST OL2 WHERE OL2.pizza_id = OL.pizza_id);

REM: 8.Display the details (order number, pizza type, customer name, qty) of the pizza with ordered quantity more than the 
REM: average ordered quantity of its pizza type. (Use correlated)

SELECT OL.order_no,P.pizza_type,C.cust_name,OL.qty FROM ORDER_LIST OL
JOIN PIZZA P ON P.pizza_id=OL.pizza_id
JOIN ORDERS O ON O.order_no=OL.order_no
JOIN CUSTOMER C ON C.cust_id=O.cust_id
WHERE OL.qty>(SELECT AVG(qty) FROM ORDER_LIST WHERE OL.pizza_id=P.pizza_id);

REM: 9.Display the customer details who placed all pizza types in a single order.

SELECT C.cust_id,C.cust_name FROM CUSTOMER C
WHERE C.cust_id IN (SELECT O.cust_id FROM ORDERS O
                    JOIN ORDER_LIST OL ON OL.order_no=O.order_no
					GROUP BY O.cust_id HAVING COUNT(DISTINCT OL.pizza_id)=5
);

REM: 10.Display the order details that contains the pizza quantity more than the average quantity of any of Pan or Italian pizza type.

SELECT order_no,pizza_id FROM ORDER_LIST
WHERE qty>(SELECT AVG(OL.qty) FROM ORDER_LIST OL
           JOIN PIZZA P ON P.pizza_type='pan')
UNION
SELECT order_no,pizza_id FROM ORDER_LIST
WHERE qty>(SELECT AVG(OL.qty) FROM ORDER_LIST OL
           JOIN PIZZA P ON P.pizza_type='italian');

REM: 11.Find the order(s) that contains Pan pizza but not the Italian pizza type.

SELECT order_no,pizza_id FROM ORDER_LIST
WHERE pizza_id IN (SELECT pizza_id FROM PIZZA
                   WHERE pizza_type='pan')
MINUS 
SELECT order_no,pizza_id FROM ORDER_LIST
WHERE pizza_id IN (SELECT pizza_id FROM PIZZA
                   WHERE pizza_type='italian');
);

REM: 12. Display the customer(s) who ordered both Italian and Grilled pizza type.

SELECT C.cust_id,C.cust_name FROM CUSTOMER C
JOIN ORDERS O ON O.cust_id=C.cust_id
JOIN ORDER_LIST OL ON OL.order_no=O.order_no
JOIN PIZZA P ON P.pizza_id=OL.pizza_id
WHERE P.pizza_id IN (SELECT pizza_id FROM PIZZA
                     WHERE pizza_type='italian')
INTERSECT
SELECT C.cust_id,C.cust_name FROM CUSTOMER C
JOIN ORDERS O ON O.cust_id=C.cust_id
JOIN ORDER_LIST OL ON OL.order_no=O.order_no
JOIN PIZZA P ON P.pizza_id=OL.pizza_id
WHERE P.pizza_id IN (SELECT pizza_id FROM PIZZA
                     WHERE pizza_type='grilled');
