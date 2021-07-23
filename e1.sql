use bmi_db;

delimiter $$
drop event if exists e1 $$
create event e1 on schedule every 1 minute do
begin
delete from bmi_bkup;
insert into bmi_bkup select * from bmi;
end $$
delimiter ;