def createAux(W):
    # initializing the array aux with 0's
    aux = [0] * len(W)

    # for index 0, it will always be 0
    # so starting from index 1
    i = 1
    # m can also be viewed as index of first mismatch
    m = 0
    while i < len(W):
        # prefix = suffix till m-1
        if W[i] == W[m]:
            m += 1
            aux[i] = m
            i += 1
        # this one is a little tricky,
        # when there is a mismatch,
        # we will check the index of previous
        # possible prefix.
        elif W[i] != W[m] and m != 0:
            # Note that we do not increment i here.
            m = aux[m-1]
        else:
            # m = 0, we move to the next letter,
            # there was no any prefix found which
            # is equal to the suffix for index i
            aux[i] = 0
            i += 1

    return aux

txt = "ABCABABB"
x = createAux(txt)
print(x)
# This code is contributed by Bhavya Jain