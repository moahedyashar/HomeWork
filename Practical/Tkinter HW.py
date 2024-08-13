

from tkinter import *
root = Tk()
e = Entry(root,width=20,fg="grey")
e.pack()
e.insert(0,"2nd semester's H_Ws ")
def myclick():
    myLabel1 = Label(root,text = "1:practice  all the python functions ")
    myLabel1.pack()
def myclick2():
    myLabel2 = Label(root,text = "2:write a program to calculate the factorial")
    myLabel2.pack()
def myclick3():
    myLabel3 = Label(root,text = "3:write a program to calculate the Fibonacci sequence")
    myLabel3.pack()
def myclick4():
    myLabel4 = Label(root,text = "4:write a graphic program that shows your homeworks's lists")
    myLabel4.pack()



myButton1 = Button(root, text = "first HW", command = myclick, fg = "green",padx=20,pady=20,bg="silver")
myButton1.pack()
myButton2 = Button(root, text = "2nd HW", command = myclick2, fg = "green",padx=20,pady=20,bg="silver")
myButton2.pack()
myButton3 = Button(root, text = "3rd HW", command = myclick3, fg = "green",padx=20,pady=20,bg="silver")
myButton3.pack()
myButton4 = Button(root, text = "4th HW", command = myclick4, fg = "green",padx=20,pady=20,bg="silver")
myButton4.pack()

mainloop()


