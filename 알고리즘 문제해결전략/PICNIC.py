# 재귀적으로 호출되면서 짝을 찾는 함수
# students : 남아있는 학생
# friendsMap[k] : k의 짝이 될 수 있는 친구의 리스트

def PairFind(students, friendsMap):
    if len(students) == 0:          # 끝까지 탐색한 경우 1을 리턴
        return 1
    st = students.pop(0)
    count = 0
    for f in friendsMap[st]:        # 이 학생과 짝을 할 수 있는 친구들을 배제하고 재귀 호출
        if f in students:           # 이미 짝을 이룬 학생은 제외
            tmp = students[::]      # 재귀의 정상적인 동작을 위해 집합을 복사
            tmp.remove(f)           # 이 학생과 짝을 지어주고 남은 학생에서 배제
            count += PairFind(tmp, friendsMap) # 재귀호출, 리턴값 저장
    return count


# MAIN
for T in range(int(input())):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    friendsMap = [[] for i in range(n)]
    for i in range(m):
        if tmp[i*2] > tmp[i*2+1]:
            friendsMap[tmp[i*2+1]].append(tmp[i*2])
        else: friendsMap[tmp[i*2]].append(tmp[i*2+1])
    for i in range(len(friendsMap)):
        friendsMap[i] = sorted(friendsMap[i])
    print(PairFind(list(range(n)), friendsMap))

