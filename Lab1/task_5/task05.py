def zig_zag(rows, cols):

    zig_zag_matrix = []

    ################### TO DO #########################
    nr = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            if j == abs(nr):
                row.append(1)
            else:
                row.append(0)

        if nr == cols - 1:
            nr = -1 * (cols - 1)
        zig_zag_matrix.append(row)
        nr += 1


    ###################################################

    return zig_zag_matrix
