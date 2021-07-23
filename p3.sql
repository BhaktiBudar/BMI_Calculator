use bmi_db;

drop table if exists bmi_bkup;
drop table if exists ht_bkup;

create table if not exists bmi_bkup
(
id int primary key,
name varchar(20) not null,
age int not null,
phone varchar(10) not null,
gender varchar(20) not null,
ht int not null,
wt int not null
);

create table if not exists ht_bkup
(
id int primary key,
ft int not null,
inc int not null
);

desc bmi_bkup;
desc ht_bkup;
