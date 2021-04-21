
def search_text(text, tosearch_string):
    """This function gets a text and a string to search, if the string appears in the 
    text it returns True."""

    index = text.lower().find(tosearch_string.lower())
    if index>=0:
        return True
    else:
        return False