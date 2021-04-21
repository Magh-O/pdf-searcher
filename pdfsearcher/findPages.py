from pdfsearcher import searchText

import io
import os
import pathlib

#Import the dependencies for pdf extraction
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

def extract_page_text(pdf_path):
    try:
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
    except PermissionError:
        print("No tiene permisos de acceso en el archivo especificado o está seleccionando un directorio")


def find_in_pdf(pdf_path, search_word):
    """This function gets a pdf and a word to search, when it founds the word in a page adds that
    page number to an array. When it finishes returns the array with the page numbers."""

    page_count = 1
    found_pages = []
    for page in extract_page_text(pdf_path):
        if searchText.search_text(page, search_word):
            found_pages.append(page_count)
        page_count += 1

    return found_pages

if __name__ == "__main__":
    import sys 
    if len(sys.argv) > 2:
        try:
            file_path = sys.argv[1]
            print(find_in_pdf(file_path, sys.argv[2]))
        except FileNotFoundError:
            print("File not found, check that the path is correct.")    
    else:
        print("The method needs two arguments, the path to the file and the word to search")