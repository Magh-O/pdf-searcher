# WORK IN PROGRESS
import io
import os
import pathlib

import tkinter as tk
import tkinter.filedialog as tk_fd
import tkinter.ttk as tk_ttk

import findPages

class UserInterface(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.file_path_lbl = tk.Label(self, text="Selecciona un directorio de búsqueda", 
                                    font=("Arial Bold", 10))
        self.file_path_lbl.pack(fill=tk.X)

        self.select_path_btn = tk.Button(self, text="Seleccionar Directorio",
                                    command=self.select_file_path)
        self.select_path_btn.pack(fill=tk.X)    

        self.word_search_ent = tk.Entry(self)
        self.word_search_ent.pack(fill=tk.X)

        self.search_btn = tk.Button(self, text="Buscar",
                                    command=self.result_window)
        self.search_btn.pack(fill=tk.X)

        #self.progress_bar = tk_ttk.Progressbar(self, mode="indeterminate")
        #self.progress_bar.pack()

    def select_file_path(self):
        path = tk_fd.askdirectory(title="Select a folder")
        self.file_path_lbl["text"] = path

    def search_word(self):
        result_text = ""

        if self.file_path_lbl["text"]: 
            for subdir, dirs, files in os.walk(self.file_path_lbl["text"]):

                for filename in files:
                    filepath = subdir + os.sep + filename

                    if filepath.endswith(".pdf"):
                        found_pages = findPages.find_in_pdf(filepath, 
                                                            self.word_search_ent.get())    

                        result_text += f'Directorio: {filename}\nPáginas encontradas: {found_pages}\n///////////////\n'

            
        return result_text
    
    def result_window(self):
        popup = tk.Toplevel()        
        
        result_text = self.search_word()        

        result_lbl = tk.Text(popup)        
        result_lbl.insert("1.0", result_text)
        result_lbl.config(state="disabled")
        result_lbl.pack()

        popup.mainloop()

root = tk.Tk()
ui = UserInterface(master=root)
ui.master.title("PDF READER Interface")
ui.mainloop()