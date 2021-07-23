use bmi_db;

delimiter $$
drop procedure if exists pr2 $$
create procedure pr2(out info varchar(1000))
begin
declare i int default 0;
declare f int default 0;
declare inches int default 0;
declare inch int default 0;
declare cm float default 0;

declare c1 cursor for select * from ht order by id desc limit 1;

set info = "";
open c1;
fetch c1 into i, f, inch;
set inches = (f * 12) + inch;
set cm = inches * 2.54;
set info = concat("Feet = ", f, "\nInches = ", inch, "\nHeight in cm = ", cm);

end $$
delimiter ;