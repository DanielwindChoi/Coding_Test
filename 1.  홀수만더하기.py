T = int(input())

for t in range(T): # range의 범위를 1부터 잡지 않아도 된다.
    n = map(int, input().split())
    sum = 0
    for i in n:
        if i % 2 != 0:
            sum += i
    print(f'#{t+1}', str(sum))
    # range의 범위를 1부터 잡지 않았으니 t+1을 해줘야 한다.