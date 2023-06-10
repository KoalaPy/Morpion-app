from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
import customtkinter as ctk

window = ctk.CTk()
window.title("Morpion")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

clique = True
count = 0

def desactive_les_autres_bouttons():
     Button1.config(state=DISABLED)
     Button2.config(state=DISABLED)
     Button3.config(state=DISABLED)

     Button4.config(state=DISABLED)
     Button5.config(state=DISABLED)
     Button6.config(state=DISABLED)

     Button7.config(state=DISABLED)
     Button8.config(state=DISABLED)
     Button9.config(state=DISABLED)

def checkGagne():
    global gagne
    gagne = False
    
    if Button1["text"] == "X" and Button2["text"] == "X" and Button3["text"] == "X":
        Button1.config(bg = "green")
        Button2.config(bg = "green")
        Button3.config(bg = "green")
        gagne = True
        messagebox.showinfo("Bravo", "X à gagné")
        desactive_les_autres_bouttons()

    elif Button4["text"] == "X" and Button5["text"] == "X" and Button6["text"] == "X":
            Button4.config(bg = "green")
            Button5.config(bg = "green")
            Button6.config(bg = "green")
            gagne = True
            messagebox.showinfo("Bravo", "X à gagné")
            desactive_les_autres_bouttons()
    elif Button7["text"] == "X" and Button8["text"] == "X" and Button9["text"] == "X":
            Button7.config(bg = "green")
            Button8.config(bg = "green")
            Button9.config(bg = "green")
            gagne = True
            messagebox.showinfo("Bravo", "X à gagné")
            desactive_les_autres_bouttons()
    elif Button1["text"] == "X" and Button4["text"] == "X" and Button7["text"] == "X":
            Button1.config(bg = "green")
            Button4.config(bg = "green")
            Button7.config(bg = "green")
            gagne = True
            messagebox.showinfo("Bravo", "X à gagné")
            desactive_les_autres_bouttons()
    elif Button2["text"] == "X" and Button5["text"] == "X" and Button8["text"] == "X":
            Button2.config(bg = "green")
            Button5.config(bg = "green")
            Button8.config(bg = "green")
            gagne = True
            messagebox.showinfo("Bravo", "X à gagné")
            desactive_les_autres_bouttons()
    elif Button3["text"] == "X" and Button6["text"] == "X" and Button9["text"] == "X":
            Button3.config(bg = "green")
            Button6.config(bg = "green")
            Button9.config(bg = "green")
            gagne = True
            messagebox.showinfo("Bravo", "X à gagné")
            desactive_les_autres_bouttons()
    elif Button1["text"] == "X" and Button5["text"] == "X" and Button9["text"] == "X":
            Button1.config(bg = "green")
            Button5.config(bg = "green")
            Button9.config(bg = "green")
            gagne = True
            messagebox.showinfo("Bravo", "X à gagné")
            desactive_les_autres_bouttons()
    elif Button3["text"] == "X" and Button5["text"] == "X" and Button7["text"] == "X":
            Button3.config(bg = "green")
            Button5.config(bg = "green")
            Button7.config(bg = "green")
            gagne = True
            messagebox.showinfo("Bravo", "X à gagné")
            desactive_les_autres_bouttons()
    
    if Button1["text"] == "O" and Button2["text"] == "O" and Button3["text"] == "O":
        Button1.config(bg = "green") 
        Button2.config(bg = "green")
        Button3.config(bg = "green")
        gagne = True
        messagebox.showinfo("Bravo", "O à gagné")
        desactive_les_autres_bouttons()

    elif Button4["text"] == "O" and Button5["text"] == "O" and Button6["text"] == "O":
            Button4.config(bg = "green")
            Button5.config(bg = "green")
            Button6.config(bg = "green")
            gagne = True
            messagebox.showinfo("Bravo", "O à gagné")
            desactive_les_autres_bouttons()
    elif Button7["text"] == "O" and Button8["text"] == "O" and Button9["text"] == "O":
            Button7.config(bg = "green")
            Button8.config(bg = "green")
            Button9.config(bg = "green")
            gagne = True
            messagebox.showinfo("Bravo", "O à gagné")
            desactive_les_autres_bouttons()
    elif Button1["text"] == "O" and Button4["text"] == "O" and Button7["text"] == "O":
            Button1.config(bg = "green")
            Button4.config(bg = "green")
            Button7.config(bg = "green")
            gagne = True
            messagebox.showinfo("Bravo", "O à gagné")
            desactive_les_autres_bouttons()
    elif Button2["text"] == "O" and Button5["text"] == "O" and Button8["text"] == "O":
            Button2.config(bg = "green")
            Button5.config(bg = "green")
            Button8.config(bg = "green")
            gagne = True
            messagebox.showinfo("Bravo", "O à gagné")
            desactive_les_autres_bouttons()
    elif Button3["text"] == "O" and Button6["text"] == "O" and Button9["text"] == "O":
            Button3.config(bg = "green")
            Button6.config(bg = "green")
            Button9.config(bg = "green")
            gagne = True
            messagebox.showinfo("Bravo", "O à gagné")
            desactive_les_autres_bouttons()
    elif Button1["text"] == "O" and Button5["text"] == "O" and Button9["text"] == "O":
            Button1.config(bg = "green")
            Button5.config(bg = "green")
            Button9.config(bg = "green")
            gagne = True
            messagebox.showinfo("Bravo", "O à gagné")
            desactive_les_autres_bouttons()
    elif Button3["text"] == "O" and Button5["text"] == "O" and Button7["text"] == "O":
            Button3.config(bg = "green")
            Button5.config(bg = "green")
            Button7.config(bg = "green")
            gagne = True
            messagebox.showinfo("Bravo", "O à gagné")
            desactive_les_autres_bouttons()

    if count ==  9 and gagne == False:
        messagebox.showinfo("Morpion", "Perdu ! Aucune personne a gagné.")
        desactive_les_autres_bouttons()

def Button_click(b):
    global clique, count
    if b["text"] == " " and clique == True:
        b["text"] = "X"
        clique = False
        count += 1
        text1 = Label(window, text= "O", fg= "black", bg= "#00FF11", font=("Courrier", 12))
        text2 = Label(window, text= "X", fg= "black", bg= "#000000", font=("Courrier", 12))
        text1.grid(row=5,column=0)
        text2.grid(row=5,column=2)
        checkGagne()

    elif b["text"] == " " and clique == False: 
        b["text"] = "O"
        clique = True
        count += 1
        text1 = Label(window, text= "O", fg= "black", bg= "#000000", font=("Courrier", 12))
        text2 = Label(window, text= "X", fg= "black", bg= "#00FF11", font=("Courrier", 12))
        text1.grid(row=5,column=0)
        text2.grid(row=5,column=2)
        checkGagne()

def rejouer():
    global Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, Button9
    global clique, count
    clique = True
    count = 0 

    Button1 = Button(window, text=" ", font=("Courrier", 15), height= 3, width= 6, bg="SystemButtonFace", command=lambda:Button_click(Button1), background="#000000", fg="white")
    Button2 = Button(window, text=" ", font=("Courrier", 15), height= 3, width= 6, bg="SystemButtonFace", command=lambda:Button_click(Button2), background="#000000", fg="white")
    Button3 = Button(window, text=" ", font=("Courrier", 15), height= 3, width= 6, bg="SystemButtonFace", command=lambda:Button_click(Button3), background="#000000", fg="white")

    Button4 = Button(window, text=" ", font=("Courrier", 15), height = 3, width= 6, bg="SystemButtonFace", command=lambda:Button_click(Button4), background="#000000", fg="white")
    Button5 = Button(window, text=" ", font=("Courrier", 15), height = 3, width= 6, bg="SystemButtonFace", command=lambda:Button_click(Button5), background="#000000", fg="white")
    Button6 = Button(window, text=" ", font=("Courrier", 15), height = 3, width= 6, bg="SystemButtonFace", command=lambda:Button_click(Button6), background="#000000", fg="white")

    Button7 = Button(window, text=" ", font=("Courrier", 15), height = 3, width= 6, bg="SystemButtonFace", command=lambda:Button_click(Button7), background="#000000", fg="white")
    Button8 = Button(window, text=" ", font=("Courrier", 15), height = 3, width= 6, bg="SystemButtonFace", command=lambda:Button_click(Button8), background="#000000", fg="white")
    Button9 = Button(window, text=" ", font=("Courrier", 15), height = 3, width= 6, bg="SystemButtonFace", command=lambda:Button_click(Button9), background="#000000", fg="white")


    Button1.grid(row=0, column=0)
    Button2.grid(row=0, column=1)
    Button3.grid(row=0, column=2)

    Button4.grid(row=1, column=0)
    Button5.grid(row=1, column=1)
    Button6.grid(row=1, column=2)

    Button7.grid(row=2, column=0)
    Button8.grid(row=2, column=1)
    Button9.grid(row=2, column=2)

menu = Menu(window)
window.config(menu = menu)

option_menu = Menu(menu, tearoff=0)
menu.add_checkbutton(label= "Quitter", command= quit)
menu.add_checkbutton(label= "Rejouer", command= rejouer)
rejouer()

window.mainloop()