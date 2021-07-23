use bmi_db;

delimiter $$
drop trigger if exists t2 $$
create trigger t2 before insert on ht for each row
begin
	if (new.ft < 1) or (new.ft > 80) then
		signal SQLSTATE '10111' set message_text = "Invalid feet";
	end if;
	if (new.inc < 0) or (new.inc > 11) then
		signal SQLSTATE '21314' set message_text = "Invalid inches";
	end if;
end $$

delimiter ;