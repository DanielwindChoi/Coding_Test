# 숫자 N은 아래와 같다.
# N=2a x 3b x 5c x 7d x 11e((a~e)는 지수다.)
# N이 주어질 때 a, b, c, d, e 를 출력하라.

# 간단한 소인수분해(?)
T = int(input())
for tc in range(1, T+1):
  # 입력으로 받은 N을 분해하는
  N = int(input()) 
  # 소인수 리스트를 만들고
  num = [2, 3, 5, 7, 11]
  # 나눠진 횟수를 담기 위한 빈 리스트도 생성
  count = [0, 0, 0, 0, 0]
  # 리스트 num을 돌면서(range로 한 이유는 같은 인덱스에 count리스트에도 횟수를 추가해주기 위해서)
  for n in range(len(num)):
    # 무한 루프를 주고
    while True:
      # 만약 N이 num의 n번째 숫자로 나눈 나머지가 0이라면
      if N % num[n] == 0:
        # N은 그 숫자로 나눈 몫으로 값을 바꾸고
        N = N/num[n]
        # count리스트의 같은 인덱스에 값을 +1
        count[n] += 1
      # 나눈 나머지가 0이 아니라면 멈추고 num의 다음 인덱스로 넘어감
      else:
        break # 빠져나오기 위해 pass나 countinue는 안되나? 확인해봐야겠다.
# 리스트컴프리헨션을 이용한 출력
# print('#{}.format(tc),''.join([str(_) for in count]))
# map함수는 str을 count의 모든 항목에 적용
  print('#{}'.format(tc), ' '.join(map(str, count)))


# 오답
# T = int(input())
# num = [2, 3, 5, 7, 11]
# count = [0, 0, 0, 0, 0]
# for i in num:
#     if i % 2 == 0:
#         count[0] += 1
#     elif i % 3 == 0:
#         count[1] += 1
#     elif i % 5 == 0:
#         count[2] += 1
#     elif i % 7 == 0:
#         count[3] += 1
#     elif i % 11 == 0:
#         count[4] += 1 
# print(count)   