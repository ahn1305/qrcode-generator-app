# Importing necessary packages 
import qrcode
import tkinter as tk 
from pathlib import Path
from tkinter import ttk
import os
from tkinter import *
from tkinter import messagebox, filedialog 

#------------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.title('QRCode Generator')
root.resizable(0,0)

#------------------------------------------------------------------------------------------------------------

#function
def gen_qrcode():
	result_qr_name = name.get()
	result_qr_link = link.get()

	dirs = os.listdir("saved_qrcode")
	for file in dirs:
		global files
		files = file.replace('.png', '')

	if files == name.get():
		tk.messagebox.showerror("Error","File with the same name already exists")	
	elif len(result_qr_name) == 0:
		tk.messagebox.showerror("Warning","Enter a name for the qrcode")
	elif len(result_qr_link) == 0:
		tk.messagebox.showerror("Warning","Enter a link or text")

	else:
		qr = qrcode.QRCode(version = 1 , box_size=15 , border=5)
		data =  result_qr_link
		qr.add_data(data)
		qr.make (fit = True)
		img = qr.make_image(fill = 'black' , back_color= 'white')
		location = "saved_qrcode/"+result_qr_name+".png"
		img.save(location)
		tk.messagebox.showinfo("Information","Qrcode generated successfully and stored in {}".format(location))

#------------------------------------------------------------------------------------------------------------


#Vars
name = StringVar()
link = StringVar()


#Labels
qr_name = Label(root,text="Enter a name for the qrcode :",bg="#E8D579")
qr_name.grid(row=1,column=0,pady=5,padx=5)

qr_link = Label(root,text="Enter the link:",bg="#E8D579")
qr_link.grid(row=2,column=0,pady=5,padx=5)

#entry
name_entry_box = Entry(root, textvariable = name, exportselection = 2, width = 50 , bg = "lightgreen")
name_entry_box.grid(row=1,column=1,pady=5,padx=5)

link_entry_box = Entry(root, textvariable = link, exportselection = 2, width = 50 , bg = "lightgreen")
link_entry_box.grid(row=2,column=1,pady=5,padx=5)

#Button
qr_gen_btn = Button(root, text="Generate",command=gen_qrcode,width=20,bg="#05E8E0")
qr_gen_btn.grid(row=3,column=0,pady=3,padx=3) 

#------------------------------------------------------------------------------------------------------------

root.mainloop()




