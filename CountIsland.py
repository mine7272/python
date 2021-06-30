'''
• 1은 섬을 의미하고 0은 바다를 의미합니다. 섬은 가로와 세로로 이어진 경우 같은
섬이라고 판단합니다. 대각선으로 이어진 경우는 같은 섬이 아닐 수 있습니다.
• 지도를 표시할 수 있는 n, m을 입력받으면 n개의 줄에 m개의 문자가 있는 줄이
표시됩니다. 이때, 지도에 있는 섬의 개수를 구하는 프로그램을 작성합니다. (지도밖은
모두 바다입니다.) 참고 : https://www.acmicpc.net/problem/4963
'''

def dfs(mapk, visit, y, k):
    visit[y][x] = True
    n = len(mapk)
    m = len(mapk[0])
    dxy = ( (0, 1), (1, 0), (0, -1), (-1, 0) ) 
    for k in dxy:
        ny = y + k[0]
        nx = x + k[1]
        if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
        if visit[ny][nx] == True or mapk[ny][nx] == 0: continue
        dfs(mapk, visit, ny, nx)


def bfs(mapk, visit, y, x):
    q = [ (y, x) ]
    n = len(mapk)
    m = len(mapk[0])
    dxy = ( (0, 1), (1, 0), (0, -1), (-1, 0) )
    while not len(q) == 0:
        u = q.pop(0)
        visit[u[0]][u[1]] = True
        for k in dxy:
            ny = u[0] + k[0]
            nx = u[1] + k[1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            if visit[ny][nx] == True or mapk[ny][nx] == 0: continue
            q.append((ny, nx))



#입력받기
n,m=map(int,input().split())
mapk=[ ]
for i in range(n):
    line=[ ]
    s=input()#라인 입력받기
    for k in s: #문자열이기 때문에 나열형으로 들어감
        if k == '1' : line.append(1)
        else: line.append(0)
    mapk.append(line) 

#해당 정점을 방문했는지 여부
visit=[[False]*m for _ in range(n)] #리스트내포 사용해서 방문여부 리스트 만들기
island=0

for y in range(n):
    for x in range(m):
        if visit[y][x] ==False and mapk[y][x]==1:
            island+=1
            bfs(mapk, visit, y, x)

print(island)