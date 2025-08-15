


"""importing plugins/addons."""
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk

points = 0  # Global variable to keep track of points


def reset_program(root):
    """Reset the program."""
    global points
    points = 0  # Reset points to 0
    root.destroy()  # Close the current window
    # create root window
    root = tk.Tk()
    # set the window title
    root.title("Pokemon Shiny Quiz")
    # set geometry for the window
    root.geometry("1400x1000")
    # make the window not resizable
    root.resizable(width=False, height=False)
    # the roots configuration for visual appeal
    root.configure(bg="#badcf9")
    # text options
    label = tk.Label(root,
                     text="Welcome to the Pokemon Shiny Quiz!\n\n" 
                     "Click the button to start the quiz.",
                     anchor=tk.CENTER,
                     height=3,
                     width=30,
                     fg="black",
                     font=("Arial", 16, "bold"),
                     bg="#badcf9",
                     justify=tk.CENTER,
                     wraplength=250)
    label.pack(pady=20)

    # button options
    button = tk.Button(root,
                       text="Start Quiz",
                       command=lambda: question_1(root),
                       anchor="center",
                       bd=3,
                       cursor="hand2",
                       font=("Arial", 16, "bold"),
                       height=2,
                       justify="center",
                       width=15)
    button.pack(padx=20, pady=20)


def button_click_q3(button_number, root, label):
    """Handle button clicks."""
    global points
    if button_number > 0:
        messagebox.showinfo("", "Correct answer for question 3!")
        points += button_number  # Add points based on the button clicked
        root.destroy()
    else:
        messagebox.showinfo("", "Incorrect answer for question 3.")
        root.destroy()

    root = tk.Tk()
    # set the window title
    root.title("Pokemon Shiny Quiz")
    # set geometry for the window
    root.geometry('1400x1000')
    root.configure(bg="#badcf9")
    # make the window not resizable
    root.resizable(width=False, height=False)
    # text options
    label = tk.Label(root,
                     text=f"Your Final Score is {points}",
                     anchor=tk.CENTER,
                     height=3,
                     width=30,
                     fg="black",
                     bg="#badcf9",
                     font=("Arial", 16, "bold"),
                     justify=tk.CENTER,
                     wraplength=250)
    label.pack(pady=20)
    kaboom = tk.Button(root, text="Reset Quiz",
                       cursor="hand2",
                       command=lambda: reset_program(root),
                       font=("Arial", 16, "bold"))
    kaboom.place(x=525, y=130, width=150, height=100)
    exit = tk.Button(root, text="Exit",
                     command=root.destroy,
                     cursor="hand2",
                     font=("Arial", 16, "bold"))
    exit.place(x=725, y=130, width=150, height=100)


def hintbutton3(root, label):
    """Show a hint for question 3."""
    messagebox.showinfo("Hint", "The shiny form of Pikachu is a warm colour.")


def question_3(root, label):
    """Start the quiz when the button is clicked."""
    label.config(text="3. What is the shiny form of Pikachu?")
    # images for the first question
    quizimg = Image.open("Quiz Files/Pikachu1.png")
    quizimg = ImageTk.PhotoImage(quizimg)
    image_label = tk.Button(root,
        image=quizimg,
        cursor="hand2",
        command=lambda: button_click_q3(0, root, label))
    image_label.place(x=400, y=230, width=288, height=288)
    quizimg2 = Image.open("Quiz Files/Pikachu2.png")
    quizimg2 = ImageTk.PhotoImage(quizimg2)
    image_label2 = tk.Button(root,
        image=quizimg2,
        cursor="hand2",
        command=lambda: button_click_q3(0, root, label))
    image_label2.place(x=700, y=230, width=288, height=288)
    quizimg3 = Image.open("Quiz Files/Pikachu3.png")
    quizimg3 = ImageTk.PhotoImage(quizimg3)
    image_label3 = tk.Button(root,
        image=quizimg3,
        cursor="hand2",
        command=lambda: button_click_q3(1, root, label))
    image_label3.place(x=400, y=530, width=288, height=288)
    quizimg4 = Image.open("Quiz Files/Pikachu4.png")
    quizimg4 = ImageTk.PhotoImage(quizimg4)
    image_label4 = tk.Button(root,
        image=quizimg4,
        cursor="hand2",
        command=lambda: button_click_q3(0, root, label))
    image_label4.place(x=700, y=530, width=288, height=288)
    # keep a reference to the image to prevent garbage collection
    image_label.image = quizimg
    image_label2.image = quizimg2
    image_label3.image = quizimg3
    image_label4.image = quizimg4
    # hint button
    hint = tk.Button(root,
        text="Hint",
        command=lambda: hintbutton3(root, label),
        font=("Arial", 16, "bold"),
        cursor="hand2")
    hint.place(x=600, y=150, width=200, height=50),


def button_click_q2(button_number, root, label):
    """Handle button clicks."""
    global points
    if button_number > 0:
        messagebox.showinfo("", "Correct answer for question 2!")
        points += button_number  # Add points based on the button clicked
        question_3(root, label)
    else:
        messagebox.showinfo("", "Incorrect answer for question 2.")
        question_3(root, label)


def hintbutton2(root, label):
    """Show a hint for question 2."""
    messagebox.showinfo("Hint", "The shiny form of Gyarados looks very angry.")


def question_2(root, label):
    """Start the quiz when the button is clicked."""
    label.config(text="2. What is the shiny form of Gyarados?")
    # images for the second question
    quizimg = Image.open("Quiz Files/Gyarados1.png")
    quizimg = ImageTk.PhotoImage(quizimg)
    image_label = tk.Button(root,
        image=quizimg,
        cursor="hand2",
        command=lambda: button_click_q2(0, root, label))
    image_label.place(x=400, y=230, width=288, height=288)
    quizimg2 = Image.open("Quiz Files/Gyarados2.png")
    quizimg2 = ImageTk.PhotoImage(quizimg2)
    image_label2 = tk.Button(root,
        image=quizimg2,
        cursor="hand2",
        command=lambda: button_click_q2(0, root, label))
    image_label2.place(x=700, y=230, width=288, height=288)
    quizimg3 = Image.open("Quiz Files/Gyarados3.png")
    quizimg3 = ImageTk.PhotoImage(quizimg3)
    image_label3 = tk.Button(root,
        image=quizimg3,
        cursor="hand2",
        command=lambda: button_click_q2(0, root, label))
    image_label3.place(x=400, y=530, width=288, height=288)
    quizimg4 = Image.open("Quiz Files/Gyarados4.png")
    quizimg4 = ImageTk.PhotoImage(quizimg4)
    image_label4 = tk.Button(root,
        image=quizimg4,
        cursor="hand2",
        command=lambda: button_click_q2(1, root, label))
    image_label4.place(x=700, y=530, width=288, height=288)
    # keep a reference to the image to prevent garbage collection
    image_label.image = quizimg
    image_label2.image = quizimg2
    image_label3.image = quizimg3
    image_label4.image = quizimg4
    # hint button
    hint = tk.Button(root,
        text="Hint",
        command=lambda: hintbutton2(root, label),
        font=("Arial", 16, "bold"),
        cursor="hand2")
    hint.place(x=600, y=150, width=200, height=50),


def button_click_q1(button_number, root, label):
    """Handle button clicks."""
    global points
    if button_number > 0:
        messagebox.showinfo("", "Correct answer for question 1!")
        points += button_number  # Add points based on the button clicked
        question_2(root, label)
    else:
        messagebox.showinfo("", "Incorrect answer for question 1.")
        question_2(root, label)

def hintbutton1 (root, label):
    """Show a hint for question 1."""
    messagebox.showinfo("Hint", "The shiny form of Ponyta has a blue flame.")

def question_1(root):
    """Start the quiz when the button is clicked."""
    global label_text
    root.destroy()  # Close the initial window
    root = tk.Tk()
    # set the window title
    root.title("Pokemon Shiny Quiz")
    # set geometry for the window
    root.geometry('1400x1000')
    root.configure(bg="#badcf9")
    # make the window not resizable
    root.resizable(width=False, height=False)
    # text options
    label = tk.Label(root,
        text="1. What is the shiny form of Ponyta?",
        anchor=tk.CENTER,      
        height=3,              
        width=30,
        fg="black", 
        bg="#badcf9",                
        font=("Arial", 16, "bold"),             
        justify=tk.CENTER,    
        wraplength=250)
    label.pack(pady=20)
    # images for the first question
    quizimg = Image.open("Quiz Files/Ponyta1.png")
    quizimg = ImageTk.PhotoImage(quizimg)
    image_label = tk.Button(root, 
    image=quizimg, 
    cursor="hand2",
    command=lambda: button_click_q1(1, root, label))
    image_label.place(x=400, y=230, width=288, height=288)
    quizimg2 = Image.open("Quiz Files/Ponyta2.png")
    quizimg2 = ImageTk.PhotoImage(quizimg2)
    image_label2 = tk.Button(root, 
    image=quizimg2, 
    cursor="hand2",
    command=lambda: button_click_q1(0, root, label))
    image_label2.place(x=700, y=230, width=288, height=288)
    quizimg3 = Image.open("Quiz Files/Ponyta3.png")
    quizimg3 = ImageTk.PhotoImage(quizimg3)
    image_label3 = tk.Button(root, 
    image=quizimg3, 
    cursor="hand2",
    command=lambda: 
    button_click_q1(0, root, label))
    image_label3.place(x=400, y=530, width=288, height=288)
    quizimg4 = Image.open("Quiz Files/Ponyta4.png")
    quizimg4 = ImageTk.PhotoImage(quizimg4)
    image_label4 = tk.Button(root, 
    image=quizimg4, 
    cursor="hand2",
    command=lambda: button_click_q1(0, root, label))
    image_label4.place(x=700, y=530, width=288, height=288)
    # keep a reference to the image to prevent garbage collection
    image_label.image = quizimg
    image_label2.image = quizimg2
    image_label3.image = quizimg3
    image_label4.image = quizimg4
    # hint button
    hint = tk.Button(root, 
    text="Hint", 
    command=lambda: hintbutton1(root, label),
    font=("Arial", 16, "bold"),
    cursor="hand2")
    hint.place(x=600, y=150, width=200, height=50),

# create root window
root = tk.Tk()
# set the window title
root.title("Pokemon Shiny Quiz")
# set geometry for the window
root.geometry("1400x1000")
# make the window not resizable
root.resizable(width=False, height=False)
# the roots configuration for visual appeal
root.configure(bg="#badcf9")
# text options
label = tk.Label(root,
    text="Welcome to the Pokemon Shiny Quiz!\n\n" \
    "Click the button to start the quiz.",
    anchor=tk.CENTER,      
    height=3,              
    width=30,
    fg="black",                 
    font=("Arial", 16, "bold"),
    bg="#badcf9",
    justify=tk.CENTER,    
    wraplength=250)
label.pack(pady=20)

# button options
button = tk.Button(root, 
    text="Start Quiz", 
    command=lambda: question_1(root),
    anchor="center",
    bd=3,
    cursor="hand2",
    font=("Arial", 16, "bold"),
    height=2,
    justify="center",
    width=15)
button.pack(padx=20, pady=20)
root.mainloop()