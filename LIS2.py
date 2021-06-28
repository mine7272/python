'''
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

1.비어있는 리스트 하나 선언
2.주어진 리스트를 차례대로 읽으면서 다음 작업 실행
    1) 만든 리스트의 마지막 원소가 읽은 값보다 작은 경우
        읽은 값을 리스트의 맨 뒤에다 추가.
    2) 그렇지 않으면
        리스트에서 읽은값을 끼워넣기 할 위치를 찾고, 해당 위치에 읽은 값을 덮어씀.
'''
from bisect import bisect_left

size=int(input())
s= tuple(map(int,input().split()))
seq=[s[0]]

for i in range(1,size):
    if seq[-1]<s[i]:
        seq.append(s[i])
    else:
        index=bisect_left(seq, s[i])
        seq[index]=s[i]

print(len(seq))