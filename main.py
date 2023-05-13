from tkinter import *

window = Tk()
window.title("Convert Mile to KM")
window.minsize(height=200, width=400)
window.config(bg="Gray", height=200, width=400)


# Create Entry.
mile_entry01 = Entry()
mile_entry01.config(width=20)
mile_entry01.pack()

# Create Label.
mile_label = Label()
mile_label.config(text="Mile", bg="Gray", font=("Arial", 10, "bold"))
mile_label.pack()

my_label_01 = Label()
my_label_01.config(text="is equal ", bg="Gray", font=("Arial", 10, "bold"))
my_label_01.pack()


mile_entry02 = Entry()
mile_entry02.config(width=20)
mile_entry02.pack()

my_label_02 = Label()
my_label_02.config(text="KM ", bg="Gray", font=("Arial", 10, "bold"))
my_label_02.pack()


# Create a Button.
my_button = Button()
my_button.config(text="Calculate")
my_button.pack()


window.mainloop()