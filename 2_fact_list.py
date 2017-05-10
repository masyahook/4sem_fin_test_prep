x = int(input())
fact = 1
i = 1
fact_list = []
while fact <= x:
    fact_list.append(fact)
    i += 1
    fact *= i
print(' '.join(map(str, fact_list)))
