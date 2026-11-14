use hdfc_database;
create table newTable(
 Employeename varchar(100) NOT NULL,
 EmployeeAge int DEFAULT 99,
 EmployeeSalary int);
 
 show tables;
 
 select * from newTable where Employeename ='Krishna';
  select * from newTable where Employeename='Teja' and EmployeeSalary<1500;
 
 select * from newTable
 insert into newTable values ('Teja', 20,1200);
 insert into newTable values ('Krishna', 20,1200);
  
 insert into newTable values ('Madhu', 20,1200);
 insert into newTable values ('Gocvinda', 20,1200);
 
  
 insert into newTable values ('Ram', 20,1200);
 insert into newTable values ('Laxman', 20,1200);
 
  
 insert into newTable values ('Ravi', 20,1200);
 insert into newTable values ('Mahesh', 20,1200);
 
  insert into newTable values ('Rukmini', 21,1200);
 
  insert into newTable values ('Teja', 20,1500);
  
  insert into newTable  (Employeename, EmployeeSalary) values ("omprakas",2500);
  
  create table mytable;
  drop table student;
  
  
  
create table employeeTable(
 Employeename varchar(100) NOT NULL,
 EmployeeAge int DEFAULT 99,
 EmployeeSalary int,
 employeeID int PRIMARY KEY );
 

 
insert into employeeTable (Employeename,EmployeeAge, EmployeeSalary,employeeID) values ('Teja', 20,1500, 10),('Rukmini', 21,1200,20);
select  Employeename,EmployeeAge from employeeTable where employeeAge>20;
insert into employeeTable (Employeename,EmployeeAge, EmployeeSalary,employeeID) values ('testDaat', 20,2500, 555);

update employeeTable set Employeename='Neha' where Employeename='Manideep';

 select * from employeeTable where Employeename='Manideep';
 
 update employeeTable set Employeename='Neha' ;
 
 delete from  employeeTable where Employeename='Manideep';

select  count(Employeename) from employeeTable;

select * from employeeTable where EmployeeSalary LIKE '%00%';
select count(*) from employeeTable where EmployeeSalary LIKE '%1200%';


select EmployeeSalary, count(*) from employeeTable group by EmployeeSalary;

select Employeename, max(EmployeeSalary)  from employeeTable;

SET SESSION sql_mode = REPLACE(@@SESSION.sql_mode, 'ONLY_FULL_GROUP_BY', '');

select Employeename from employeeTable where EmployeeSalary =(select max(EmployeeSalary) from employeeTable);
  
  select sum(EmployeeSalary) from employeeTable group by EmployeeSalary;
    select avg(EmployeeSalary) from employeeTable;
    select avg(EmployeeSalary) from employeeTable group by EmployeeAge;
    
select * from helloworld_student;








create table helloworld_employee (
employee_name varchar(100),
employee_email varchar(100),
employee_age int)





select * from employee;

create table employee (
employee_name varchar(20),
employee_email varchar(100),
employee_age int);
show tables;
drop table employee;
select * from employee;
select employee_name, employee_email from employee;
/* select means to view the current record
insert to insert new record of data
create-->to create tables and databases
delete-->to delete existing records
update-->to update any current existing record*/

insert into employee (employee_name,employee_email, employee_age) values ('Teja', 'teja@gmail.com', 10),('Teja', 'teja@gmail.com', 10);
insert into employee (employee_name,employee_email, employee_age) values ('Teja2', 'teja@gmail.com', 23),('Teja2', 'teja@gmail.com', 23);

update employee set employee_name="test" where employee_age=10;
delete from employee where employee_age=10;


create table employee_2 (
employeeID int primary key,
employee_name varchar(20),
employee_email varchar(100),
employee_age int);

insert into employee_2 (employeeID, employee_name,employee_email, employee_age) values (130,'Teja2', 'teja@gmail.com', 14),(203,'Teja2', 'teja@gmail.com', 3);
insert into employee_2 (employeeID, employee_name,employee_email, employee_age) values (1010,'Teja2', 'teja@gmail.com', 13),(2010,'Teja2', 'teja@gmail.com', 14);
insert into employee_2 (employeeID, employee_name,employee_email, employee_age) values (1014,'Teja2', 'teja@gmail.com', 40),(2014,'Teja2', 'teja@gmail.com', 12);
insert into employee_2 (employeeID, employee_name,employee_email, employee_age) values (1011,'Ram2', 'ram@yahoo.com', 35),(2101,'krishna', 'krishna@gmail.com', 89);

select * from employee_2;
update employee_2 set employee_name="ram" where employeeID=10;
 delete from employee_2 where employee_age=23;
 show tables;
 drop table employee_2;
 select max(employee_age) from employee_2;
 select * from employee_2 where employee_age=18;
  select * from employee_2 order by employee_age desc;
  select count(*),sum(employee_age) from employee_2 group by employeeID;
  
  select * from employee_2;
  ALTER TABLE employee_2
  ADD employee_designation varchar(100);

ALTER TABLE employee_2
DROP COLUMN employee_designation;

ALTER TABLE employee_2
RENAME COLUMN employee_age to employee_dob;

ALTER TABLE employee_2
MODIFY employeeID varchar(10) NOT NULL;

ALTER TABLE employee_2
ADD employee_designation varchar(30) default ('software dev');


SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;

create table cutomers (
cusID int primary key,
CusName varchar(20),
CusOrderId int,

FOREIGN KEY (CusOrderId)
REFERENCES orders(orderID));

create table orders(
orderID int primary key,
productName varchar(20),
customerID int);
insert into cutomers values (1011,'Ram2', 35);

insert into cutomers values (101,'laxman', 35),(2101,'krishna', 890);
insert into cutomers values (1012,'Om Prakash', 359),(2108,'neha', 894);
insert into cutomers values (1014,'Santosh', 354),(2109,'Atul', 819);
insert into cutomers values (1017,'Charan', 37),(2104,'Shreesha', 859);
insert into cutomers values (10111,"test",Null);

insert into orders values (359, "laptop", 1011);
insert into orders values (354, "mobile", 1012);
insert into orders values (37, "mouse", 1011);
insert into orders values (890, "iphone", 2101);
insert into orders values (894, "wire", 2108);
insert into orders values (819, "tv", 2104);
insert into orders values (859, "washing machine", 1017);
insert into orders values (990,"washing poweder",555);

select * from cutomers;
select * from orders;


Select * from cutomers;
select * from orders;

Select count(CusOrderId) from cutomers;
select sum(CusOrderId) from cutomers where cusID=2108;
select max(cusID)   from cutomers ;
select distinct (CusName) from cutomers limit 5;

select * from cutomers order by CusName desc limit 5;

select CusName, sum(cusID) from cutomers group by CusName;
ALTER TABLE orders 
ADD produtc_value int default (4009) NOT NULL;




/*alter table "table_name add/drop/rename/Modify column_name constraints*/
ALTER TABLE cutomers 
ADD customer_age int default (40) NOT NULL;

ALTER TABLE cutomers 
ADD customer_Address varchar(100) NOT NULL;

ALTER TABLE cutomers
DROP COLUMN customer_Address;

ALTER TABLE cutomers
RENAME COLUMN CusOrderId to cutomers;

ALTER TABLE cutomers
MODIFY order_id varchar(10) NOT NULL;
insert into cutomers (cusID,CusName,CusOrderId) values (106586,'Charan', 37),(5216084,'Shreesha', 859);






SELECT cusName,orders.orderID, productName, produtc_value
FROM orders
inner JOIN cutomers
ON cutomers.order_id = orders.orderID;

create table test_app1_student (
Std_name varchar(20),
email  varchar(20),
age int)
