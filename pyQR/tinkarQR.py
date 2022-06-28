from tkinter import *
import qrcode
from PIL import Image , ImageTk
from resizeimage import resizeimage

class Qr_generator:
    def __init__(self ,root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("Qr generator devlop by sanskar")
        self.root.resizable(False ,False)

        title = Label(self.root , text = "  Qr code Generator" ,font = ("times new roman", 40) , bg= '#053246', fg='lightyellow' , anchor='w').place(x=0 , y=0, relwidth =1)

        #employ details window
        # variables
        self.var_emp_code= StringVar()
        self.var_name= StringVar()
        self.var_department= StringVar()
        self.var_designatin= StringVar()
        emp_frame = Frame(self.root ,bd=2 , relief=RIDGE ,bg = 'white')
        emp_frame.place(x=50 ,y=100 ,width=500 , height= 380)
        emp_title = Label(emp_frame , text = " Employee details" ,font = ("goudy old style", 20) , bg= '#043246', fg='white').place(x=0 , y=0, relwidth =1)



        lbl_ID = Label(emp_frame , text = "Employee ID " ,font = ("times new roman", 15 , 'bold') , bg= 'white').place(x=20 , y=60)
        lbl_name = Label(emp_frame , text = "Name " ,font = ("times new roman", 15 , 'bold') , bg= 'white').place(x=20 , y=100)
        lbl_department = Label(emp_frame , text = "Department " ,font = ("times new roman", 15 , 'bold') , bg= 'white').place(x=20 , y=140)
        lbl_designation = Label(emp_frame , text = "Designation " ,font = ("times new roman", 15 , 'bold') , bg= 'white').place(x=20 , y=180)

        txt_ID = Entry(emp_frame ,font = ("times new roman", 15 ), textvariable=self.var_emp_code , bg= 'lightyellow').place(x=200 , y=60)
        txt_name = Entry(emp_frame  ,font = ("times new roman", 15 ),textvariable=self.var_name , bg= 'lightyellow').place(x=200 , y=100)
        txt_department = Entry(emp_frame ,font = ("times new roman", 15 ),textvariable=self.var_department , bg= 'lightyellow').place(x=200 , y=140)
        txt_designation = Entry(emp_frame ,font = ("times new roman", 15),textvariable=self.var_designatin , bg= 'lightyellow').place(x=200 , y=180)

        btn_generator = Button(emp_frame, text="Qr generate" ,command= self.generate , font=("times new roman" , 18, "bold"), bg="#2196f3" ,fg = 'white').place(x = 70, y = 250 ,width=160 , height=40)

        clean_generator = Button(emp_frame, text="clear" , command=self.clear,font=("times new roman" , 18, "bold"), bg="#607d8b" ,fg = 'white').place(x = 260, y = 250 ,width=140 , height=40)
        self.msg = " "
        self.lbl_msg= Label(emp_frame , text = self.msg ,font = ("times new roman", 20 , ) ,bg="white" , fg= 'green')
        self.lbl_msg.place(x=0 , y=300 , relwidth=1)

        #employ details window
        qr_frame = Frame(self.root ,bd=2 , relief=RIDGE ,bg = 'white')
        qr_frame.place(x=600 ,y=100 ,width=250 , height= 380)
        qr_title = Label(qr_frame , text = "Enployee QR Code" ,font = ("goudy old style", 20) , bg= '#043246', fg='white').place(x=0 , y=0, relwidth =1)

        self.qr_code = Label(qr_frame , text= "No \n Qr Available" , font=('times new roman' , 15) , bg ='#3f51b5' , fg= 'white' ,bd=1 , relief=RIDGE)
        self.qr_code.place(x =35 ,y= 100 , width=180 , height= 180)


    def generate(self):
        if self.var_emp_code.get()== ''or self.var_name.get() ==''or self.var_department.get() =='' or self.var_designatin.get()=='' :
            self.msg ='All fields are Requred !!!'
            self.lbl_msg.config(text= self.msg , fg='red')
        else:

            qr_data =(f"Employee ID: {self.var_emp_code.get()} \n Employee Name: {self.var_name.get()} \n Employee Department: {self.var_department.get()} \n Employee designation: {self.var_designatin.get()}")
            qr_code = qrcode.make(qr_data)
            # print(qr_code)
            qr_code = resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("qr.py"+ str(self.var_emp_code.get()) + '.png' )
            # QR code image update
            self.im =ImageTk.PhotoImage(file = "qr.py"+ str(self.var_emp_code.get()) + '.png' )
            self.qr_code.config(image = self.im)
   

                     # update notification
            self.msg = "QR code generated successfully!!!"
            self.lbl_msg.config(text= self.msg , fg='red')
           

    def clear(self):
        self.var_emp_code .set('')
        self.var_name .set('')
        self.var_department .set('')
        self.var_designatin .set('')
        self.msg=''
        self.lbl_msg.config(text= self.msg)
        self.qr_code.config(image='')
        


        
        
root  = Tk()
obj = Qr_generator(root)
root.mainloop()