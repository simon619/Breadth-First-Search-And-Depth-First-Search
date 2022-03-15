adj = []
with open('Question2 input2.txt') as textfile:
    for line in textfile:
        adj_row = [item.strip() for item in line.split(' ')]
        adj.append(adj_row)

print(adj)
# A H T H
# H H T A
# T T H H
# A H T H
# H T H H

col = len(adj[0])
row = len(adj)
print('Row = %d' % row)
print('Column = %d' % col)


def stringify(i, j):
    s = ''
    s = s + str(i) + str(j)
    return s


visited = []
queue = [[], []]
time = 0


def arrival():
    global time
    v = 0
    while queue:
        print('%d Generation Aliens Invading: %s' %(time + 1, queue))
        x = queue[v].pop(0)
        l = list(x)
        r, s = (int(l[0]), int(l[1]))
        invasion(r, s, v + 1)

        if len(queue[v]) == 0:
            if len(queue[v]) == 0 and len(queue[v + 1]) == 0:
                queue.pop(0)
                queue.pop(0)

            else:
                queue.append([])
                queue.pop(0)
                time += 1
                print('%d minute After Invasion Scenario:' % time)


def invasion(i, j, k):
    if 1 <= i <= row - 2 and 1 <= j <= col - 2:
        if adj[i][j - 1] == 'H':
            check = stringify(i, j - 1)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i][j - 1] = 'A'
            else:
                pass

        if adj[i][j + 1] == 'H':
            check = stringify(i, j + 1)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i][j + 1] = 'A'
            else:
                pass

        if adj[i + 1][j] == 'H':
            check = stringify(i + 1, j)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i + 1][j] = 'A'
            else:
                pass

        if adj[i - 1][j] == 'H':
            check = stringify(i - 1, j)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i - 1][j] = 'A'
            else:
                pass

    if (i, j) == (0, 0):
        if adj[i][j + 1] == 'H':
            check = stringify(i, j + 1)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i][j + 1] = 'A'
            else:
                pass

        if adj[i + 1][j] == 'H':
            check = stringify(i + 1, j)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i + 1][j] = 'A'
            else:
                pass

    if (i, j) == (0, col - 1):
        if adj[i][j - 1] == 'H':
            check = stringify(i, j - 1)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i][j - 1] = 'A'
            else:
                pass

        if adj[i + 1][j] == 'H':
            check = stringify(i + 1, j)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i + 1][j] = 'A'
            else:
                pass

    if (i, j) == (row - 1, 0):
        if adj[i][j + 1] == 'H':
            check = stringify(i, j + 1)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i][j + 1] = 'A'
            else:
                pass

        if adj[i - 1][j] == 'H':
            check = stringify(i - 1, j)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i - 1][j] = 'A'
            else:
                pass

    if (i, j) == (row - 1, col - 1):
        if adj[i][j - 1] == 'H':
            check = stringify(i, j - 1)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i][j - 1] = 'A'
            else:
                pass

        if adj[i - 1][j] == 'H':
            check = stringify(i - 1, j)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i - 1][j] = 'A'
            else:
                pass

    if 1 <= i <= row - 2 and j == 0:
        if adj[i][j + 1] == 'H':
            check = stringify(i, j + 1)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i][j + 1] = 'A'
            else:
                pass

        if adj[i + 1][j] == 'H':
            check = stringify(i + 1, j)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i + 1][j] = 'A'
            else:
                pass

        if adj[i - 1][j] == 'H':
            check = stringify(i - 1, j)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i - 1][j] = 'A'
            else:
                pass

    if 1 <= i <= row - 2 and j == col - 1:
        if adj[i][j - 1] == 'H':
            check = stringify(i, j - 1)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i][j - 1] = 'A'
            else:
                pass

        if adj[i + 1][j] == 'H':
            check = stringify(i + 1, j)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i + 1][j] = 'A'
            else:
                pass

        if adj[i - 1][j] == 'H':
            check = stringify(i - 1, j)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i - 1][j] = 'A'
            else:
                pass

    if i == 0 and 1 <= j <= col - 2:
        if adj[i][j - 1] == 'H':
            check = stringify(i, j - 1)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i][j - 1] = 'A'
            else:
                pass

        if adj[i + 1][j] == 'H':
            check = stringify(i + 1, j)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i + 1][j] = 'A'
            else:
                pass

        if adj[i][j + 1] == 'H':
            check = stringify(i, j + 1)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i][j + 1] = 'A'
            else:
                pass

    if i == row - 1 and 1 <= j <= col - 2:
        if adj[i][j - 1] == 'H':
            check = stringify(i, j - 1)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i][j - 1] = 'A'
            else:
                pass

        if adj[i - 1][j] == 'H':
            check = stringify(i - 1, j)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i - 1][j] = 'A'
            else:
                pass

        if adj[i][j + 1] == 'H':
            check = stringify(i, j + 1)
            if check not in visited:
                queue[k].append(check)
                visited.append(check)
                adj[i][j + 1] = 'A'
            else:
                pass


def census():
    alien_counter = 0
    human_counter = 0
    p = 0
    while p < len(adj):
        for q in range(len(adj[p])):
            if adj[p][q] == 'A':
                alien_counter += 1
                check = stringify(p, q)
                if check not in visited:
                    visited.append(check)
                    queue[0].append(check)
                else:
                    pass

            if adj[p][q] == 'H':
                human_counter += 1

            else:
                pass

        p += 1

    print('Number of Humans is %d' % human_counter)
    print('Number of Aliens is %d' % alien_counter)


census()
print('%d minute After Invasion Scenario:' % time)
arrival()
census()
print('Time: %d Minutes' % time)
