from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Resposnse Accepted")

#Heading
Label(root, text="Python Registeration Form", font="arial 15 bold underline").grid(row=0, column=3)

#Field Name
name=Label(root, text="Full Name")
phone=Label(root, text="Contact No.")
gender=Label(root, text="Gender")
college=Label(root, text="College")
enroll=Label(root, text="Enrollment No.")

#Packing Fields
name.grid(row=1 ,column=2)
phone.grid(row=2 ,column=2)
gender.grid(row=3 ,column=2)
college.grid(row=4 ,column=2)
enroll.grid(row=5 ,column=2)

#Variables for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
collegevalue = StringVar
enrollvalue = StringVar
checkvalue = IntVar

#Creating entry field
nameenrty = Entry(root, textvariable=namevalue)
phoneenrty = Entry(root, textvariable=phonevalue)
genderenrty = Entry(root, textvariable=gendervalue)
collegeenrty = Entry(root, textvariable=collegevalue)
enrollenrty = Entry(root, textvariable=enrollvalue)

#Packing entry field
nameenrty.grid(row=1, column=3)
phoneenrty.grid(row=2, column=3)
genderenrty.grid(row=3, column=3)
collegeenrty.grid(row=4, column=3)
enrollenrty.grid(row=5, column=3)
checkbutton = Checkbutton(text = "Remember Me?", variable=checkvalue)
checkbutton.grid(row=6, column=3)

#Submit Button
Button(text = "SUBMIT", command=getvals).grid(row=7, column=3)

root.mainloop()