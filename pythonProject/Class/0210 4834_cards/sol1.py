'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
# 0. T = tc의 개수, N = 카드 장수 numbers = 숫자
for tc in range(1, T + 1):
    N= int(input())
    numbers = list(map(int, input()))
    # print(numbers)
    cards = [0] * 50

    # number에서 나온 수를 1씩 더함.
    for num in numbers:
        cards[num] += 1
    #print(cards)

    # 가장 큰 수 찾기
    maxnum = cards[0]
    max_i= 0
    for i in range(50):
        # 내가 놓쳤던 부분 tc2번 일때는 <=를 해줘야 마지막 인덱스가 들어간다.
        if maxnum <= cards[i]:
            maxnum = cards[i]
            max_i = i
    print(f'#{tc} {max_i} {maxnum}')