# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
# ”YYYY/MM/DD”형식으로 출력
# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램
# 31일 : 1, 3, 5, 7, 8, 10, 12월
# 30일 : 4, 6, 9, 11월
# 28일 : 2월 

T = int(input())
for calendar in range(T):
    Date = input()
    month = int(Date[4:6])
    day = int(Date[6:]) 
    if month in (1, 3, 5, 7, 8, 10, 12): 
        if day <= 31:
            print(f'#{calendar+1} {Date[:4]}/{Date[4:6]}/{Date[6:]}')
        else:
            print(f'#{calendar+1} -1')
    elif month in (4, 6, 9, 11): 
        if day <= 30:
            print(f'#{calendar+1} {Date[:4]}/{Date[4:6]}/{Date[6:]}')
        else:
            print(f'#{calendar+1} -1')
    # elif month in (2,): (2)라고 쓰면 int로 인식해서 에러가 난다.
    elif month == 2: 
        if day <= 28:
            print(f'#{calendar+1} {Date[:4]}/{Date[4:6]}/{Date[6:]}')
        else:
            print(f'#{calendar+1} -1')
    else:
       print(f'#{calendar+1} -1')          


# 오답
# T = int(input())
# for t in range(T):
#     Date = input()
#     month = int(Date[4:6])
#     day = int(Date[7:9]) 
#     for i in range(1,13):
#         if i in month:
#             pass
#         else:
#             print(-1)
#         if 2 in month:
#             if day <= 28:
#                 pass
#             else:
#                 print(-1)