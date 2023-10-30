def task1a(nums):
    '''
    nums -> vector int
    return -> vector int

    Dublati elementele care se divid cu 6, iar pe cele 
    care nu se divid, triplati-le folosind functionale
    '''

    result = []
    func = lambda x: x * 2 if x % 6 == 0 else x * 3

    ################### TO DO #########################
    result = map(func, nums)


    ###################################################

    # Nu modificati valoarea de retur a functiei
    return list(result)
