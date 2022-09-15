from tkinter import StringVar, Tk, Button, Frame, messagebox, OptionMenu
import tkinter as tk
from ics import Calendar, Event
from datetime import date

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
            self.config(bg="pink")
            self.pressed = False
            ToggleButton.eDates.append(self['text'])
        else:
            self.config(bg="#FFFDD0")
            self.pressed = True
            ToggleButton.eDates.remove(self['text'])


#test

#Window Setup
root = Tk()
root.title("Recursive Event Creator")
eventsList = []

def eventClick():
    eventDatesPass = ToggleButton.getDates().copy()
    createCalender(eventDatesPass)

def createCalendar(fixedEventDates):
    #Iniltilizes Calendar
    eCalendar = Calendar()

    #Change event days to 00 format

    for i in range(len(fixedEventDates)):
        if len(fixedEventDates[i]) == 1:
            fixedEventDates[i] = '0'+fixedEventDates[i]

    #Change event months to 00 format

    monthNum = str(monthOptions.index(monthVar.get())+1)
    if len(monthNum) == 1:
        monthNum = '0'+monthNum
    
    #Give current year for events
    today = date.today()
    temptime = today.strftime("%Y-")

    #Add dates to list
    for i in range(len(fixedEventDates)):
        try:
            eventsList.append(Event(name=eventName.get(), begin= temptime+monthNum+"-"+fixedEventDates[i]+" 00:00:00"))
        except ValueError:
            tk.messagebox.showwarning(title='Incorrect dates for month', message='Selected dates are out of the selected month\'s range')

    #Write dates to calendar
    for i in eventsList:
        eCalendar.events.add(i)

    #Write calendar to ics file
    open('Event Calendar.ics', 'w+').writelines(eCalendar)


#Puts 31 date ToggleButtons into a list
buttons = []
for i in range(31):
    buttons.append(ToggleButton(root, text=str(i+1), bg= "#FFFDD0", width = 20, height = 6))

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

#Directions with a popup
def directions():
    tk.messagebox.showinfo(title='Directions', message='This program allows the user to create a schedule of a reoccuring task on their calendar and download a caldender file (ics file)\n\n1. Click on the month you want to put your task\n\n2. Select however many days on the month by clicking on the corresponding squares\n\n3. Type in your task at the bottom\n\n4. Click the yellow button that states "Create Event"\n\n5. Find the ics file in the same directory as the program')

#Month Dropdown Selection

monthOptions = ['January','Feburary','March','April','May','June','July','August','September','October','November','December']
monthVar = StringVar(root)
monthVar.set(monthOptions[0])
monthDropdown = OptionMenu(root, monthVar, *monthOptions)
monthDropdown.grid(row=8)

#Runs 
runButton = Button(root,text='Create Event', bg='yellow', command = eventClick)
runButton.grid(row=7)
runButtonDirections = Button(root,text = 'Directions', bg = 'yellow', command = directions)
runButtonDirections.grid(row = 11)


#Event Name Selection

eventNameLabel = tk.Label(root,text= 'Enter event name:')
eventNameLabel.grid(row=9)
eventName = tk.StringVar()
eventNameBox = tk.Entry(root, width=18, textvariable= eventName)
eventNameBox.grid(row=10)






#Runs root
directions()
root.mainloop()
