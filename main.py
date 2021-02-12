from tkinter import Tk, Button
import tkinter as tk

class ToggleButton(tk.Button):

    #List for selected dates
    eDates = []

    #Passthrough for eDates list
    @staticmethod
    def getDates():
        ToggleButton.eDates.sort()
        return ToggleButton.eDates

    #Initilizes ToggleButton instance with 'pressed' boolean
    def __init__(self, master, **kw):
        self.pressed = True
        tk.Button.__init__(self,master,**kw)
        self['command'] = self.tester

    #Allows buttons to have different commands based on title state
    def tester(self):
        if self.pressed:
            self.config(bg="blue")
            self.pressed = False
            ToggleButton.eDates.append(int(self['text']))
        else:
            self.config(bg="red")
            self.pressed = True
            ToggleButton.eDates.remove(int(self['text']))




#Window Setup
root = Tk()
root.title("bruh moment")
root.geometry("500x500")

#Function to print out ToggleButton selected dates
def printDates():
    print(ToggleButton.getDates())

#Puts 31 date ToggleButtons into a list
buttons = []
for i in range(31):
    buttons.append(ToggleButton(root, text=str(i+1), bg= "red"))

#Sets each ToggleButton to respective grid position
C = 0
for y in range(4):
    for x in range(7):
        buttons[C].grid(row=y,column=x)
        C=C+1

#Sets remaining ToggleButtons to last row of date grid
for i in range(C,31):
    buttons[i].grid(row=5)

#List Test Button
buttons.append(Button(root,text='Print List', bg='yellow', command = printDates))
buttons[-1].grid(row=7)

#Runs root
root.mainloop()
