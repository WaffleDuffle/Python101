def func(nume_complete):
    """
    Creeaza un tuplu "nume_formatat" care sa contina 3 elemente:
    nume_formatat[0] = lista cu numele de familie
    nume_formatat[1] = lista cu primele prenume
    nume_formatat[2] = lista cu celelalte prenume

    HINT!  conversie string - lista || (string.split("delimiter"))
    """


    ################### TO DO #########################

    nume_lista = []
    prenume1_lista = []
    prenume2_lista = []
    for element in nume_complete:
        nume = element.split(" ")
        nume_lista.append(nume[0])
        prenume = nume[1].split("-")
        prenume1_lista.append(prenume[0])
        prenume2_lista.append(prenume[1])
    nume_formatat = (nume_lista, prenume1_lista, prenume2_lista)


    ###################################################

    return nume_formatat

    