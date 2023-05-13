from tkinter import *

window = Tk()
window.title("Convert Mile to KM")
window.minsize(height=200, width=400)
window.config(bg="Gray", height=200, width=400)


# Create a button function.
def button_function():
    flot_miles = float(mile_entry01.get())
    convert_file = flot_miles * 1.60934
    my_textbox.insert(END, convert_file)



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

# Create a textBox.
my_textbox = Text()
my_textbox.config(width=10, height=1)
my_textbox.pack()

my_label_02 = Label()
my_label_02.config(text="KM ", bg="Gray", font=("Arial", 10, "bold"))
my_label_02.pack()


# Create a Button.
my_button = Button()
my_button.config(text="Calculate", command=button_function)
my_button.pack()


window.mainloop()