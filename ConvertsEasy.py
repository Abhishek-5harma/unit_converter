# Import modules
from tkinter import *
from tkinter import messagebox


# Method length()
def length():

    # Inches to Centimeters
    def ic():
        l1 = Tk()
        l1.title("Inches to Centimeters")
        l1.resizable(0,0)
        l1.minsize(height="300",width="500")
        l1.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                cm = float(txt2.get())
                res = cm * 0.4
                txt1.delete(0,END)
                txt1.insert(0,res)
            else:
                inc = float(txt1.get())
                res = inc * 2.54
                txt2.delete(0,END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(l1,text="Enter Inches:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(l1,width=40)
        txt1.place(x=180,y=50)

        l1.bind('<Return>',con)

        lbl2 = Label(l1,text="Enter Centimeters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(l1, width=40)
        txt2.place(x=180, y=100)

        btns1 = Button(l1,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(l1, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        l1.mainloop()

    # Foot to Centimeters
    def fc():
        l2 = Tk()
        l2.title("Foot to Centimeters")
        l2.resizable(0,0)
        l2.minsize(height="300",width="500")
        l2.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                cm = float(txt2.get())
                res = float(cm / 30.0)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                foot = float(txt1.get())
                res = float(foot * 30.0)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(l2,text="Enter Foot:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(l2,width=40)
        txt1.place(x=180,y=50)

        l2.bind('<Return>', con)
        
        lbl2 = Label(l2,text="Enter Centimeters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(l2, width=40)
        txt2.place(x=180, y=100)

        btns1 = Button(l2,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(l2, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        l2.mainloop()

    # Yards to Meters
    def ym():
        l3 = Tk()
        l3.title("Yards to Meters")
        l3.resizable(0,0)
        l3.minsize(height="300",width="500")
        l3.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                m = float(txt2.get())
                res = m / 0.91
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                y = float(txt1.get())
                res = y * 0.91
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(l3,text="Enter Yards:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(l3,width=40)
        txt1.place(x=180,y=50)

        l3.bind('<Return>', con)

        lbl2 = Label(l3,text="Enter Meters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(l3, width=40)
        txt2.place(x=180, y=100)

        btns1 = Button(l3,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(l3, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        l3.mainloop()

    # Miles to Kilometers
    def mk():
        l4 = Tk()
        l4.title("Miles to Kilometers")
        l4.resizable(0,0)
        l4.minsize(height="300",width="500")
        l4.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                km = float(txt2.get())
                res = km / 1.6
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                m = float(txt1.get())
                res = m * 1.6
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(l4,text="Enter Miles:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(l4,width=40)
        txt1.place(x=180,y=50)

        l4.bind('<Return>', con)

        lbl2 = Label(l4,text="Enter Kilometers:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(l4, width=40)
        txt2.place(x=180, y=100)

        btns1 = Button(l4,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(l4, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        l4.mainloop()

    # Millimeters to Inches
    def mi():
        l5 = Tk()
        l5.title("Millimeters to Inches")
        l5.resizable(0,0)
        l5.minsize(height="300",width="500")
        l5.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                inc = float(txt2.get())
                res = float(inc / 0.04)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                mm = float(txt1.get())
                res = float(mm * 0.04)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(l5,text="Enter Millimeters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(l5,width=40)
        txt1.place(x=180,y=50)

        l5.bind('<Return>', con)

        lbl2 = Label(l5,text="Enter Inches:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(l5, width=40)
        txt2.place(x=180, y=100)

        btns1 = Button(l5,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(l5, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        l5.mainloop()

    # Meters to Feet
    def mf():
        l6 = Tk()
        l6.title("Meters to Feet")
        l6.resizable(0,0)
        l6.minsize(height="300",width="500")
        l6.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                ft = float(txt2.get())
                res = float(ft / 3.3)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                m = float(txt1.get())
                res = float(m * 3.3)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(l6,text="Enter Meters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(l6,width=40)
        txt1.place(x=180,y=50)

        l6.bind('<Return>', con)

        lbl2 = Label(l6,text="Enter Feet:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(l6, width=40)
        txt2.place(x=180, y=100)

        btns1 = Button(l6,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(l6, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        l6.mainloop()

    # Window form
    len = Tk()
    len.maxsize(height=680, width=1370)
    len.minsize(height=680, width=1370)
    len.title("Field of measurement : Length")
    len.config(bg="Orange")

    # Labels
    lblh1 = Label(len,text = "Length Measurement ",bg="green",fg="white", font=('Arial',20,'bold','italic','underline'))
    lblh1.place(x=550,y=20)

    lblh2 = Label(len,text="Enter type of Conversion: ",bg="green",fg="white",font=('Arial',15,'italic','bold'))
    lblh2.place(x=565,y=100)

    # Buttons
    btn1 = Button(len, text="Inches to Centimeters", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=ic)
    btn1.place(x=610, y=200)

    btn2 = Button(len, text="Foot to Centimeters", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=fc)
    btn2.place(x=430, y=270)

    btn3 = Button(len, text="Yards to Meters", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=ym)
    btn3.place(x=810, y=270)

    btn4 = Button(len, text="Miles to Kilometers", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=mk)
    btn4.place(x=432, y=340)

    btn5 = Button(len, text="Millimeters to Inches", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=mi)
    btn5.place(x=792, y=340)

    btn6 = Button(len, text="Meters to Feet", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=mf)
    btn6.place(x=638, y=410)

    btns3 = Button(len, text="Back to home", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),
                   command=len.destroy)
    btns3.place(x=40, y=40)

    # Label
    lblsub = Label(len,text="copyright @ abhishek sharma",bg="orange",fg="black",font=('Arial',10,'bold','italic','underline'))
    lblsub.place(x=1100,y=600)

    len.mainloop()

# Method area()
def area():

    # Sq. Inches to Sq. Centimeters
    def sic():
        a1 = Tk()
        a1.title("Sq. Inches to Sq. Centimeters")
        a1.resizable(0,0)
        a1.minsize(height="300",width="500")
        a1.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                cm = float(txt2.get())
                res = float(cm * 0.16)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                inc = float(txt1.get())
                res = float(inc * 6.5)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(a1,text="Enter Sq. Inches:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(a1,width=40)
        txt1.place(x=200,y=50)

        a1.bind('<Return>', con)

        lbl2 = Label(a1,text="Enter Sq. Centimeters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(a1, width=40)
        txt2.place(x=200, y=100)

        btns1 = Button(a1,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(a1, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        a1.mainloop()

    # Sq. Feet to Sq. Meters
    def sfm():
        a2 = Tk()
        a2.title("Sq. Feet to Sq. Meters")
        a2.resizable(0,0)
        a2.minsize(height="300",width="500")
        a2.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                m = float(txt2.get())
                res = float(m / 0.09)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                ft = float(txt1.get())
                res = float(ft * 0.09)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(a2,text="Enter Sq. Feet:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(a2,width=40)
        txt1.place(x=200,y=50)

        a2.bind('<Return>', con)

        lbl2 = Label(a2,text="Enter Sq. Meters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(a2, width=40)
        txt2.place(x=200, y=100)

        btns1 = Button(a2,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(a2, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        a2.mainloop()

    # Sq. Yards to Sq. Meters
    def sym():
        a3 = Tk()
        a3.title("Sq. Yards to Sq. Meters")
        a3.resizable(0,0)
        a3.minsize(height="300",width="500")
        a3.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                m = float(txt2.get())
                res = float(m * 1.2)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                y = float(txt1.get())
                res = float(y * 0.8)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(a3,text="Enter Sq. Yards:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(a3,width=40)
        txt1.place(x=200,y=50)

        a3.bind('<Return>', con)

        lbl2 = Label(a3,text="Enter Sq. Meters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(a3, width=40)
        txt2.place(x=200, y=100)

        btns1 = Button(a3,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(a3, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        a3.mainloop()

    # Sq. Miles to Sq. Kilometers
    def smk():
        a4 = Tk()
        a4.title("Sq. Miles to Sq. Kilometers")
        a4.resizable(0,0)
        a4.minsize(height="300",width="500")
        a4.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                km = float(txt2.get())
                res = float(km * 0.4)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                m = float(txt1.get())
                res = float(m * 2.6)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(a4,text="Enter Sq. Miles:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(a4,width=40)
        txt1.place(x=200,y=50)

        a4.bind('<Return>', con)

        lbl2 = Label(a4,text="Enter Sq. Kilometers:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(a4, width=40)
        txt2.place(x=200, y=100)

        btns1 = Button(a4,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(a4, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        a4.mainloop()

    # Hectares to Acres
    def hc():
        a5 = Tk()
        a5.title("Hectares to Acres")
        a5.resizable(0,0)
        a5.minsize(height="300",width="500")
        a5.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                a = float(txt2.get())
                res = float(a / 2.47)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                h = float(txt1.get())
                res = float(h * 2.47)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(a5,text="Enter Hectares:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(a5,width=40)
        txt1.place(x=200,y=50)

        a5.bind('<Return>', con)

        lbl2 = Label(a5,text="Enter Acres:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(a5, width=40)
        txt2.place(x=200, y=100)

        btns1 = Button(a5,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(a5, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        a5.mainloop()

    # Window form
    ar = Tk()
    ar.maxsize(height=680, width=1370)
    ar.minsize(height=680, width=1370)
    ar.title("Field of measurement : Area")
    ar.config(bg="Orange")

    lblh1 = Label(ar, text="Area  Measurement", bg="green", fg="white",
                  font=('Arial', 20, 'bold', 'italic', 'underline'))
    lblh1.place(x=565, y=20)

    lblh2 = Label(ar, text="Enter type of Conversion: ", bg="green", fg="white", font=('Arial', 15, 'italic', 'bold'))
    lblh2.place(x=565, y=80)

    btn1 = Button(ar, text="Sq. Inches to Sq. Centimeters", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=sic)
    btn1.place(x=580, y=180)

    btn2 = Button(ar, text="Sq. Feet to Sq. Meters", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=sfm)
    btn2.place(x=807, y=250)

    btn3 = Button(ar, text="Sq. Yards to Sq. Meters", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=sym)
    btn3.place(x=403, y=250)

    btn4 = Button(ar, text="Sq. Miles to Sq. Kilometers", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=smk)
    btn4.place(x=790, y=320)

    btn5 = Button(ar, text="Hectares to Acre", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=hc)
    btn5.place(x=430, y=320)

    btns3 = Button(ar, text="Back to home", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),
                   command=ar.destroy)
    btns3.place(x=40, y=40)

    lblsub = Label(ar, text="copyright @ abhishek sharma", bg="orange", fg="black",
                   font=('Arial', 10, 'bold', 'italic', 'underline'))
    lblsub.place(x=1100, y=600)

    ar.mainloop()

# Method mass()
def mass():

    # Ounces to Grams
    def og():
        m1 = Tk()
        m1.title("Ounces to Grams")
        m1.resizable(0,0)
        m1.minsize(height="300",width="500")
        m1.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                g = float(txt2.get())
                res = float(g * 0.035)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                o = float(txt1.get())
                res = float(o * 28)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(m1,text="Enter Ounces:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(m1,width=40)
        txt1.place(x=180,y=50)

        m1.bind('<Return>', con)

        lbl2 = Label(m1,text="Enter Grams:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(m1, width=40)
        txt2.place(x=180, y=100)

        btns1 = Button(m1,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(m1, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        m1.mainloop()

    # Pounds to Kilograms
    def pk():
        m2 = Tk()
        m2.title("Pounds to Kilograms")
        m2.resizable(0,0)
        m2.minsize(height="300",width="500")
        m2.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                kg = float(txt2.get())
                res = float(kg * 2.2)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                p = float(txt1.get())
                res = float(p * 0.45)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(m2,text="Enter Pounds:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(m2,width=40)
        txt1.place(x=180,y=50)

        m2.bind('<Return>', con)

        lbl2 = Label(m2,text="Enter Kilograms:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(m2, width=40)
        txt2.place(x=180, y=100)

        btns1 = Button(m2,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(m2, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        m2.mainloop()

    # Short Ton to Metric Ton
    def sm():
        m3 = Tk()
        m3.title("Short Ton to Metric Ton")
        m3.resizable(0,0)
        m3.minsize(height="300",width="500")
        m3.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                mt = float(txt2.get())
                res =  float(mt * 1.1)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                st = float(txt1.get())
                res = float(st * 0.9)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(m3,text="Enter Short Ton:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(m3,width=40)
        txt1.place(x=180,y=50)

        m3.bind('<Return>', con)

        lbl2 = Label(m3,text="Enter Metric Ton:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(m3, width=40)
        txt2.place(x=180, y=100)

        btns1 = Button(m3,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(m3, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        m3.mainloop()

    # Window form
    ma = Tk()
    ma.maxsize(height=680, width=1370)
    ma.minsize(height=680, width=1370)
    ma.title("Field of measurement : Mass")
    ma.config(bg="Orange")

    # Labels
    lblh1 = Label(ma, text="Mass/Weight Measurement", bg="green", fg="white",
                  font=('Arial', 20, 'bold', 'italic', 'underline'))
    lblh1.place(x=520, y=20)

    lblh2 = Label(ma, text="Enter type of Conversion: ", bg="green", fg="white", font=('Arial', 15, 'italic', 'bold'))
    lblh2.place(x=565, y=80)

    # Buttons
    btn1 = Button(ma, text="Ounces to Grams", bg="yellow", fg="red",font=('Arial', 12, 'italic', 'underline'),command=og)
    btn1.place(x=625, y=180)

    btn2 = Button(ma, text="Pounds to Kilograms", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=pk)
    btn2.place(x=414, y=260)

    btn3 = Button(ma, text="Short Ton to Metric Ton", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=sm)
    btn3.place(x=805, y=260)

    btns3 = Button(ma, text="Back to home", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),
                   command=ma.destroy)
    btns3.place(x=40, y=40)

    # Labels
    lblsub = Label(ma, text="copyright @ abhishek sharma", bg="orange", fg="black",
                   font=('Arial', 10, 'bold', 'italic', 'underline'))
    lblsub.place(x=1100, y=600)

    ma.mainloop()

# Method volume()
def volume():

    # Teaspoons to Milliliters
    def tm1():
        v1 = Tk()
        v1.title("Teaspoons to Milliliters")
        v1.resizable(0,0)
        v1.minsize(height="300",width="500")
        v1.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                ml = float(txt2.get())
                res = float(ml / 5)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                ts = float(txt1.get())
                res = float(ts * 5)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(v1,text="Enter Teaspoons:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(v1,width=40)
        txt1.place(x=200,y=50)

        v1.bind('<Return>', con)

        lbl2 = Label(v1,text="Enter Milliliters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(v1, width=40)
        txt2.place(x=200, y=100)

        btns1 = Button(v1,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(v1, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        v1.mainloop()

    # Tablespoons to Milliliters
    def tm2():
        v2 = Tk()
        v2.title("Tablespoons to Milliliters")
        v2.resizable(0,0)
        v2.minsize(height="300",width="500")
        v2.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                ml = float(txt2.get())
                res = float(ml / 15)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                ts = float(txt1.get())
                res = float(ts * 15)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(v2,text="Enter Tablespoons:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(v2,width=40)
        txt1.place(x=200,y=50)

        v2.bind('<Return>', con)

        lbl2 = Label(v2,text="Enter Milliliters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(v2, width=40)
        txt2.place(x=200, y=100)

        btns1 = Button(v2,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(v2, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        v2.mainloop()

    # Fluid Ounces to Milliliters
    def fom():
        v3 = Tk()
        v3.title("Fluid Ounces to Milliliters")
        v3.resizable(0,0)
        v3.minsize(height="300",width="500")
        v3.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                ml = float(txt2.get())
                res = float(ml / 30)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                fo = float(txt1.get())
                res = float(fo * 30)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(v3,text="Enter Fluid Ounces:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(v3,width=40)
        txt1.place(x=200,y=50)

        v3.bind('<Return>', con)

        lbl2 = Label(v3,text="Enter Milliliters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(v3, width=40)
        txt2.place(x=200, y=100)

        btns1 = Button(v3,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(v3, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        v3.mainloop()

    # Cups to Liters
    def cl():
        v4 = Tk()
        v4.title("Cups to Liters")
        v4.resizable(0,0)
        v4.minsize(height="300",width="500")
        v4.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                l = float(txt2.get())
                res = float(l / 0.24)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                c = float(txt1.get())
                res = float(c * 0.24)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(v4,text="Enter Cups:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(v4,width=40)
        txt1.place(x=200,y=50)

        v4.bind('<Return>', con)

        lbl2 = Label(v4,text="Enter Liters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(v4, width=40)
        txt2.place(x=200, y=100)

        btns1 = Button(v4,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(v4, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        v4.mainloop()

    # Pints to Liters
    def pl():
        v5 = Tk()
        v5.title("Pints to Liters")
        v5.resizable(0,0)
        v5.minsize(height="300",width="500")
        v5.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                l = float(txt2.get())
                res = float(l / 0.47)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                p = float(txt1.get())
                res = float(p * 0.47)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(v5,text="Enter Pints:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(v5,width=40)
        txt1.place(x=200,y=50)

        v5.bind('<Return>', con)

        lbl2 = Label(v5,text="Enter Liters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(v5, width=40)
        txt2.place(x=200, y=100)

        btns1 = Button(v5,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(v5, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        v5.mainloop()

    # Quarts to Liters
    def ql():
        v6 = Tk()
        v6.title("Quarts to Liters")
        v6.resizable(0,0)
        v6.minsize(height="300",width="500")
        v6.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                l = float(txt2.get())
                res = float(l / 0.95)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                q = float(txt1.get())
                res = float(q * 0.95)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(v6,text="Enter Quarts:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(v6,width=40)
        txt1.place(x=200,y=50)

        v6.bind('<Return>', con)

        lbl2 = Label(v6,text="Enter Liters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(v6, width=40)
        txt2.place(x=200, y=100)

        btns1 = Button(v6,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(v6, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        v6.mainloop()

    # Gallons to Liters
    def gl():
        v7 = Tk()
        v7.title("Gallons to Liters")
        v7.resizable(0,0)
        v7.minsize(height="300",width="500")
        v7.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                l = float(txt2.get())
                res = float(l / 3.8)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                g = float(txt1.get())
                res = float(g * 3.8)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(v7,text="Enter Gallons:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(v7,width=40)
        txt1.place(x=200,y=50)

        v7.bind('<Return>', con)

        lbl2 = Label(v7,text="Enter Liters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(v7, width=40)
        txt2.place(x=200, y=100)

        btns1 = Button(v7,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(v7, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        v7.mainloop()

    # Cubic Feet to Cubic Meters
    def cfcm():
        v8 = Tk()
        v8.title("Cubic Feet to Cubic Meters")
        v8.resizable(0,0)
        v8.minsize(height="300",width="500")
        v8.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                cm = float(txt2.get())
                res = float(cm / 0.03)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                cf = float(txt1.get())
                res = float(cf * 0.03)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(v8,text="Enter Cubic Feet:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(v8,width=40)
        txt1.place(x=200,y=50)

        v8.bind('<Return>', con)

        lbl2 = Label(v8,text="Enter Cubic Meters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(v8, width=40)
        txt2.place(x=200, y=100)

        btns1 = Button(v8,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(v8, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        v8.mainloop()

    # Cubic Yards to Cubic Meters
    def cycm():
        v9 = Tk()
        v9.title("Cubic Yards to Cubic Meters")
        v9.resizable(0,0)
        v9.minsize(height="300",width="500")
        v9.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                cm = float(txt2.get())
                res = float(cm / 0.76)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                cy = float(txt1.get())
                res = float(cy * 0.76)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(v9,text="Enter Cubic Yards:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(v9,width=40)
        txt1.place(x=200,y=50)

        v9.bind('<Return>', con)

        lbl2 = Label(v9,text="Enter Cubic Meters:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(v9, width=40)
        txt2.place(x=200, y=100)

        btns1 = Button(v9,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(v9, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        v9.mainloop()

    # Window form
    vol = Tk()
    vol.maxsize(height=680, width=1370)
    vol.minsize(height=680, width=1370)
    vol.title("Field of measurement : Volume")
    vol.config(bg="Orange")

    # Labels
    lblh1 = Label(vol, text="Volume Measurement", bg="green", fg="white",
                  font=('Arial', 20, 'bold', 'italic', 'underline'))
    lblh1.place(x=550, y=20)

    lblh2 = Label(vol, text="Enter type of Conversion: ", bg="green", fg="white", font=('Arial', 15, 'italic', 'bold'))
    lblh2.place(x=565, y=80)

    # Buttons
    btn1 = Button(vol, text="Teaspoons to Milliliters", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=tm1)
    btn1.place(x=600, y=160)

    btn2 = Button(vol, text="Tablespoons to Milliliters", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=tm2)
    btn2.place(x=400, y=220)

    btn3 = Button(vol, text="Fluid Ounces to Milliliters", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=fom)
    btn3.place(x=790, y=220)

    btn4 = Button(vol, text="Cups to Liters", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=cl)
    btn4.place(x=440, y=280)

    btn5 = Button(vol, text="Pints to Liters", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=pl)
    btn5.place(x=830, y=280)

    btn6 = Button(vol, text="Quarts to Liters", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=ql)
    btn6.place(x=435, y=340)

    btn7 = Button(vol, text="Gallons to Liters", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=gl)
    btn7.place(x=820, y=340)

    btn8 = Button(vol, text="Cubic Feet to Cubic Meters", bg="yellow", fg="red", font=('Arial', 12, 'italic', 'underline'),command=cfcm)
    btn8.place(x=390, y=400)

    btn9 = Button(vol, text="Cubic Yards to Cubic Meters", bg="yellow", fg="red",font=('Arial', 12, 'italic', 'underline'),command=cycm)
    btn9.place(x=780, y=400)

    btns3 = Button(vol, text="Back to home", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),
                   command=vol.destroy)
    btns3.place(x=40, y=40)

    lblsub = Label(vol, text="copyright @ abhishek sharma", bg="orange", fg="black",
                   font=('Arial', 10, 'bold', 'italic', 'underline'))
    lblsub.place(x=1100, y=600)

    vol.mainloop()

# Method temp()
def temp():

    # Fahrenheit to Celsius
    def fc():
        t1 = Tk()
        t1.title("Fahrenheit to Celsius")
        t1.resizable(0,0)
        t1.minsize(height="300",width="500")
        t1.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                c = float(txt2.get())
                res = float(c * 9/5 + 32)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                f = float(txt1.get())
                res = float((f - 32) * 5/9)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        lbl1 = Label(t1,text="Enter Fahrenheit:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(t1,width=40)
        txt1.place(x=180,y=50)

        t1.bind('<Return>', con)

        lbl2 = Label(t1,text="Enter Celsius:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(t1, width=40)
        txt2.place(x=180, y=100)

        btns1 = Button(t1,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(t1, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        t1.mainloop()

    # Kelvin to Celsius
    def kc():
        t2 = Tk()
        t2.title("Kelvin to Celsius")
        t2.resizable(0,0)
        t2.minsize(height="300",width="500")
        t2.config(bg="orange")

        def con(event=None):
            if txt1.get()=="" and txt2.get()=="":
                messagebox.showerror("Error","Enter data in any one space!")
            elif txt1.get()=="":
                c = float(txt2.get())
                res = float(c + 273.15)
                txt1.delete(0, END)
                txt1.insert(0,res)
            else:
                k = float(txt1.get())
                res = float(k - 273.15)
                txt2.delete(0, END)
                txt2.insert(0,res)

        def clear():
            txt1.delete(0,END)
            txt2.delete(0,END)

        # Labels
        lbl1 = Label(t2,text="Enter Kelvin:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl1.place(x=20,y=50)
        txt1 = Entry(t2,width=40)
        txt1.place(x=180,y=50)

        t2.bind('<Return>', con)

        lbl2 = Label(t2,text="Enter Celsius:",bg="orange",fg="black",font=('Arial',12,'bold'))
        lbl2.place(x=20,y=100)
        txt2 = Entry(t2, width=40)
        txt2.place(x=180, y=100)

        # Buttons
        btns1 = Button(t2,text="Convert",bg="green",fg="white",font=('Arial',12,'bold','underline','italic'),command=con)
        btns1.place(x=200,y=150)

        btns2 = Button(t2, text="Clear", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),command=clear)
        btns2.place(x=300, y=150)

        t2.mainloop()

    # Window form
    tem = Tk()
    tem.maxsize(height=680, width=1370)
    tem.minsize(height=680, width=1370)
    tem.title("Field of measurement : Temperature")
    tem.config(bg="Orange")

    # Labels
    lblh1 = Label(tem, text="Temperature Measurement", bg="green", fg="white",
                  font=('Arial', 20, 'bold', 'italic', 'underline'))
    lblh1.place(x=515, y=20)

    lblh2 = Label(tem, text="Enter type of Conversion: ", bg="green", fg="white", font=('Arial', 15, 'italic', 'bold'))
    lblh2.place(x=565, y=80)

    # Buttons
    btn1 = Button(tem,text="Fahrenheit to Celcius", bg="yellow", fg="red", font=('Arial',12,'underline','italic'),command=fc)
    btn1.place(x=610,y=180)

    btn2 = Button(tem, text="Kelvin to Celcius", bg="yellow", fg="red", font=('Arial', 12, 'underline', 'italic'),command=kc)
    btn2.place(x=627, y=240)

    btns3 = Button(tem, text="Back to home", bg="green", fg="white", font=('Arial', 12, 'bold', 'underline', 'italic'),
                   command=tem.destroy)
    btns3.place(x=40, y=40)

    lblsub = Label(tem, text="copyright @ abhishek sharma", bg="orange", fg="black",
                   font=('Arial', 10, 'bold', 'italic', 'underline'))
    lblsub.place(x=1100, y=600)

    tem.mainloop()

# Home Page
def home():

    # Window form
    root = Tk()
    root.maxsize(height=680, width=1370)
    root.minsize(height=680, width=1370)
    root.title("Easy Converter")
    root.config(bg="Orange")

    # Labels
    lblHead = Label(root, text=" Converts Easy  ", bg="green", fg="powder blue",
                    font=('Algerian', 20, 'italic', 'bold', 'underline'))
    lblHead.place(x=550, y=20)

    lblhead1 = Label(root, text=" Enter Your Field of Measurement: ", bg="green", fg="powder blue",
                     font=('Arial', 15, 'bold'))
    lblhead1.place(x=510, y=100)

    # Buttons
    btn1 = Button(root, text="Length", bg="yellow", fg="red", font=('Arial', 12, 'bold', 'underline'), command=length)
    btn1.place(x=640, y=180)

    btn2 = Button(root, text="Area", bg="yellow", fg="red", font=('Arial', 12, 'bold', 'underline'), command=area)
    btn2.place(x=650, y=240)

    btn3 = Button(root, text="Mass/Weight", bg="yellow", fg="red", font=('Arial', 12, 'bold', 'underline'),
                  command=mass)
    btn3.place(x=620, y=300)

    btn4 = Button(root, text="Volume", bg="yellow", fg="red", font=('Arial', 12, 'bold', 'underline'), command=volume)
    btn4.place(x=640, y=360)

    btn5 = Button(root, text="Temperature", bg="yellow", fg="red", font=('Arial', 12, 'bold', 'underline'),
                  command=temp)
    btn5.place(x=620, y=420)

    lblsub = Label(root, text="copyright @ abhishek sharma", bg="orange", fg="black",
                   font=('Arial', 10, 'bold', 'italic', 'underline'))
    lblsub.place(x=1100, y=600)

    root.mainloop()

home()