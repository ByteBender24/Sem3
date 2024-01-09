REM| Author : Harishraj S
REM| Date : 16-10-2023


REM| Write the following using JOIN:
REM| 1. For each pizza, display the total quantity ordered by the customers.

SELECT PIZZA.pizza_id, PIZZA.pizza_type, SUM(ORDER_LIST.qty) as "TOTAL QUANTITY"
FROM PIZZA
LEFT JOIN ORDER_LIST
-- LET IT BE LEFT JOIN (so that even if no pizza is been ordered, it can be shown as NULL)
ON PIZZA.pizza_id =  ORDER_LIST.pizza_id
GROUP BY PIZZA.pizza_id, PIZZA.pizza_type;

REM| 2. Find the pizza type(s) that is not delivered on the ordered day

SELECT PIZZA.pizza_type, ORDERS.order_date, ORDERS.delv_date
FROM PIZZA
RIGHT JOIN ORDER_LIST
ON ORDER_LIST.pizza_id = PIZZA.pizza_id
RIGHT JOIN ORDERS
ON ORDER_LIST.order_no = ORDERS.order_no
WHERE ORDERS.order_date != ORDERS.delv_date
ORDER BY PIZZA.pizza_id;

-- SEE WHETHER TO USE RIGHT JOIN, LEFT JOIN, carefully
-- For dates with null values

REM| 3.Display the number of order(s) placed by each customer whether or not
REM| he/she placed the order.

SELECT CUSTOMER.cust_id, CUSTOMER.cust_name, count(ORDERS.order_no) as No_of_orders
FROM CUSTOMER
RIGHT JOIN ORDERS
ON CUSTOMER.cust_id = ORDERS.cust_id
GROUP BY CUSTOMER.cust_id, CUSTOMER.cust_name;

REM| 4. Find the pairs of pizzas such that the ordered quantity of first pizza type is
REM| more than the second for the order OP100.

SELECT OL1.pizza_id AS first_pizza, OL2.pizza_id AS second_pizza
FROM ORDER_LIST OL1
JOIN ORDER_LIST OL2 
ON OL1.order_no = OL2.order_no
WHERE OL1.order_no = 'OP100' AND OL1.qty > OL2.qty;
