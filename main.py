from tkinter import Tk, Button, Frame, Grid
import tkinter as tk

class ToggleButton(tk.Button):

    #List for selected dates
    eDates = [] 

    #Passthrough for eDates list
    @staticmethod
    def getDates():
        return ToggleButton.eDates

    #Initilizes ToggleButton instance with 'pressed' boolean
    def __init__(self, master, **kw):
        self.pressed = True
        tk.Button.__init__(self,master,**kw)
        self['command'] = self.tester
        

    #Allows buttons to have different commands based on title state
    def tester(self):
        if self.pressed:
            self.config(bg="pink")
            self.pressed = False
            ToggleButton.eDates.append(self['text'])
        else:
            self.config(bg="#FFFDD0")
            self.pressed = True
            ToggleButton.eDates.remove(self['text'])




#Window Setup
root = Tk()
root.title("SWOUSE")
root.geometry("909x750")

#Function to print out ToggleButton selected dates
def printDates():
    print(ToggleButton.getDates())

#Puts 31 date ToggleButtons into a list
buttons = []
for i in range(31):
    buttons.append(ToggleButton(root, text=str(i+1), bg= "#FFFDD0", width = 15, height = 5))

#Sets each ToggleButton to respective grid position
C = 0
for y in range(4):
    for x in range(7):
        buttons[C].grid(row=y,column=x)
        C=C+1
        
#Sets remaining ToggleButtons to last row of date grid
for i in range(3):
    buttons[C].grid(row=4,column=i)
    C=C+1

#List Test Button
buttons.append(Button(root,text='Print List', bg='yellow', command = printDates))
buttons[-1].grid(row=7)

#Runs root
root.mainloop()
