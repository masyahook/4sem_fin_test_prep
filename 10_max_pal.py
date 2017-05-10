def max_pal(seq):
    len_seq = len(seq)
    pals = [1] * len_seq
    rightest, pos = 0, 0
    for i in range(len_seq):
        if i <= rightest + pos:
            j = 2 * pos - i
        else:
            j = i
        cur = pals[j]
        while i - cur >= 0 and i + cur < len_seq and seq[i - cur] == seq[i + cur]:
            cur += 1
        pals[i] = cur
    return [(x - 1) * 2 + 1 for x in pals]

print(' '.join(map(str, max_pal(input()))))
