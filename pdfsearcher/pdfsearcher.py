#Open a PDF and search an user determined text
#By MaghO
#v1.0.0

import io
import os
import pathlib

import findPages
import UserInterface

PDF_PATH = '..\data'

def search_word_dir(filepath, search_word):

    print("Searching...")
    for subdir, dirs, files in os.walk(filepath):

        for filename in files:
            filepath = subdir + os.sep + filename

            if filepath.endswith(".pdf"):
                found_pages = findPages.find_in_pdf(filepath, search_word)    
                print(filepath)
                print(found_pages)

    print("Finished.")

def console_main():

    print(f"Actualmente te encuentras en el directorio {pathlib.Path(__file__).parent.absolute()}")
    print(f"La busqueda va a realizarse en el directorio {PDF_PATH}")
    print("//////////////////////////////////////////////////////////////////")
    print("Introduce la palabra que desees encontrar, escribe exit para salir: ")
    while True:

        try:
            user_in = str(input(">"))
        except ValueError:
            print("Not valid format")

        if user_in != "exit":
            search_word_dir(PDF_PATH, user_in)
        else:
            break

def main():
    root = tk.Tk()
    ui = UserInterface(master=root)
    ui.master.title("PDF READER Interface")
    ui.mainloop()
  
if __name__ == "__main__":
    main()