"""importing plugins/addons"""
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
#create root window
root = tk.Tk()
#set the window title
root.title("Pokemon Shiny Quiz")
#set geometry for the window
root.geometry('1400x1000')
#make the window not resizable
root.resizable(width=False, height=False)
#text options
label = tk.Label(root,
    text="Welcome to the Pokemon Shiny Quiz!\n\n" \
    "Click the button to start the quiz.",
    anchor=tk.CENTER,      
    height=3,              
    width=30,
    fg="black",                 
    font=("Arial", 16, "bold"),             
    justify=tk.CENTER,    
    wraplength=250)
label.pack(pady=20)
#button testing

points = 0  # Global variable to keep track of points
label_text = "Welcome to the Pokemon Shiny Quiz!\n\n"

def button_click_q3(button_number, root, label):
    """Function to handle button clicks."""
    global points
    if button_number > 0:
        messagebox.showinfo("","Correct answer for question 3!")
        points += button_number  # Add points based on the button clicked
        root.destroy()  # Close the current window
    else:
        messagebox.showinfo("","Incorrect answer for question 3.")
        root.destroy()  # Close the current window

def question_3(root, label):
    """Function to start the quiz when the button is clicked."""
    label.config(text="3. What is the shiny form of Pikachu?")
    #images for the first question
    quizimg = Image.open("Assets for my Game/Pikachu1.png")
    quizimg = ImageTk.PhotoImage(quizimg)
    image_label = tk.Button(root, image=quizimg, command=lambda: 
                            button_click_q3(0, root, label))
    image_label.place(x=400, y=230, width=288, height=288)
    quizimg2 = Image.open("Assets for my Game/Pikachu2.png")
    quizimg2 = ImageTk.PhotoImage(quizimg2)
    image_label2 = tk.Button(root, image=quizimg2, command=lambda: 
                             button_click_q3(0, root, label))
    image_label2.place(x=700, y=230, width=288, height=288)
    quizimg3 = Image.open("Assets for my Game/Pikachu3.png")
    quizimg3 = ImageTk.PhotoImage(quizimg3)
    image_label3 = tk.Button(root, image=quizimg3, command=lambda: 
                             button_click_q3(1,root, label))
    image_label3.place(x=400, y=530, width=288, height=288)
    quizimg4 = Image.open("Assets for my Game/Pikachu4.png")
    quizimg4 = ImageTk.PhotoImage(quizimg4)
    image_label4 = tk.Button(root, image=quizimg4, command=lambda: 
                             button_click_q3(0,root, label))
    image_label4.place(x=700, y=530, width=288, height=288)
    #keep a reference to the image to prevent garbage collection
    image_label.image = quizimg
    image_label2.image = quizimg2
    image_label3.image = quizimg3
    image_label4.image = quizimg4

def button_click_q2(button_number, root, label):
    """Function to handle button clicks."""
    global points
    if button_number > 0:
        messagebox.showinfo("","Correct answer for question 2!")
        points += button_number  # Add points based on the button clicked
        question_3(root, label)
    else:
        messagebox.showinfo("","Incorrect answer for question 2.")
        question_3(root, label)

def question_2(root, label):
    """Function to start the quiz when the button is clicked."""
    label.config(text="2. What is the shiny form of Gyarados?")
    #images for the second question
    quizimg = Image.open("Assets for my Game/Gyarados1.png")
    quizimg = ImageTk.PhotoImage(quizimg)
    image_label = tk.Button(root, image=quizimg, command=lambda: 
                            button_click_q2(0, root, label))
    image_label.place(x=400, y=230, width=288, height=288)
    quizimg2 = Image.open("Assets for my Game/Gyarados2.png")
    quizimg2 = ImageTk.PhotoImage(quizimg2)
    image_label2 = tk.Button(root, image=quizimg2, command=lambda: 
                             button_click_q2(0, root, label))
    image_label2.place(x=700, y=230, width=288, height=288)
    quizimg3 = Image.open("Assets for my Game/Gyarados3.png")
    quizimg3 = ImageTk.PhotoImage(quizimg3)
    image_label3 = tk.Button(root, image=quizimg3, command=lambda: 
                             button_click_q2(0,root, label))
    image_label3.place(x=400, y=530, width=288, height=288)
    quizimg4 = Image.open("Assets for my Game/Gyarados4.png")
    quizimg4 = ImageTk.PhotoImage(quizimg4)
    image_label4 = tk.Button(root, image=quizimg4, command=lambda: 
                             button_click_q2(1,root, label))
    image_label4.place(x=700, y=530, width=288, height=288)
    #keep a reference to the image to prevent garbage collection
    image_label.image = quizimg
    image_label2.image = quizimg2
    image_label3.image = quizimg3
    image_label4.image = quizimg4

def button_click_q1(button_number, root, label):
    """Function to handle button clicks."""
    global points
    if button_number > 0:
        messagebox.showinfo("","Correct answer for question 1!")
        points += button_number  # Add points based on the button clicked
        question_2(root, label)
    else:
        messagebox.showinfo("","Incorrect answer for question 1.")
        question_2(root, label)

def question_1(root):
    """Function to start the quiz when the button is clicked."""
    global label_text
    root.destroy()  # Close the initial window
    root = tk.Tk()
    #set the window title
    root.title("Pokemon Shiny Quiz")
    #set geometry for the window
    root.geometry('1400x1000')
    #make the window not resizable
    root.resizable(width=False, height=False)
    #text options
    label = tk.Label(root,
        text="1. What is the shiny form of Ponyta?",
        anchor=tk.CENTER,      
        height=3,              
        width=30,
        fg="black",                 
        font=("Arial", 16, "bold"),             
        justify=tk.CENTER,    
        wraplength=250)
    label.pack(pady=20)
    messagebox.showinfo("","Quiz Started")
    #images for the first question
    quizimg = Image.open("Assets for my Game/Ponyta1.png")
    quizimg = ImageTk.PhotoImage(quizimg)
    image_label = tk.Button(root, image=quizimg, command=lambda: 
                            button_click_q1(1, root, label))
    image_label.place(x=400, y=230, width=288, height=288)
    quizimg2 = Image.open("Assets for my Game/Ponyta2.png")
    quizimg2 = ImageTk.PhotoImage(quizimg2)
    image_label2 = tk.Button(root, image=quizimg2, command=lambda: 
                             button_click_q1(0, root, label))
    image_label2.place(x=700, y=230, width=288, height=288)
    quizimg3 = Image.open("Assets for my Game/Ponyta3.png")
    quizimg3 = ImageTk.PhotoImage(quizimg3)
    image_label3 = tk.Button(root, image=quizimg3, command=lambda: 
                             button_click_q1(0, root, label))
    image_label3.place(x=400, y=530, width=288, height=288)
    quizimg4 = Image.open("Assets for my Game/Ponyta4.png")
    quizimg4 = ImageTk.PhotoImage(quizimg4)
    image_label4 = tk.Button(root, image=quizimg4, command=lambda: 
                             button_click_q1(0, root, label))
    image_label4.place(x=700, y=530, width=288, height=288)
    #keep a reference to the image to prevent garbage collection
    image_label.image = quizimg
    image_label2.image = quizimg2
    image_label3.image = quizimg3
    image_label4.image = quizimg4

#button options
button = tk.Button(root, 
    text="Start Quiz", 
    command=lambda: question_1(root),
    activebackground="light blue", 
    activeforeground="white",
    anchor="center",
    bd=3,
    bg="lightgray",
    cursor="hand2",
    disabledforeground="gray",
    fg="black",
    font=("Arial", 12),
    height=2,
    highlightbackground="black",
    highlightcolor="green",
    highlightthickness=2,
    justify="center",
    overrelief="raised",
    width=15,
    wraplength=100)
button.pack(padx=20, pady=20)
root.mainloop()