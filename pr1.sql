use bmi_db;

delimiter $$
drop procedure if exists pr1 $$
create procedure pr1(out info varchar(1000))
begin
declare i int default 0;
declare n varchar(20) default "";
declare a int default 0;
declare p varchar(10) default "";
declare g varchar(20) default "";
declare h int default 0;
declare ht float default 0;
declare w int default 0;
declare bmi float default 0;
declare msg varchar(50) default "";

declare c1 cursor for select * from bmi order by id desc limit 1;

set info = "";
open c1;
fetch c1 into i, n, a, p, g, h, w;
set ht = h/100;
set bmi = w/power(ht,2);
if bmi < 18.5 then set msg = "Underweight";
end if;
if (bmi > 18.5) and (bmi < 24.9) then set msg = "Normal weight";
end if;
if (bmi > 25.0) and (bmi < 29.9) then set msg = "Pre-obesity";
end if;
if (bmi > 30.0) and (bmi < 34.9) then set msg = "Obesity class I";
end if;
if (bmi > 35.0) and (bmi < 39.9) then set msg = "Obesity class II";
end if;
if bmi > 39.9 then set msg = "Obesity class III";
end if;
set info = concat("Name = ", n, "\nAge = ", a, "\nPhone = ", p, "\nGender = ", g, "\nBMI = ", bmi, "\n", msg);

end $$
delimiter ;