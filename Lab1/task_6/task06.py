def func(size):
    
    romb = ""
    size = size + 2 + (size+1) % 2  #adjust size for easier use
    ################### TO DO #########################

    puncte = ""
    spatii = ""
    for i in range(size//2):
        spatii += " "
        puncte += ".." #point and space vector for string slicing
    for i in range(size//2):
        romb += spatii[:size//2-1-i] + "@" + puncte[:-2*(size//2) + 2*i] + "@\n"
    for i in range(size//2-2, -1, -1):
        romb += spatii[:size//2-1-i] + "@" + puncte[:-2*(size//2) + 2*i] + "@\n"

    ###################################################

    return romb
