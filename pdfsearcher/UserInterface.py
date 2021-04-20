# WORK IN PROGRESS
import io
import os
import pathlib

import tkinter as tk
import tkinter.filedialog as tk_fd

import findPages

class UserInterface(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.file_path_lbl = tk.Label(self, text="Selecciona un directorio de búsqueda", 
                                    font=("Arial Bold", 20))
        self.file_path_lbl.pack()

        self.select_path_btn = tk.Button(self, text="Directorio",
                                    command=self.select_file_path)
        self.select_path_btn.pack()    

        self.word_search_ent = tk.Entry(self, width=20)
        self.word_search_ent.pack()

        self.search_btn = tk.Button(self, text="Buscar",
                                    command=self.search_word)
        self.search_btn.pack()

    def select_file_path(self):
        path = tk_fd.askdirectory(title="Select a folder")
        self.file_path_lbl["text"] = path

    def search_word(self):
        if self.file_path_lbl["text"]: 
            for subdir, dirs, files in os.walk(self.file_path_lbl["text"]):

                for filename in files:
                    filepath = subdir + os.sep + filename

                    if filepath.endswith(".pdf"):
                        found_pages = findPages.find_in_pdf(filepath, 
                                                            self.word_search_ent.get())    
                        print(self.file_path_lbl["text"])
                        print(self.word_search_ent.get()) 
                        print(found_pages)

root = tk.Tk()
ui = UserInterface(master=root)
ui.master.title("PDF READER Interface")
ui.mainloop()