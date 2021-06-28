def perm(v,r,s=[]): #s는 v의 배열을 가지고 r개 묶은 결과
    if r==0: #탈출조건
        print(s)
        return
    for x in v: #리스트에 이미 값이 존재한다면
        if x in s : continue #성능에 문제가 생길 수 있음
        perm(v,r-1,s+[x]) #그렇지않으면 원소 하나 줄이고(r개만 더 넣자) 재귀 s배열에 원소를 집어넣음

v=["홍길동","성춘향","이몽룡"]
r=2
perm(v,r)