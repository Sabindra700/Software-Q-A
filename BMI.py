#import module
from tkinter import *

#create a window
top = Tk()

#top window title and dimension
top.title("BMI Calculator")
top.geometry('300x200')

#adding a label to window
lbl = Label(top, text = "Height:\n  Feet            Inches")
lbl.grid()

#adding Entry field for feet
Feet = Entry(top, width = 10)
Feet.grid(column = 0, row = 1)

#adding Entry field for inches
Inch = Entry(top, width = 10)
Inch.grid(column = 1, row = 1)

lbl = Label(top, text = "Weight:\n Pound")
lbl.grid()

#adding Entry field for pound
Pound = Entry(top, width = 10)
Pound.grid(column = 0, row = 3)
lbl.grid()

# function to get weight in metric form
def metric_pound():
  get_weight = int(Pound.get())
  weight_kg = get_weight * 0.45
  return weight_kg

#function to get height in metric form
def met_height():
  get_feet = int(Feet.get())
  height_inch = get_feet * 12
  get_inches = int(Inch.get())
  Total_height = height_inch + get_inches
  height_meter = Total_height * 0.025
  height_m2 = height_meter * height_meter
  return height_m2

#function to calculate bmi
def cal_bmi():
 bmi_weight = metric_pound()
 bmi_height = met_height()
 bmi = bmi_weight / bmi_height
  
 if (bmi < 18.5):
    print(bmi, "Underweight")
 elif ( bmi >= 18.5 and bmi< 24.9):
    print(bmi, "Normal Weight")
 elif ( bmi >= 24.9 and bmi < 30):
    print(bmi, "Overweight")
 elif ( bmi >=30):
    print(bmi, "Suffering from Obesity")
   
 lbl.configure(text = bmi)
 lbl.grid(column = 0, row = 10)

#button to calcuate BMI
btn = Button(top, text = "Calculate", fg = "green", command = cal_bmi)
btn.grid(column=0, row=6)

#execute Tkinter
top.mainloop()
