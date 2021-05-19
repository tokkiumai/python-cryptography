def m(seed, taps):
    sr, xor = seed, 0
    while 1:
        for t in taps:
            xor += int(sr[t - 1])
        if xor % 2 == 0.0:
            xor = 0
        else:
            xor = 1
        sr, xor = str(xor) + sr[:-1], 0
        yield sr
        if sr == seed:
            break


for state in m('11001001', (8, 7, 6, 1)):
    print(state[0])  # the xor value
    print(state)  # the sr value
