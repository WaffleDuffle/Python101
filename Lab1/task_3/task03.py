
def func(string_message):
    """ 
    Puneti rezultatul codificarii mesajului in "encoded_message"

    HINT!
    chr() si ord() sunt functii implicite care "jongleaza" cu caracterele
    ASCII si codificarile lor. Astfel, daca pentru litera 'A', avem codificarea
    65, iar pentru 'B' avem 66, atunci:
    
    chr(65) = 'A'   ||   chr(66) = 'B'  
    ord('A') = 65   ||   ord('B') = 66

    ANOTHER HINT!
    Poti folosi dictionarele.
    """
    
    encoded_message = ""
    ################### TO DO #########################

    for i in string_message:
        if i == " ":
            encoded_message += '0'
        else:
            encoded_message += str(ord(i) - ord('A') + 1)



    ###################################################

    return encoded_message