import time
# https://www.programiz.com/python-programming/time
# https://docs.python.org/3/library/time.html

goal = [['1','2','3'],['4','5','6'],['7','8','0']]
coord = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]] # coordinates of the goal state

nodesExp = 0 #everytime we append to queue add 1
qSize = 0 #everytime append add 1; everytime pop subtract 1
max = 0 #compare with max to track biggest queue size

def main():
    puzzle = chooseBoard()
    chooseSearch(puzzle)


#which board does the user want to solve
def chooseBoard():
    boardNumber = input("Choose the board that you would like to solve(0-7) or choose '8' to create your own: ")
    while boardNumber != '0' and boardNumber != '1' and boardNumber != '2' and boardNumber != '3' and boardNumber != '4' and boardNumber != '5' and boardNumber != '6' and boardNumber != '7' and boardNumber != '8':
        print("Try again")
        boardNumber = input("Choose the board that you would like to solve(0-7) or choose '8' to create your own: ")

    if boardNumber == '0':
        board = [['1','2','3'],['4','5','6'],['7','8','0']] #depth 0
    elif boardNumber == '1':
        board = [['1','2','3'],['4','5','6'],['0','7','8']] #depth 2
    elif boardNumber == '2':
        board = [['1','2','3'],['5','8','6'],['4','7','0']] #depth 4
    elif boardNumber == '3':
        board = [['1','3','6'],['5','8','2'],['4','7','0']] #depth 8
    elif boardNumber == '4':
        board = [['1','3','6'],['5','0','7'],['4','8','2']] #depth 12
    elif boardNumber == '5':
        board = [['1','6','7'],['5','0','3'],['4','8','2']] #depth 16
    elif boardNumber == '6':
        board = [['7','1','2'],['4','8','5'],['6','3','0']] #depth 20
    elif boardNumber == '7':
        board = [['0','7','2'],['4','6','1'],['3','5','8']] #depth 24
    elif boardNumber == '8':
        customRow1 = input("Enter row 1 with spaces in between each number: ")
        customRow2 = input("Enter row 2 with spaces in between each number: ")
        customRow3 = input("Enter row 3 with spaces in between each number: ")

        customRow1 = (customRow1.split())
        customRow2 = (customRow2.split())
        customRow3 = (customRow3.split())

        board = [customRow1, customRow2, customRow3]
    printBoard(board)
    return board


def chooseSearch(board):
    search = input('Which search would you like to implement?\n1: Uniform Search\n2: Manhattan Search\n3: Tile Search\nInput: ')
    while search != '1' and search != '2' and search != '3':
        print('Try again')
        search = input('Which search would you like to implement?\n1: Uniform Search\n2: Manhattan Search\n3: Tile Search\nInput: ')
    if search == '1':
        print('Uniform Search')
        return UniformSearch(board, goal)
    elif search == '2':
        print('Manhattan Search')
        return ManhattanSearch(board, goal)
    elif search == '3':
        print('TileSearch')
        return TileSearch(board, goal)


def printBoard(board):
    for i in range(0,3):
        for y in range(0,3):
            print(board[i][y], end = ' ')
        print('')


#gets the different ways that the blank can move
def getChildren(board):
    print('hi')


#Breadth First Search - A* g(n) + h(n) where h(n) = 0
def UniformSearch(board,goal):
    depth = 0
    queue = [board]
    done = [board]
    while len(queue) > 0:
        node = queue.pop()
        if(node == goal):
            printBoard(node)
            print('Goal State!')
            print('Solution Depth was ' + depth)
            print('Number of nodes expanded: ' + nodesExp)
            print('Max queue size: ' + qSize)
            return node
        else:
            queue.append(getChildren(node))
    return None
    

def ManhattanSearch(board, goal):
    depth = 0
    queue = [board] #of states
    alg = []   #of sum of algorithms
    done = [board]
    #calculate the h(n)
    while len(queue) > 0:
        node = queue.pop()
        manhattan = 0
        for i in range(0,3):
            for j in range(0,3):
                if node[i][j] != goal[i][j] and node[i][j] != '0':
                    value = int(node[i][j])
                    manhattan += (abs(i-coord[value-1][0]) + abs(j-coord[value-1][1]))
        print(manhattan)
        alg.append(depth + manhattan)
    print('The best state to expand with a g(n) = 3 and h(n) = 0 is: ')

def TileSearch(board, goal):
    depth = 0
    queue3 = [board]
    alg = [0]   #of sum of algorithms
    done3 = [board]
    #calculate h(n)
    misplaced = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] != goal[i][j]:
                misplaced +=1
    if(board[2][2] != '0'):
        misplaced -=1
    print(misplaced)
    print('The best state to expand with a g(n) = 3 and h(n) = 0 is: ')

if __name__ == "__main__":
    main()
