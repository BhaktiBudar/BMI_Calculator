drop database if exists bmi_db;
create database if not exists bmi_db;
use bmi_db;

drop table if exists bmi;

create table if not exists bmi
(
id int primary key auto_increment,
name varchar(20) not null,
age int not null,
phone varchar(10) not null,
gender varchar(20) not null,
ht int not null,
wt int not null
);

desc bmi;

