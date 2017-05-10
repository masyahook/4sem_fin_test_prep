n = int(input())
seq = input().split()
for i in range(n):
    for j in range((n - i) // 2):
        if seq[i + j] != seq[-1 - j]:
            break
    else:
        break
print(i)
if i != 0:
    print(' '.join(map(str, seq[:i][-1::-1])))
