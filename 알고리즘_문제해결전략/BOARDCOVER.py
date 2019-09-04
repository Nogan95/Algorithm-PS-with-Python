from copy import deepcopy       # 재귀 인자로 2차원 배열을 넘기기 때문에 깊은 복사가 필요하다.
def BoardCover(H, W, curMap, x, y):
    global count                # curMap : 현재 맵 상태, x:세로좌표(상-> 하)  y:가로좌표(좌->우)
    if y == W:
        y = 0; x += 1
    if x == H-1:                # 마지막 직전줄 까지 끝났다면
        for k in range(W):      # 마지막 줄이 전부 채워졌는지 확인하고
            if curMap[H-1][k]:
                return
        count += 1              # 그렇다면 카운트에 1을 더해준다.
        return
    if not curMap[x][y]:        # 현재 좌표가 빈칸이 아니면 다음 좌표로 이동
        BoardCover(H, W, curMap, x, y + 1)
    else:                       # 현재 좌표가 빈칸이라면 4가지 경우의 수를 확인 후 재귀 호출
        if y < W-1: # 오버플로 방지
            if curMap[x][y+1] and curMap[x+1][y+1]:
                newMap = deepcopy(curMap)
                newMap[x][y], newMap[x][y+1], newMap[x+1][y+1] = False, False, False
                BoardCover(H,W,newMap,x,y+1)
            if curMap[x][y+1] and curMap[x+1][y]:
                newMap = deepcopy(curMap)
                newMap[x][y] ,newMap[x][y+1], newMap[x+1][y] = False, False, False
                BoardCover(H,W,newMap,x,y+1)
            if curMap[x+1][y] and curMap[x+1][y+1]:
                newMap = deepcopy(curMap)
                newMap[x][y], newMap[x+1][y], newMap[x+1][y+1] = False, False, False
                BoardCover(H,W,newMap,x,y+1)
        if y > 0: # 오버 플로 방지
            if curMap[x+1][y] and curMap[x+1][y-1]:
                newMap = deepcopy(curMap)
                newMap[x][y], newMap[x+1][y], newMap[x+1][y-1] = False, False, False
                BoardCover(H,W,newMap,x,y+1)


# Main
for n in range(int(input())):
    H, W = map(int, input().split())
    totalMap = [list(map(lambda x: True if x == '.' else False, input()[:W])) for i in range(H)]
    # totalMap : 2차원 배열 형태로 입력을 받고 #을 False로 .을 True로 입력받음
    count = 0
    BoardCover(H,W, totalMap, 0, 0)
    print(count)