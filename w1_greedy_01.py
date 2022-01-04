
'''
#이건 내가 오름차순으로 한 풀이
x.sort()
cnt=0
i=0
member_num=0

while i<n:
    member_num+=1
    if member_num>=x[i]: # 인덱스 번호 쓰는 것보다는 밑에처럼 바로 for 문 돌리면서 뽑아쓰자.
        cnt+=1
        member_num=0
    i+=1

print(cnt)
'''
import sys
sys.stdin=open("input.txt", "r")
input=sys.stdin.readline

n=int(input())
data=list(map(int, input().split()))
data.sort()

result=0 # 총 그룹의 수
count=0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count+=1 # 현재 그룹에 해당 모험가를 포함시키기
    if count>=i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result+=1 # 총 그룹의 수 증가시키기
        count=0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result)

