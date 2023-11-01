def task(register):
    '''
    register -> dictionar
    return -> lista doar cu numele studentilor
    '''
    names = []

    ################### TO DO #########################
    
    #procedual approach
    # def avg(list):
    #     return float(sum(list)/len(list))
    # names = [key for key, value in register.items() if avg(value) >= 8.5]
    
    #functional approach

    #print(register)
    
    medie = lambda key: float(sum(register[key])/len(register[key])) >= 8.5
    names = list(filter(medie, register.keys()))
    
    #print(names)
    ###################################################
    
    return names
