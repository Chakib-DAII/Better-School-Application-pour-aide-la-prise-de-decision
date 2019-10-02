from tkinter import *
import functions as metier

def demarrerTbd():
    root = Tk()
    root.iconbitmap("..\pics\icon.ico")
    root.title('Better School : Tableau de bord')
    
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    #Add a canvas to the window
    canvas = Canvas(root,width=w, height=h)
    canvas.grid(column=0, row=0, sticky=N+S+E+W)
    root.geometry('%dx%d+%d+%d' % (550, 105, (w/2)-275, (h/2)-52))

    #Allow the canvas (in row/column 0,0)
    #to "grow" to fill the entire window.
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    
    root.resizable(False, False)



    #This frame must be defined as a child of the canvas,
    #even though we later add it as a window to the canvas
    f = Frame(canvas)

    x=1
    y=1

    bouton1=Button(f, text='    moyenne General     ' , borderwidth=1, command=metier.classparnationality).grid(row=x, column=y);y=y+1
    bouton2=Button(f, text='   moyenne/Gouvernorat  ' , borderwidth=1, command=metier.classparplaceofbirth).grid(row=x, column=y);y=y+1
    bouton3=Button(f, text='    moyenne/Matiere     ' , borderwidth=1, command=metier.classpartopic).grid(row=x, column=y);y=y+1
    bouton4=Button(f, text='     moyenne/Genre      ' , borderwidth=1, command=metier.classpargender).grid(row=x, column=y);y=y+1
   

    x=x+1
    y=1

    bouton5=Button(f, text='      moyenne/Level     ' , borderwidth=1, command=metier.classparstage).grid(row=x, column=y);y=y+1
    bouton6=Button(f, text='    moyenne/Semestre    ' , borderwidth=1, command=metier.classparsemester).grid(row=x, column=y);y=y+1
    bouton7=Button(f, text='      absence/Jours     ' , borderwidth=1, command=metier.abscenceperday).grid(row=x, column=y);y=y+1
    bouton8=Button(f, text='    absence/Matiere     ' , borderwidth=1, command=metier.abscenceperdaypartopic).grid(row=x, column=y);y=y+1

    x=x+1
    y=1

    bouton9=Button(f, text='      absence/Genre     ' , borderwidth=1, command=metier.abscenceperdaypargender).grid(row=x, column=y);y=y+1
    bouton10=Button(f, text='     absence/Level     ' , borderwidth=1, command=metier.abscenceperdayparstage).grid(row=x, column=y);y=y+1
    bouton11=Button(f, text='    absence/Semestre   '  , borderwidth=1, command=metier.abscenceperdayparsemester).grid(row=x, column=y);y=y+1
    bouton12=Button(f, text='   Discussion/Matiere  ' , borderwidth=1, command=metier.discussionpartopic).grid(row=x, column=y);y=y+1

    x=x+1
    y=1

    bouton13=Button(f, text='  participation/Matiere ' , borderwidth=1, command=metier.raisedhandspartopic).grid(row=x, column=y);y=y+1
    bouton14=Button(f, text='palette De participation' , borderwidth=1, command=metier.palettedeparticipation).grid(row=x, column=y);y=y+1
    bouton15=Button(f, text='    Effet de Famille    ' , borderwidth=1, command=metier.relationwithfamily).grid(row=x, column=y);y=y+1
    bouton16=Button(f, text='  Effet de Discussion   ' , borderwidth=1, command=metier.discussionparticipation).grid(row=x, column=y);y=y+1

    x=x+1
    y=1
    
    #Add the frame to the canvas
    canvas.create_window((0,0), anchor=NW, window=f)

    #IMPORTANT:

    f.update_idletasks() #REQUIRED: For f.bbox() below to work!

    #Tell the canvas how big of a region it should scroll
    canvas.config(scrollregion= f.bbox("all")  )


    mainloop()  #Wait for user events!
