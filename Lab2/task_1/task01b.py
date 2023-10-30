def task1b(phrase):
    '''
    phrase -> string
    return -> string

    Transformati in litere mari vocalele din fraza
    si salvati rezultatul in "new_phrase"
    '''

    new_phrase = ""

    ################### TO DO #########################

    upper = lambda x: x.upper() if x in "aeiou" else x
    new_phrase = map(upper, phrase)
    ###################################################

    # Nu modificati valoarea de retur a functiei
    return ''.join(list(new_phrase))
