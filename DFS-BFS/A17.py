# 경쟁적 전염

from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n): # 맵정보 입력
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] != 0 :
      data.append((graph[i][j],0,i,j))
    
data.sort() # 낮은 번호부터 증식하기 때문에 정열 후 큐로 옮기기
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while q:
  virus, s, x, y = q.popleft()
  if s == target_s : #큐가 비거나 s초가 될때까지 반복
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx and nx<n and 0<=ny and ny<n:
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus, s+1, nx,ny))

print(graph[target_x -1][target_y -1])