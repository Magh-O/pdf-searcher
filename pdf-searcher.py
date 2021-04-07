#Open a PDF and search an user determined text

import io
import os
import pathlib

#Import the dependencies for pdf extraction
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

pdf_path = './test.pdf'

def search_text(page, search_word):
    """This function gets a page in string format and a word to search, if the word appears in the 
    page text it returns True"""

    index = page.lower().find(search_word.lower())
    if index>=0:
        return True
    else:
        return False

def extract_page_text(pdf_path):
    with open(pdf_path, 'rb') as f:
        for page in PDFPage.get_pages(f, 
                                    caching=True,
                                    check_extractable=True):
            res_manager = PDFResourceManager()
            fake_f_handle = io.StringIO()
            converter = TextConverter(res_manager, fake_f_handle)
            page_interpreter = PDFPageInterpreter(res_manager, converter)
            page_interpreter.process_page(page)

            text = fake_f_handle.getvalue()
            yield text

            converter.close()
            fake_f_handle.close()

def extract_text(pdf_path, search_word):
    page_count = 1
    found_pages = []
    for page in extract_page_text(pdf_path):
        if search_text(page, search_word):
            found_pages.append(page_count)
        page_count += 1

    return found_pages

def search_word_dir(filepath, search_word):

    print("Searching...")
    for subdir, dirs, files in os.walk(filepath):
        for filename in files:
            filepath = subdir + os.sep + filename

            if filepath.endswith(".pdf"):
                found_pages = extract_text(filepath, search_word)
                #founds[filepath].append(found_pages)
                print(filepath)
                print(found_pages)

    print("Finished.")

def main_loop():

    print(f"The current folder is {pathlib.Path(__file__).parent.absolute()}")
    print("//////////////////////////////////////////////////////////////////")
    print("Introduce la palabra que desees encontrar, escribe exit para salir: ")
    while True:

        try:
            user_in = str(input(">"))
        except ValueError:
            print("Not valid format")

        if user_in != "exit":
            search_word_dir('./files-to-search', user_in)
        else:
            break

main_loop()