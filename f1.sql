use bmi_db;
delimiter $$
drop function if exists f1 $$
create function f1() returns int DETERMINISTIC
begin
declare co int default 0;
select count(*) into co from bmi;
return co;
end $$
delimiter ;