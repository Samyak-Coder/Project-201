from tkinter import *
window=Tk()
# add widgets here


window.title('Simple Interest Calculator')
window.geometry("700x400")
window.configure(bg='grey')
   
def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i, 2)

    
    result.destroy()
    
    message=Label(resultFrame,text="Interest on Rs."+str(p)+" at rate of interest "+str(r)+"% for "+str(t)+" years is Rs."+str(interest), bg = "grey", font=("Calibri", 12), width=55)
    message.place(x=20,y=40)
    message.pack()

appLabel=Label(window, text="SIMPLE INTEREST CALCULATOR", fg = "black", bg = "grey", font=("Calibri", 20),bd=5)
appLabel.place(x=20, y=20)

principleLabel=Label(window, text="Principle in Rs", fg = "black", bg = "grey", font=("Calibri", 12),bd=1)
principleLabel.place(x=50, y=92)

principle=Entry(window, text="", bd=2, width=22)
principle.place(x=200, y=92)

rateLabel=Label(window, text="Rate of Interest in %", fg = "black", bg = "grey", font=("Calibri", 12))
rateLabel.place(x=50, y=140)

rate=Entry(window, text="", bd=2, width=15)
rate.place(x=200, y=142)

timeLabel=Label(window, text="Time in Yrs", fg = "black", bg = "grey", font=("Calibri", 12))
timeLabel.place(x=50, y=185)

time=Entry(window, text="", bd=2, width=15)
time.place(x=200, y=187)

calculate_button=Button(window,text="CALCULATE",fg = "black", bg = "grey",bd=4,command=calculate_interest)
calculate_button.place(x=50,y=250)

resultFrame = LabelFrame(window,text="Result", bg = "grey", font=("Calibri", 12), )
resultFrame.pack(padx=20, pady=20)
resultFrame.place(x=20,y=300)

result=Label(resultFrame,text="Your result will be displayed here", bg = "grey", font=("Calibri", 12), width=80)
result.place(x=20,y=20)
result.pack()

window.mainloop()