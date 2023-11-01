def task(*args):
    '''
    args -> elemente de tipuri diferite
    return -> lista cu elementele corespunzatoare
    '''

    result = []

    ################### TO DO #########################

    #functional approach

    func = lambda x: type(x) == int or (type(x) == str and x not in "aeiou" and x >= "a" and x <= "z" and len(x) == 1)
    result = list(filter(func, args))


    ###################################################
    
    return result
