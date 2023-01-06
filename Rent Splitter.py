from tkinter import *

mainWindow = Tk()

# Labels
Label(mainWindow, text = "Renter 1").grid(row = 0, column = 0)
Label(mainWindow, text = "Renter 2").grid(row = 1, column = 0)
Label(mainWindow, text = "Total Rent").grid(row = 2, column = 0)

# Input
person_a_salary = Entry(mainWindow, width = 25, borderwidth = 5)
person_a_salary.grid(row = 0, column = 1)
person_a_rent_label = Label(mainWindow, text = "       -       ")
person_a_rent_label.grid(row = 0, column = 2)
person_b_salary = Entry(mainWindow, width = 25, borderwidth = 5)
person_b_salary.grid(row = 1, column = 1)
person_b_rent_label = Label(mainWindow, text = "       -       ")
person_b_rent_label.grid(row = 1, column = 2)
rent_total = Entry(mainWindow, width = 25, borderwidth = 5)
rent_total.grid(row = 2, column = 1)


def proportionalRentSplit(person_a_salary, person_b_salary, rentTotal):
    
    totalIncome = person_a_salary + person_b_salary

    person_a_proportion = person_a_salary/totalIncome
    person_b_proportion = person_b_salary/totalIncome

    person_a_rent = round((person_a_proportion * rentTotal), 2)
    person_b_rent = round((person_b_proportion * rentTotal), 2)

    person_a_rent_label.configure(text = "Rent Ammount: " + str(person_a_rent))
    person_b_rent_label.configure(text = "Rent Ammount: " + str(person_b_rent))

def on_click():
    proportionalRentSplit(int(person_a_salary.get()), int(person_b_salary.get()), int(rent_total.get()))
    

# Buttons
Button(mainWindow, text = "Submit", command = on_click).grid(row = 3, column= 1)


mainWindow.mainloop()