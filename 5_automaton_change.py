n = int(input())
sales = list(map(int, input().split()))
balance = min_balance = 0
for i in range(n):
    if sales[i] == 5:
        balance += 5
    else:
        balance -= sales[i] - 5
    if balance < min_balance:
        min_balance = balance
print(-min_balance // 5)
