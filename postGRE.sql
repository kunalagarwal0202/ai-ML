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

SELECT SUM(amount) from payment;
select max(amount) from pa
