CREATE DATABASE grocery_store_db;

USE grocery_store_db;

SHOW DATABASES;

#Product Table
CREATE TABLE products(
product_id INT AUTO_INCREMENT PRIMARY KEY,
product_name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10,2),
stock INT
);

#Customer Table
CREATE TABLE customers(
customer_id INT AUTO_INCREMENT PRIMARY KEY,
customer_name VARCHAR(100),
phone VARCHAR(15)
);

#Order Table
CREATE TABLE orders(
order_id INT AUTO_INCREMENT PRIMARY KEY,
customer_id INT,
product_id INT,
quantity INT,
total_price DECIMAL(10,2)
);

SHOW TABLES;

SELECT * FROM products;

SELECT * FROM orders;

SELECT * FROM customers;