create database dataanalytics;

use dataanalytics;

create table persons(
	person_id int,
    lastname varchar(30),
    firstname varchar(20),
    adress varchar(40)
    ,city varchar(20)
    );
    
insert into persons values(1,"noel","christ","ls_apartments","lonavala");
insert into persons values(2,"noellong","christ","sl_apartments","lonavala");
insert into persons values(3,"noelbottom","christ","slasss_apartments","lonavala");
insert into persons values(3,"noelbotm","christ","slasss_apartments","lonavala");

select * from persons;
delete from persons where person_id=2;
SET SQL_SAFE_UPDATES = 0;
update persons set firstname="suman" where person_id=1;
select * from persons;

create table user5(
	userid int auto_increment primary key,
    username varchar(50) unique not null,
    email varchar(29) unique not null,
    password1 varchar(100) not null,
    firstname varchar(30),
    lastname varchar(30),
    dateofbirth date,
    createdat datetime default current_timestamp,
    lastlogin datetime,
    statues enum("active","inactive","suspended") default "active",
    index(email)
    );
    
#insert into user5(username,email,password1,firstname,lastname,dateofbirth,lastlogin) values('hari','hari@44','hari@3','itha','hari',1101-04-03,now())
create table student(
	studentid int primary key,
    name varchar(100),
    age int,
    check(age>18)
    );
insert into student values(1,"sumanh",24);
select * from student;
create table enrollments(
	enrollmentid int primary key,
    studentid int,
    courseid int,
    foreign key(studentid) references student(studentid)
    );
insert into enrollments values(1,1,1);

create table orderdetails(
orderid int,
productid int,
quantity int,
primary key(orderid,productid)
);
select * from orderdetails;  
create table products(pid int, productname varchar(30),price int);
insert into products values(1,"activa",60000),(2,"yamaha",90000),(3,"suzuki",99000),(1,"maruthi",80000);
insert into products values(2,"tesla",40000);
select * from products;
select min(price)

from products;
select min(price) as smallestprice,pid
from products
group by pid;
select avg(price) as avgprice,pid
from products
group by pid;

select count(pid) as numofcol#in bracket u can use specific or * anything is ok
from products;
#for counting how many values greater than 80k
select count(pid)
from products
where price>80000;

select count(distinct pid)
from products;

select sum(price) as total
from products;

create table customer(
cid int primary key,
cname varchar(30));
create table orders(
oid int primary key,
cid int,
product varchar(30),
foreign key(cid) references customer(cid)
on delete cascade);

insert into customer values(1,"ayyapa"),(2,"yasin"),(3,"mariyam"),(4,"bhairava");
insert into orders values(1,1,"idli"),(2,2,"dosa"),(3,3,"poori"),(4,4,"biryani");
select * from customer;
select * from orders;
delete from customer where cid=1;

select * from products
order by(price);

select pid,price*1.5 as ofroadprice
from products
order by ofroadprice desc;

CREATE TABLE Customerstable (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    ContactName VARCHAR(100),
    Country VARCHAR(50)
);
 
CREATE TABLE Orderstable (
    OrderID INT PRIMARY KEY,
    OrderDate DATE,
    CustomerID INT,
    Amount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customerstable(CustomerID)
);
 
INSERT INTO Customerstable (CustomerID, CustomerName, ContactName, Country) VALUES
(1, 'John Doe', 'John D.', 'USA'),
(2, 'Jane Smith', 'Jane S.', 'UK'),
(3, 'Alice Brown', 'Alice B.', 'Canada'),
(4, 'Bob Johnson', 'Bob J.', 'Australia');
 
INSERT INTO Orderstable (OrderID, OrderDate, CustomerID, Amount) VALUES
(101, '2024-09-01', 1, 250.00),
(102, '2024-09-05', 2, 300.00),
(103, '2024-09-07', 1, 150.00),
(104, '2024-09-10', 3, 450.00);

select * from customerstable;
select * from orderstable;

select customerstable.customerid,
customerstable.customername,
orderstable.orderid,
orderstable.amount
from customerstable join orderstable on customerstable.customerid=orderstable.customerid;

create table drinks(
did int,
dname varchar(10));

create table snacks(
sid int,
sname varchar(30));

insert into drinks values(1,"tea"),(2,"cofee"),(3,"milk");
insert into snacks values(1,"samosa"),(2,"gobi"),(3,"puff");
select 
drinks.did,
drinks.dname,
snacks.sid,
snacks.sname
from drinks cross join snacks;


create table employee(empid int,ename varchar(20),jobdesc varchar(20),salaary int,hiredate date);
insert into employee values(1,"ram","developer",60000,date '2023-05-11'),(2,"omkar","sde",40000,date '2024-05-15');
insert into employee values(3,"rahman","developer",30000,date '2025-05-11'),(4,"omrauth","sde",70000,date '2022-05-15');
insert into employee values(5,"ramya","dataanalyst",50000,date '2021-05-11'),(6,"omram","sde3",90000,date '2020-05-15');
select * from employee order by jobdesc;

select jobdesc,avg(salaary) from employee group by jobdesc;
select jobdesc,count(empid) from employee group by jobdesc;

select jobdesc,count(empid)
from employee
group by jobdesc
having count(empid)>1
order by jobdesc;

select jobdesc,count(empid)
from employee where salaary>30000
group by jobdesc
having count(empid)>1
order by jobdesc;


select ename,salaary
from employee
where salaary>(select avg(salaary) from employee);


CREATE TABLE departments (

    department_id INT PRIMARY KEY,

    department_name VARCHAR(50)

);
 
CREATE TABLE employees (

    employee_id INT PRIMARY KEY,

    employee_name VARCHAR(50),

    department_id INT,

    FOREIGN KEY (department_id) REFERENCES departments(department_id)

);

INSERT INTO departments (department_id, department_name) VALUES

(1, 'Sales'),

(2, 'Marketing'),

(3, 'HR');
 
INSERT INTO employees (employee_id, employee_name, department_id) VALUES

(101, 'Alice', 1),

(102, 'Bob', 1),

(103, 'Charlie', 2),

(104, 'Diana', 3);
 
select * from departments;
select * from employees;

select employee_name
from employees
where department_id in(
	select department_id from departments
    where department_name="sales"
    );

select employee_name,
	(select department_name
    from departments
    where departments.department_id=employees.department_id)as department_name
from employees;

select employee_name
from employees
where department_id in(select department_id
	from employees
    group by department_id
    having count(*)>1);
    
INSERT INTO employees(employee_name, department_id) VALUES ('Alice', 1);
    
    
    
select department_name
from department d
where exists(select 1
from employees e
where e.department_id=d.department_id);

select ucase("hello world") as upper;
select lcase("hello world") as lower;
select mid("hello world",4,7)as substring;
select length("hello world") as lengthofstr;
select round(1234.8765,2)as roundval;
select now() as currentdate;
select format(1234,5656,2)as formats;

select employee_name,length(employee_name)as lengname from employees;


create table users(
	userid int auto_increment,
    name1 varchar(30),
    primary key(userid)
    );
 insert into users(name1) values("happy"),("varun"),("vijay"),("vaman");
 insert into users(name1) values(null),(null),(null);
select * from users;
alter table users auto_increment=1001;
select userid,coalesce(name1,'default') as names from users;
start transaction;
savepoint point;
insert into users(name1) value("hurray");
insert into users(name1) value("huppy");
rollback to point;
commit;

DELIMITER //
create procedure getusers1()
begin
	select *from users;
end;
//

call getusers1();

delimiter //



CREATE DATABASE imdb_movie_project;

USE imdb_movie_project;

CREATE TABLE movie_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    year INT,
    rating FLOAT,
    genre VARCHAR(255),
    director VARCHAR(255),
    actors TEXT,
    runtime INT,
    revenue FLOAT
);

create database imdb_database;
create database imdb_movies;


CREATE TABLE imdb_movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(100),
    description TEXT,
    director VARCHAR(255),
    actors TEXT,
    year INT,
    runtime INT,
    rating FLOAT,
    votes INT,
    revenue FLOAT,
    metascore FLOAT
);
create database imdb_db;
show databases;
use imdb_db;
show tables;
describe movies;
CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    director VARCHAR(255),
    year INT,
    runtime INT,
    rating DECIMAL(3, 1),
    votes INT,
    revenue DECIMAL(20, 2)
);
show tables;
SELECT * FROM movies LIMIT 10;

use imdb_db;
CREATE DATABASE imdb_movie_analysis_v2;
use imdb_movie_analysis_v2;

CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    director VARCHAR(255),
    year INT,
    runtime INT,
    rating FLOAT,
    votes INT,
    revenue FLOAT
);
select * from movies;
desc movies;



create database IMDB;

-- Check current plugin
SELECT user, host, plugin FROM mysql.user WHERE user = 'sparkuser';

-- Recreate the user correctly (this overrides any previous setup)
DROP USER IF EXISTS 'sparkuser'@'%';
CREATE USER 'sparkuser'@'%' IDENTIFIED WITH mysql_native_password BY 'Spark@123';
GRANT ALL PRIVILEGES ON spark_output.* TO 'sparkuser'@'%';
FLUSH PRIVILEGES;







