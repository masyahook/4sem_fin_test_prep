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
        l_bound, r_bound = i - cur, i + cur
        while l_bound >= 0 and r_bound < len_seq and seq[l_bound] == seq[r_bound]:
            cur += 1
            l_bound -= 1
            r_bound += 1
        pals[i] = cur
        possible_rightest = cur - 1 + i
        if possible_rightest > rightest:
            rightest, pos = possible_rightest, i
    return [2 * x - 1 for x in pals]

print(' '.join(map(str, max_pal(input()))))
