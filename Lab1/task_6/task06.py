def func(size):

    romb = ""
    size += 2
    ################### TO DO #########################
    if size % 2 == 0:
        size += 1
    puncte = ""
    spatii = ""
    for i in range(size//2):
        spatii += " "
        puncte += ".."
    for i in range(size//2):
        romb += spatii[:size//2-1-i] + "@" + puncte[:-2*(size//2) + 2*i] + "@\n"
    for i in range(size//2-2, -1, -1):
        romb += spatii[:size//2-1-i] + "@" + puncte[:-2*(size//2) + 2*i] + "@\n"

    ###################################################

    return romb