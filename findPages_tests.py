from pdfsearcher import findPages


#assert search_word_dir(PDF_PATH, "girl") == "[8, 15, 30]", "TEST ERROR - Should be [8, 15, 30]"
#TODO - Add Unitary tests for the app modules
assert findPages.find_in_pdf("../data", "girl") == [8, 15, 30], "TEST ERROR - Should be [8, 15, 30]"
#TODO - Main method to run unitary tests