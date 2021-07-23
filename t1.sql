use bmi_db;

delimiter $$
drop trigger if exists t1 $$
create trigger t1 before insert on bmi for each row
begin
	if (length(new.name) < 2) or not (new.name regexp "^[A-z ]*$") then
		signal SQLSTATE '12345' set message_text = "Invalid name";
	end if;
	if (new.age < 1) or (new.age > 100) then
		signal SQLSTATE '23456' set message_text = "Invalid age";
	end if;
	if (length(new.phone) < 10) or not (new.phone regexp "^[0-9]*$") then
		signal SQLSTATE '34567' set message_text = "Invalid phone number";
	end if;
	if (new.ht < 50) or (new.ht > 2400) then
		signal SQLSTATE '45678' set message_text = "Invalid height";
	end if;
	if (new.wt < 3) or (new.age > 500) then
		signal SQLSTATE '56789' set message_text = "Invalid weight";
	end if;
end $$

delimiter ;