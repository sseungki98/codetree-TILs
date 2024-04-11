N, M, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
users = []
for _ in range(M):
    users.append(list(map(int, input().split())))

move_count = 0

exit = list(map(int, input().split()))
maps[exit[0]-1][exit[1]-1] = 'X'
for user in users:
    maps[user[0]-1][user[1]-1] = 'U'

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def getNewPosition():
    exit_x = -1
    exit_y = -1
    user_stack = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 'X':
                exit_x = i
                exit_y = j
            elif maps[i][j] == 'U':
                user_stack.append([i, j])
    
    return exit_x, exit_y, user_stack

def findSquare2():
    for k in range(2, N+1):
        for i in range(N):
            for j in range(N):
                user_flag = False
                exit_flag = False
                if i + k > N or j + k > N:
                    continue
                for n in range(k):
                    for m in range(k):
                        if maps[i+n][j+m] == 'X':
                            exit_flag = True
                        if maps[i+n][j+m] == 'U':
                            user_flag = True

                if user_flag and exit_flag:
                    return i, j, k


def moveMaze(left_top_x, left_top_y, size):
    temp_map = [arr[:] for arr in maps]
    size = size - 1
    
    for i in range(size+1):
        for j in range(size+1):
            if temp_map[left_top_x + i][left_top_y + j] in [0, 'U', 'X']:
                maps[left_top_x + j][left_top_y + size - i] = temp_map[left_top_x + i][left_top_y + j]
            else:
                maps[left_top_x + j][left_top_y + size - i] = temp_map[left_top_x + i][left_top_y + j] - 1

def moveUser():
    global move_count
    exit_x = -1
    exit_y = -1
    user_stack = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 'X':
                exit_x = i
                exit_y = j
            elif maps[i][j] == 'U':
                user_stack.append([i, j])

    for us in user_stack:
        i, j = us[0], us[1]
        dist = abs(exit_x - i) + abs(exit_y - j)
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            new_dist = abs(exit_x - x) + abs(exit_y - y)
            if 0<= x <N and 0<= y < N:
                if dist > new_dist:
                    if maps[x][y] == 0:
                        maps[x][y] = 'U'
                        maps[i][j] = 0
                        move_count += 1
                        break
                    elif maps[x][y] == 'X':
                        maps[i][j] = 0
                        move_count += 1
                        break
    # print('------')
    # for item in maps:
    #     print(item)
out_flag = False

for i in range(K):
    moveUser()
    l_x, l_y, size = findSquare2()
    moveMaze(l_x, l_y, size)
    exit_x, exit_y, users = getNewPosition()
    if len(users) == 0:
        print(move_count)
        print(exit_x+1, exit_y+1)
        out_flag = True
        break

if not out_flag:
    exit_x, exit_y, users = getNewPosition()
    print(move_count)
    print(exit_x+1, exit_y+1)