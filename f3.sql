use bmi_db;
delimiter $$
drop function if exists f3 $$
create function f3() returns varchar(50) DETERMINISTIC
begin
return current_timestamp();
end $$
delimiter ;