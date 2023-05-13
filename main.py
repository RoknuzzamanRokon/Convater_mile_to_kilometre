from tkinter import *

window = Tk()
window.title("Convert Mile to KM")
window.minsize(height=200, width=400)
window.config(bg="Gray", height=200, width=400)


# Create Entry.
mile_entry = Entry()
mile_entry.config(width=20)
mile_entry.pack()

# Create Label.
mile_label = Label()
mile_label.config(text="Mile", bg="Gray", font=("Arial", 10, "bold"))
mile_label.pack()


window.mainloop()