create database OrderManagement;

use OrderManagement;

create table Products (
	productId int primary key,
	productName varchar(100),
	description varchar(255),
	price decimal(10,2),
	quantityInStock int,
	type varchar(20) check (type in ('Electronics','Clothing'))
	);

create table Electronics (
	productId int primary key,
	brand varchar(50),
	warrantyPeriod int,
	foreign key (productId) references Products(productId)
	);

create table Clothing (
	productId int primary key,
	size nvarchar(10),
	color varchar(20),
	foreign key (productId) references Products(productId)
	);

create table Users (
	userId int primary key,
	username nvarchar(50),
	password nvarchar(50),
	role varchar(20) check (role in ('Admin', 'User'))
	)

create table orders (
	orderId int primary key identity(1,1),
	userId int,
	foreign key (userid) references Users(userId)
	)

create table OrderDetails (
	orderDetailId int primary key identity(1,1),
	orderId int,
	productId int,
	quantity int,
	foreign key (orderId) references Orders(orderId),
	foreign key (productId) references Products(productId)
	)

insert into Products values
(1, 'Vivo Smartphone','Mid-Range Smartphone',20000.00,50,'Electronics'),
(2, 'HP Laptop','Gaming Laptop',50000.00,60,'Electronics'),
(3, 'T-Shirt','Casual Wears',700.00,30,'Clothing'),
(4, 'Pants','Formal Pants',300.00,40,'Clothing');

insert into Electronics values
(1,'Vivo',2),
(2,'HP',2)

insert into Clothing values
(3, 'M','Blue'),
(4, 'M','Black')

insert into Users values
(1, 'Sai', 'password123', 'User'),
(2, 'Subash', 'admin', 'Admin');

select * from Users;
insert into orders values
(1),
(2),
(3)

--insert into OrderDetails values
--(1, 1, 2),
--(1, 3, 3),
--(2, 2, 1),
--(3, 4, 2);

insert into orders (userId) values
(1),
(2),
(1);

select * from orders; 
-- Check in the Orders table before inserting values for the OrderDetails
-- As in some times there can be ForeignKey error if orderId is not matched correctly 
-- with the orderid in orders table

--insert into OrderDetails values
--(16, 1, 2),
--(17, 3, 3),
--(18, 2, 1);

select * from Users;

SELECT o.orderId, od.productId, p.productName, od.quantity FROM Orders o 
INNER JOIN OrderDetails od ON o.orderId = od.orderId 
INNER JOIN Products p ON od.productId = p.productId 
WHERE o.userId = 1

select * from OrderDetails;
