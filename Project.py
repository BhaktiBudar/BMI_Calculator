from tkinter import *
from datetime import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import mysql.connector
import os

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="abc123"
)

def f1():
	bmi_window.deiconify()
	main_window.withdraw()

def f2():
	view_window.deiconify()
	main_window.withdraw()
	view_window_st_data.delete(1.0, END)
	info = ''
	con = None
	try:
		con = mysql.connector.connect(host="localhost", user="root", password="abc123", database="bmi_db")
		cursor = con.cursor()
		sql = "select * from bmi"
		cursor.execute(sql)
		data = cursor.fetchall()
		un = "\n--------------------------------------------------\n"
		for d in data:
			info = info + "Name: " + str(d[0]) + "\nAge: " + str(d[1]) + "\nPhone" + str(d[2]) + "\nGender: " + str(d[3]) + "\nHeight: " + str(d[4]) + "\nWeigth: " + str(d[5]) + un
		view_window_st_data.insert(INSERT, info)
	except Exception as e:
		showerror('Failure', e)
	finally:
		if con is not None:
			con.close()

def f4():
	convert_window.deiconify()
	bmi_window.withdraw()

def f5():
	con = None
	try:
		con = mysql.connector.connect(host="localhost", user="root", password="abc123", database="bmi_db")
		cursor = con.cursor()
		sql = "insert into bmi (name, age, phone, gender, ht, wt) values ('%s', '%d', '%s', '%s', '%d', '%d')"
		name = bmi_window_ent_name.get()
		age = int(bmi_window_ent_age.get())
		phone = int(bmi_window_ent_phone.get())
		selection = f9()
		if selection == "2":
			gender = "Female"
		else:
			gender = "Male"
		ht = int(bmi_window_ent_ht.get())
		wt = int(bmi_window_ent_wt.get())
		cursor.execute(sql % (name, age, phone, gender, ht, wt))
		con.commit()
		args = [0]
		result_args = cursor.callproc('pr1', args)
		showinfo('BMI', result_args[0])
		bmi_window_ent_name.delete(0,END)
		bmi_window_ent_age.delete(0, END)
		bmi_window_ent_phone.delete(0,END)
		bmi_window_rb_male.select()
		bmi_window_ent_ht.delete(0, END)
		bmi_window_ent_wt.delete(0,END)
	except ValueError:
		showerror('Failure', "ValueError:\nYou need to enter correct values in each field")
	except Exception as e:
		showerror('Failure', e)
	finally:
		if con is not None:
			con.close()

def f6():
	main_window.deiconify()
	bmi_window.withdraw()
	bmi_window_rb_male.select()

def f7():
	con = None
	try:
		con = mysql.connector.connect(host="localhost", user="root", password="abc123", database="bmi_db")
		cursor = con.cursor()
		sql = "insert into ht (ft, inc) values ('%d', '%d')"
		ft = int(convert_window_ent_ft.get())
		inc = int(convert_window_ent_inc.get())
		cursor.execute(sql % (ft, inc))
		con.commit()
		args = [0]
		result_args = cursor.callproc('pr2', args)
		showinfo('Height', result_args[0])
		convert_window_ent_ft.delete(0, END)
		convert_window_ent_inc.delete(0,END)
		bmi_window.deiconify()
		convert_window.withdraw()
	except ValueError:
		showerror('Failure', "ValueError:\nYou need to enter correct values in each field")
	except Exception as e:
		showerror('Failure', e)
	finally:
		if con is not None:
			con.close()
def f8():
	main_window.deiconify()
	view_window.withdraw()

def f9():
	selection = str(var.get())
	return selection

def f10():
	con = None
	try:
		con = mysql.connector.connect(host="localhost", user="root", password="abc123", database="bmi_db")
		cursor = con.cursor()
		sql = "select f1()"
		cursor.execute(sql)
		co = cursor.fetchall()
		return co
	except Exception as e:
		showerror('Failure', e)
	finally:
		if con is not None:
			con.close()

def f3():
	con = None
	try:
		con = mysql.connector.connect(host="localhost", user="root", password="abc123", database="bmi_db")
		cursor = con.cursor()
		c = f10()
		co = c[0]
		d = co[0]
		sql = "select * into outfile 'C:/backup/bk" + str(d) + ".txt' from bmi"
		cursor.execute(sql)
		showinfo('Success', 'Data exported successfully')
	except Exception as e:
		showerror('Failure', e)
		print(e)
	finally:
		if con is not None:
			con.close()

def f11():
	con = None
	try:
		con = mysql.connector.connect(host="localhost", user="root", password="abc123", database="bmi_db")
		cursor = con.cursor()
		sql = "select f2()"
		cursor.execute(sql)
		msg = cursor.fetchall()
		m = msg[0]
		return m[0]
	except Exception as e:
		showerror('Failure', e)
	finally:
		if con is not None:
			con.close()
def f12():
	con = None
	try:
		con = mysql.connector.connect(host="localhost", user="root", password="abc123", database="bmi_db")
		cursor = con.cursor()
		sql = "select f3()"
		cursor.execute(sql)
		dt = cursor.fetchall()
		t = dt[0]
		return t[0]
	except Exception as e:
		showerror('Failure', e)
	finally:
		if con is not None:
			con.close()

def f13():
	bmi_window.deiconify()
	convert_window.withdraw()

main_window = Tk()
main_window.title("BMI Calculator")
main_window.geometry("400x350+150+0")
main_window.configure(background = 'lightskyblue')

var = IntVar()

main_window_lbl_dt = Label(main_window, text = f12(), font = ('Arial', 15, 'bold'), background = 'gray93')
main_window_lbl_msg = Label(main_window, text = f11(), font = ('Arial', 15, 'bold'), background = 'gray93')
main_window_btn_bmi = Button(main_window, text = "Calculate BMI", font = ('Arial', 15, 'bold'), width = 15, command = f1)
main_window_btn_view = Button(main_window, text = "View History", font = ('Arial', 15, 'bold'), width = 15, command = f2)
main_window_btn_export = Button(main_window, text = "Export Data", font = ('Arial', 15, 'bold'), width = 15, command = f3)
main_window_lbl_count = Label(main_window, text = f10(), font = ('Arial', 15, 'bold'), background = 'gray93')

main_window_lbl_dt.pack(pady = 10)
main_window_lbl_msg.pack(pady = 10)
main_window_btn_bmi.pack(pady = 10)
main_window_btn_view.pack(pady = 10)
main_window_btn_export.pack(pady = 10)
main_window_lbl_count.pack(pady = 10)

bmi_window = Toplevel(main_window)
bmi_window.title("Calculate")
bmi_window.geometry("600x450+400+5")
bmi_window.configure(background = 'lightskyblue')

bmi_window_lbl_name = Label(bmi_window, text = "Enter name:", font = ('Arial', 15, 'bold'), background = 'gray93')
bmi_window_ent_name = Entry(bmi_window, bd = 5, font = ('Arial', 15, 'bold'))
bmi_window_lbl_age = Label(bmi_window, text = "Enter age:", font = ('Arial', 15, 'bold'), background = 'gray93')
bmi_window_ent_age = Entry(bmi_window, bd = 5, font = ('Arial', 15, 'bold'))
bmi_window_lbl_phone = Label(bmi_window, text = "Enter phone:", font = ('Arial', 15, 'bold'), background = 'gray93')
bmi_window_ent_phone = Entry(bmi_window, bd = 5, font = ('Arial', 15, 'bold'))
bmi_window_lbl_gender = Label(bmi_window, text = "Gender:", font = ('Arial', 15, 'bold'), background = 'gray93')
bmi_window_rb_male = Radiobutton(bmi_window, text = "Male", variable = var, value = 1, font = ('Arial', 15, 'bold'), command = f9)
bmi_window_rb_female = Radiobutton(bmi_window, text = "Female", variable = var, value = 2, font = ('Arial', 15, 'bold'), command = f9)
bmi_window_lbl_ht = Label(bmi_window, text = "Enter height in cm:", font = ('Arial', 15, 'bold'), background = 'gray93')
bmi_window_ent_ht = Entry(bmi_window, bd = 5, font = ('Arial', 15, 'bold'))
bmi_window_btn_convert = Button(bmi_window, text = "Convert", font = ('Arial', 15, 'bold'), width = 10, command = f4)
bmi_window_lbl_wt = Label(bmi_window, text = "Enter weight in kg:", font = ('Arial', 15, 'bold'), background = 'gray93')
bmi_window_ent_wt = Entry(bmi_window, bd = 5, font = ('Arial', 15, 'bold'))
bmi_window_btn_save = Button(bmi_window, text = "Save", font = ('Arial', 15, 'bold'), width = 10, command = f5)
bmi_window_btn_back = Button(bmi_window, text = "Back", font = ('Arial', 15, 'bold'), width = 10, command = f6)

bmi_window_ent_name.focus()
bmi_window_rb_male.select()

bmi_window_lbl_name.place(x=10, y=10)
bmi_window_ent_name.place(x=210, y=10)
bmi_window_lbl_age.place(x=10, y=60)
bmi_window_ent_age.place(x=210, y=60)
bmi_window_lbl_phone.place(x=10, y=110)
bmi_window_ent_phone.place(x=210, y=110)
bmi_window_lbl_gender.place(x=10, y=160)
bmi_window_rb_male.place(x=210, y=160)
bmi_window_rb_female.place(x=410, y=160)
bmi_window_lbl_ht.place(x=10, y=210)
bmi_window_ent_ht.place(x=210, y=210)
bmi_window_btn_convert.place(x=450, y=210)
bmi_window_lbl_wt.place(x=10, y=260)
bmi_window_ent_wt.place(x=210, y=260)
bmi_window_btn_save.place(x=250, y=310)
bmi_window_btn_back.place(x=250, y=360)
bmi_window.withdraw()

convert_window = Toplevel(bmi_window)
convert_window.title("Height converter")
convert_window.geometry("500x550+400+50")
convert_window.configure(background = 'palegreen')

convert_window_lbl_ht = Label(convert_window, text = "Enter your height", font = ('Arial', 20, 'bold'), background = 'gray93')
convert_window_lbl_ft = Label(convert_window, text = "Feet", font = ('Arial', 20, 'bold'), background = 'gray93')
convert_window_ent_ft = Entry(convert_window, bd = 5, font = ('Arial', 20, 'bold'))
convert_window_lbl_inc = Label(convert_window, text = "Inches", font = ('Arial', 20, 'bold'), background = 'gray93')
convert_window_ent_inc = Entry(convert_window, bd = 5, font = ('Arial', 20, 'bold'))
convert_window_btn_convert = Button(convert_window, text = "Convert", font = ('Arial', 20, 'bold'), width = 10, command = f7)
convert_window_btn_back = Button(convert_window, text = "Back", font = ('Arial', 20, 'bold'), width = 10, command = f13)

convert_window_ent_ft.focus()

convert_window_lbl_ht.pack(pady = 10)
convert_window_lbl_ft.pack(pady = 10)
convert_window_ent_ft.pack(pady = 10)
convert_window_lbl_inc.pack(pady = 10)
convert_window_ent_inc.pack(pady = 10)
convert_window_btn_convert.pack(pady = 10)
convert_window_btn_back.pack(pady = 10)

convert_window.withdraw()

view_window = Toplevel(main_window)
view_window.title("View")
view_window.geometry("500x500+400+100")
view_window.configure(background = 'lightskyblue')

view_window_st_data = ScrolledText(view_window, width = 30, height = 10, font = ('Arial', 20, 'bold')) #, background = 'white'
view_window_btn_back = Button(view_window, text = "Back", font = ('Arial', 20, 'bold'), command = f8)
view_window_st_data.pack(pady = 10)
view_window_btn_back.pack(pady = 10)
view_window.withdraw()

main_window.mainloop()