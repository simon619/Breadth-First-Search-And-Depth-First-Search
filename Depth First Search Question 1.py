adj = []
with open('input.txt') as textfile:
    for line in textfile:
        adj_row = [item.strip() for item in line.split(' ')]
        adj.append(adj_row)

print(adj)
# N N N Y Y N N
# N Y N N Y Y N
# Y Y N Y N N Y
# N N N N N Y N
# Y Y N N N N N
# N N N Y N N N

col = len(adj[0])
row = len(adj)
print('Row = %d' % row)
print('Column = %d' % col)


def stringify(i, j):
    s = ''
    s = s + str(i) + str(j)
    return s


visited = []
stack = []
count = 0
maximum = []


def find_your_mates(i, j):
    global count
    if 1 <= i <= row - 2 and 1 <= j <= col - 2:
        if adj[i - 1][j - 1] == 'Y':
            check = stringify(i - 1, j - 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i - 1][j + 1] == 'Y':
            check = stringify(i - 1, j + 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i][j - 1] == 'Y':
            check = stringify(i, j - 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i - 1][j] == 'Y':
            check = stringify(i - 1, j)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i][j + 1] == 'Y':
            check = stringify(i, j + 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i + 1][j - 1] == 'Y':
            check = stringify(i + 1, j - 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i + 1][j] == 'Y':
            check = stringify(i + 1, j)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i + 1][j + 1] == 'Y':
            check = stringify(i + 1, j + 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

    if (i, j) == (0, 0):
        if adj[i][j + 1] == 'Y':
            check = stringify(i, j + 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1

        if adj[i + 1][j + 1] == 'Y':
            check = stringify(i + 1, j + 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i + 1][j] == 'Y':
            check = stringify(i + 1, j)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

    if i == 0 and j == col - 1:
        if adj[i][j - 1] == 'Y':
            check = stringify(i, j - 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i + 1][j - 1] == 'Y':
            check = stringify(i + 1, j - 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i + 1][j] == 'Y':
            check = stringify(i + 1, j)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

    if i == 0 and (1 <= j <= col - 2):
        if adj[i][j - 1] == 'Y':
            check = stringify(i, j - 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i][j + 1] == 'Y':
            check = stringify(i, j + 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i + 1][j - 1] == 'Y':
            check = stringify(i + 1, j - 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i + 1][j] == 'Y':
            check = stringify(i + 1, j)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i + 1][j + 1] == 'Y':
            check = stringify(i + 1, j + 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

    if i == row - 1 and (1 <= j <= col - 2):
        if adj[i - 1][j - 1] == 'Y':
            check = stringify(i - 1, j - 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i - 1][j + 1] == 'Y':
            check = stringify(i - 1, j + 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i][j - 1] == 'Y':
            check = stringify(i, j - 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i - 1][j] == 'Y':
            check = stringify(i - 1, j)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i][j + 1] == 'Y':
            check = stringify(i, j + 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

    if i == row - 1 and j == 0:
        if adj[i - 1][j] == 'Y':
            check = stringify(i - 1, j)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i - 1][j + 1] == 'Y':
            check = stringify(i - 1, j + 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i][j + 1] == 'Y':
            check = stringify(i, j + 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

    if i == row - 1 and j <= col - 1:
        if adj[i - 1][j - 1] == 'Y':
            check = stringify(i - 1, j - 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i - 1][j] == 'Y':
            check = stringify(i - 1, j)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i][j - 1] == 'Y':
            check = stringify(i, j - 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

    if (1 <= i <= row - 2) and j == 0:
        if adj[i - 1][j] == 'Y':
            check = stringify(i - 1, j)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i - 1][j + 1] == 'Y':
            check = stringify(i - 1, j + 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i][j + 1] == 'Y':
            check = stringify(i, j + 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i + 1][j] == 'Y':
            check = stringify(i + 1, j)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i + 1][j + 1] == 'Y':
            check = stringify(i + 1, j + 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

    if (1 <= i <= row - 2) and j == col - 1:
        if adj[i - 1][j] == 'Y':
            check = stringify(i - 1, j)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i - 1][j - 1] == 'Y':
            check = stringify(i - 1, j - 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i][j - 1] == 'Y':
            check = stringify(i, j - 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i + 1][j] == 'Y':
            check = stringify(i + 1, j)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

        if adj[i + 1][j - 1] == 'Y':
            check = stringify(i + 1, j - 1)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
            else:
                pass

    print('visited => %s' % visited)
    print('Stacked => %s' % stack)
    if len(stack) != 0:
        x = stack.pop()
        w = list(x)
        p = int(w[0])
        q = int(w[1])
        find_your_mates(p, q)

    else:
        maximum.append(count)
        if count > 1:
            print("Output: Affected People in This Cluster Is %d" % count)
        else:
            print('Output: Only one person gets infected')
        count = 0


m = 0
while m < len(adj):
    for n in range(len(adj[m])):
        if adj[m][n] == 'Y':
            check = stringify(m, n)
            if check not in visited:
                visited.append(check)
                stack.append(check)
                count += 1
                find_your_mates(m, n)
            else:
                pass
        else:
            pass
    m += 1
print("Output: Highest Infected Region Has %d People Infected" % max(maximum))
