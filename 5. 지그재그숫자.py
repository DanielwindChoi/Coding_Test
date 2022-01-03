T = int(input()) 

for i in range(1, T+1): # 1에서 T까지의 리스트 중에서
    N = int(input()) # N값이 입력되면

    sum = 1
    for i in range(2,N+1): # 2부터 N까지의 리스트 중에서
        if i%2 == 0 : # 2로 나눠떨어지는 짝수는 
            sum -= i # sum에서 그 값을 빼주고 
        else : # 홀수인 경우
            sum += i # 더해줘라

print(f'#(t, sum)') # 그 결과 값을 f string으로 출력
