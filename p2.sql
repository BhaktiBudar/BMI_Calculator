use bmi_db;

drop table if exists ht;

create table if not exists ht
(
id int primary key auto_increment,
ft int not null,
inc int not null
);

desc ht;
