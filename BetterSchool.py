import numpy as np #linear algebra
import pandas as pd #data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pylab as plt
import seaborn as sns
from tkinter import *
import csv
from tkinter.filedialog import *
import functions as metier
import tableaudebord as tdb
sns.set(style='ticks')


def alert():
    print('fonction en cours de developpement')

def openCSV():
    filename = askopenfilename(title="Ouvrir votre document",filetypes=[('csv files','.csv'),('all files','.*')])
    data=pd.read_csv(r'xAPI-Edu-Data.csv')

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

#from subprocess import check_output
#print(check_output(["ls", "../input"]).decode("utf8"))

# Any results you write to the current directory are saved as output.
data=pd.read_csv(r'xAPI-Edu-Data.csv')

# there are no nan values or missing something in 
print(data.info())

# These are the features names
print(data.columns)

root = Tk()

root.iconbitmap("..\pics\icon.ico")
root.title('Better School')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#Add a canvas to the window
canvas = Canvas(root,width=w, height=h)
canvas.grid(column=0, row=0, sticky=N+S+E+W)
root.geometry('%dx%d+%d+%d' % (w, h, 0, 0))

menubar = Menu(root)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Sourcer", command=openCSV)
menu1.add_command(label="TableauDeBord", command=tdb.demarrerTbd)
menu1.add_separator()
menu1.add_command(label="Quitter", command=root.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

root.config(menu=menubar)

#Allow the canvas (in row/column 0,0)
#to "grow" to fill the entire window.
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


#Add a scrollbar that will scroll the canvas vertically
vscrollbar = Scrollbar(root)
vscrollbar.grid(column=1, row=0, sticky=N+S)
#Link the scrollbar to the canvas
canvas.config(yscrollcommand=vscrollbar.set)
vscrollbar.config(command=canvas.yview)


#Add a scrollbar that will scroll the canvas horizontally
hscrollbar = Scrollbar(root, orient=HORIZONTAL)
hscrollbar.grid(column=0, row=1, sticky=E+W)
canvas.config(xscrollcommand=hscrollbar.set)
hscrollbar.config(command=canvas.xview)



#This frame must be defined as a child of the canvas,
#even though we later add it as a window to the canvas
f = Frame(canvas)


#Create a button in the frame.
#b = Button(f,text="hi there")
#b.grid(row=0, column=0)

#read csv
fichier = open(r"xAPI-Edu-Data.csv", "r")
readCSV = csv.reader(fichier, delimiter=',')
x=1
y=1
#create dashboard
#for colonne in range(5):
#    Label(f, text='').grid(row=x, column=y)
#    y=y+1
   
#bouton1=Button(f, text='L%s-C%s' % (x, y), borderwidth=1, command=metier.raisedhandspartopic).grid(row=x, column=y);y=y+1
#bouton2=Button(f, text='L%s-C%s' % (x, y), borderwidth=1, command=metier.unsuccess).grid(row=x, column=y);y=y+1
#bouton3=Button(f, text='L%s-C%s' % (x, y), borderwidth=1, command=metier.nationality).grid(row=x, column=y);y=y+1
#bouton4=Button(f, text='L%s-C%s' % (x, y), borderwidth=1, command=metier.chimestry).grid(row=x, column=y);y=y+1
#bouton5=Button(f, text='L%s-C%s' % (x, y), borderwidth=1, command=metier.relationwithfamily).grid(row=x, column=y);y=y+1
#bouton6=Button(f, text='L%s-C%s' % (x, y), borderwidth=1, command=metier.discussionparticipation).grid(row=x, column=y);y=y+1
#bouton7=Button(f, text='L%s-C%s' % (x, y), borderwidth=1, command=metier.abscenceperday).grid(row=x, column=y);y=y+1
x=x+1
y=1
l=0;
#Add a large grid of sample label widgets to fill the space
for row in readCSV:
    for element in row:
        if(y==1):
            if(l==0):
                Label(f, text='  ').grid(row=x, column=y);y=y+1;l=l+1
            else :
                Label(f, text=l).grid(row=x, column=y);y=y+1;l=l+1
        Label(f, text=element).grid(row=x, column=y)
        y=y+1
    y=1    
    x=x+1

#Add the frame to the canvas
canvas.create_window((0,0), anchor=NW, window=f)

#IMPORTANT:

f.update_idletasks() #REQUIRED: For f.bbox() below to work!

#Tell the canvas how big of a region it should scroll
canvas.config(scrollregion= f.bbox("all")  )

#lancer le tableau de bord
tdb.demarrerTbd()
mainloop()  #Wait for user events!
