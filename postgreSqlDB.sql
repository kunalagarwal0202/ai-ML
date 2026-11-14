
select * from actor;
select distinct first_name from actor;
select count (distinct first_name) from actor;
select last_nam,first_name from actor where last_name='guiness'
explain analyze select * from actor where last_name='%ness'
explain analyze select first_name from actor
create index first_name_index on actor(first_name)
explain analyze select count(first_name) from actor;
SELECT actor  FROM information_schema.tables  WHERE table_schema = 'public';

select count(distinct staff_id) from payment;
select * from payment;

select * from actor where first_name LIKE'%a%'

select count(customer_id), staff_id from payment group by staff_id;
select customer_id, staff_id, rental_id from payment order by rental_id;


SELECT SUM(amount) from payment;
select max(amount) from payment;
select min(amount) from payment;

select avg(amount) from payment;

select * from payment where amount=(Select max(amount) from payment) limit 5

select count(first_name), last_name, first_name from actor group by last_name, first_name

select * from actor
Kenneth Paltrow

insert into actor values (9001, 'Kenneth', 'Paltrow')

select * from payment where amount >10 order by amount desc
select * from payment where amount != 10.99 order by amount desc
select * from payment where amount =10.99
select * from payment where amount <=10 order by amount desc
select * from actor where first_name not LIKE'%A%'
SELECT * FROM actor where first_name='Fay' or last_name='Hope'

select * from payment where amount between 8 and 10


create table employee(
employee_id int primary key,
employee_name varchar(100),
payment_id int,
FOREIGN KEY (payment_id)
    REFERENCES payment(payment_id)
)
insert into employee values (1,'test',17503), (2,'test2',17504), (3,'test3',17505)

select employee_id, amount from employee join payment on employee.payment_id=payment.payment_id



