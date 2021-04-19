from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter.filedialog import askdirectory


def select_directory():
    path = askdirectory(title="Select a folder")
    selected_dir_lbl.configure(text=path)

window = Tk()

window.title("PDF word searcher")
window.geometry("500x200")

instruction_text = "Por favor, selecciona un directorio de búsqueda e introduce una palabra a buscar"
text_font = "Arial Bold"
text_size = 10

instruction_lbl = Label(window, text=instruction_text, font=(text_font, text_size))
selected_dir_lbl = Label(window, text="", font=(text_font, text_size))
select_dir_btn = Button(window, text="Select Directory", command=select_directory)
word_search_ent = Entry(window, width=20)
search_btn = Button(window, text="Search")

instruction_lbl.grid(column=0, row=0)
selected_dir_lbl.grid(column=0, row=2)
select_dir_btn.grid(column=0, row=3)
word_search_ent.grid(column=0, row=4)
search_btn.grid(column=0, row=5)

window.mainloop()