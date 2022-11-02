import time
import copy
# https://www.programiz.com/python-programming/time
# https://docs.python.org/3/library/time.html
# https://docs.python.org/3/tutorial/classes.html
# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/

#create Node class
class Node:
    def __init__(self, state):
        self.child0 = None # blank moves up
        self.child1 = None #blank moves down
        self.child2 = None #blank moves left
        self.child3 = None #blank moves right
        self.depth = 0 #depth node is at
        self.cost = 0 #cost to get to node/estimated cost to get to goal
        self.state = state

goal = [['1','2','3'],['4','5','6'],['7','8','0']]
coord = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]] # coordinates of the goal state




def main():
    problem = chooseBoard()
    search = chooseSearch(problem)
    UniformSearch(problem, search)


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
        board = [['1','2','3'],['5','0','6'],['4','7','8']] #depth 4
    elif boardNumber == '3':
        board = [['1','3','6'],['5','0','2'],['4','7','8']] #depth 8
    elif boardNumber == '4':
        board = [['1','3','6'],['5','0','7'],['4','8','2']] #depth 12
    elif boardNumber == '5':
        board = [['1','6','7'],['5','0','3'],['4','8','2']] #depth 16
    elif boardNumber == '6':
        board = [['7','1','2'],['4','8','5'],['6','3','0']] #depth 20
    elif boardNumber == '7':
        board = [['0','7','2'],['4','6','1'],['3','5','8']] #depth 24
    #create custom board   
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


#user chooses which search to do
# 1 - Uniform, 2 - Manhatten, 3 - Misplaced
def chooseSearch(board):
    search = input('Which search would you like to implement?\n1: Uniform Search\n2: Manhattan Search\n3: Tile Search\nInput: ')
    #while invalid input
    while search != '1' and search != '2' and search != '3':
        print('Try again')
        search = input('Which search would you like to implement?\n1: Uniform Search\n2: Manhattan Search\n3: Tile Search\nInput: ')
    return search

#print baord
def printBoard(board):
    for i in range(0,3):
        for y in range(0,3):
            print(board[i][y], end = ' ')
        print('')
    print('')


#gets the different ways that the blank can move
def getChildren(node):
    #declaration of variables
    children = [] #array for children
    board = node.state
    r = 0 #row where 0 is
    c = 0 #column where 0 is

    #find the indices for '0'
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == '0':
                r = i
                c = j
    
    #0 move right
    if c !=2:
        #create new Node
        rightChild =  Node(board)
        rightChild.depth = node.depth + 1
        rightChild.cost = node.cost +1

        child = copy.deepcopy(node.state) # make copy of parent node
        #swap
        temp = child[r][c]
        child[r][c] = child[r][c+1]
        child[r][c+1] = temp

        #assign the new Node updated board
        rightChild.state = child
        #assign child
        node.child3 = rightChild
        children.append(rightChild)
    
    #0 move left
    if c !=0:
        leftChild =  Node(board)
        leftChild.depth = node.depth + 1

        child = copy.deepcopy(node.state) # make copy of parent node
        #swap
        temp = child[r][c]
        child[r][c] = child[r][c-1]
        child[r][c-1] = temp

        #assign the new Node updated board
        leftChild.state = child
        #assign child
        node.child2 = child
        children.append(leftChild)
    
    #0 move up
    if r !=0:
        upChild = Node(node)
        upChild.depth = node.depth + 1

        child = copy.deepcopy(node.state) # make copy of parent node
        #swap
        temp = child[r][c]
        child[r][c] = child[r-1][c]
        child[r-1][c] = temp

        #assign the new Node updated board
        upChild.state = child
        #assign child
        node.child0 = child
        children.append(upChild)

    #0 move down
    if r !=2:
        downChild = Node(node)
        downChild.depth = node.depth + 1

        child = copy.deepcopy(node.state) # make copy of parent node
        #swap
        temp = child[r][c]
        child[r][c] = child[r+1][c]
        child[r+1][c] = temp

        #assign the new Node updated board
        downChild.state = child
        #assign child
        node.child1 = child
        children.append(downChild)

    return children


#Breadth First Search - A* g(n) + h(n) where h(n) = 0
def UniformSearch(board,search):
    #initialize variables
    qSize = 0 #len of queue
    max = 0 #compare with max to track biggest queue size  
    nodesExp = 0 #everytime we append to queue add 1
    timestart = time.time() #to get time elapsed
    start = Node(board)
    start.cost = 1
    queue = []
    done = []

    #append root node
    queue.append(start)
    #while length of queue is not empty
    while len(queue) > 0:
        node = queue.pop(0)
        #if the board of the node is not in the done array append it on
        if node.state not in done:
            done.append(node.state)
        
        #if the node state is equal to the goal, then done
        if node.state == goal:
            print('Goal State!')
            print('Solution Depth was ' + str(node.depth))
            print('Number of nodes expanded: ' + str(nodesExp))
            print('Max queue size: ' + str(max))
            print('Time taken is ' + str(f'{(time.time() - timestart):.2f}') + ' secs')
            return node
        else:
            children = []
            dup = False
            printBoard(node.state)
            children0 = getChildren(node)
            #check for duplicates
            for i in children0:
                for j in done:
                    if i.state == j:
                        dup = True
                if dup == False:
                    children.append(i)
                dup = False
            #if uniform search, append to queue
            if search == '1':
                for i in children:
                    queue.append(i)
                    #increment number of nodes expanded
                    nodesExp += 1
            #if Manhattan search
            elif search == '2': 
                for i in children:
                    heuristic = ManhattanSearch(i)
                    i.cost = heuristic
                    #increment number of nodes expanded
                    nodesExp += len(children)
            #if Misplaced tiles
            elif search == '3':
                for i in children:
                    heuristic = TileSearch(i)
                    i.cost = heuristic
                    #increment number of nodes expanded
                    nodesExp += len(children)

            #find index of min heurestic
            if search != '1':
                min = 100
                for i in children:
                    if int(i.cost) < min:
                        minchild = i
                        min = i.cost
                #find all instances of the min cost
                for i in children:
                    if i.cost == min:
                        queue.append(i)
                
                print('The best state to expand with a g(n) = ' + str(minchild.depth) + ' and h(n) = ' + str(minchild.cost) + ' is: ')
            #check for max size of the queue
            qSize = len(queue)
            if qSize > max:
                max = qSize    

def ManhattanSearch(node):
    #calculate the h(n)
    board = node.state
    manhattan = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] != goal[i][j] and board[i][j] != '0':
                value = int(board[i][j])
                manhattan += (abs(i-coord[value-1][0]) + abs(j-coord[value-1][1]))
    return manhattan
    

def TileSearch(node):
    #calculate h(n)
    board = node.state
    misplaced = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] != goal[i][j]:
                misplaced +=1
    #if 0 is not in the correct place, subtract 1 from count --> not worrying about 0
    if(board[2][2] != '0'):
        misplaced -=1
    return misplaced

if __name__ == "__main__":
    main()
