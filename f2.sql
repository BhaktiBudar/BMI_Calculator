use bmi_db;
delimiter $$
drop function if exists f2 $$
create function f2() returns varchar(200) DETERMINISTIC
begin
declare h int;
declare msg varchar(100);
set h = hour(current_timestamp());
if (h < 11) then set msg = 'Good Morning';
end if;
if (h > 12) or (h < 15) then set msg = 'Good Afternoon';
end if;
if (h > 16) then set msg = 'Good Evening';
end if;
return msg;
end $$
delimiter ;