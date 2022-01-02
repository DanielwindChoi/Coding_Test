T = int(input())

for t in range(T):
    n = list(map(int, input().split())) # map함수로 끝나는 게 아니라
    sum = 0                             # 리스트를 만들어줘야
    for i in n :
        if i > 0:
            sum += i

    average = int(round((sum)/len(n))) # len을 통해서 평균값을 계산할 수 있음 
    print(f'#{t+1} {average}')

# 오답, 간단한 문젠데 푸는데 너무 오래 걸린다ㅜㅜ
# T = int(input())

# for t in range(T):
#     n = list(map(int, input().split()))
#     sum = 0
#     for i in n :
#         if i > 0:
#             sum += i
#         average = (round(sum))/len(n, 0)

# print({} {}.format{#(i+1)} {rount(average, .*)})
# format을 사용하는 것이 익숙치 않아서 f string으로 풀었다.

