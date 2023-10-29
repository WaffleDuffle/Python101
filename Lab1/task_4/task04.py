def func(given_numbers):
    ################### TO DO #########################

    # Completeaza doar linia urmatoare
    nice_list = [(i ** 1, i ** 2, i ** 3) for i in given_numbers if i < 100 and (i % 2 == 0 or i % 3 == 0)]

    ###################################################

    return nice_list
