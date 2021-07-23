use bmi_db;

delimiter $$
drop event if exists e2 $$
create event e2 on schedule every 1 minute do
begin
delete from ht_bkup;
insert into ht_bkup select * from ht;
end $$
delimiter ;