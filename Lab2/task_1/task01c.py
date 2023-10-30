def task1c(words):
    '''
    words -> lista string-uri
    return -> lista string-uri

    Salvati cuvintele care sunt palindrom in "palindromes"
    '''

    palindromes = []

    ################### TO DO #########################
    palindrom = lambda string: string == string[::-1]
    palindromes = filter(palindrom, words)

    ###################################################

    # Nu modificati valoarea de retur a functiei
    return list(palindromes)
