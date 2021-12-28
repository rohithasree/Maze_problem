# program on maze 
# this program will generate optimal path from start node to goal node using A* search algorithm
# importing libraries pyamaze for maze creation and queue for priority queue generation
from queue import PriorityQueue
from pyamaze import maze,agent,textLabel
# generating heuristics
# calculating manhattan distance between the current node and the goal node
# here we can take euclidean distance as well
def h(cur_cell1,cur_cell2):
    x1,y1=cur_cell1
    x2,y2=cur_cell2
# this function will return manhattan distance as output
    return abs(x1-x2) + abs(y1-y2)
# generating priority queue using the aStar function
def aStaralgo(m):
# intializing start node as right bottom cell of maze
    start=(m.rows,m.cols)
# initializing g(n) of all cells to infinity
    g_score={cell:float('inf') for cell in m.grid}
# intializing g() of start node to zero 
    g_score[start]=0
# initializing f(n) of all cells to infinity 
    f_score={cell:float('inf') for cell in m.grid}
# intializing f(start) to heuristic of start node 
    f_score[start]=h(start,(1,1))
# creating priority queue named list which will keep track of traversing nodes an childnodes
    list=PriorityQueue()
# pushing start node into the priority queue using put function
    list.put((h(start,(1,1)),h(start,(1,1)),start))
# intializing a dictionary for keeping track of path we have traversed
    aPath={}
# this loop will continue till the priority queue becomes empty
    while not list.empty():
# taking the variable current_cell and itializing it to start cell
        currCell=list.get()[2]
# if it is equal to goal node then break the loop. here the goal node is taken a (1,1)
        if currCell==(1,1):
            break
# if the start node is not the goal node then the loop will be continue
# E- east S- south N-north W-west
# we can go through four directions and reach the neighbour nodes
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
# direction is east then row value remains the same and the column value will be increased by 1
                if d=='E':
                    n_Cell=(currCell[0],currCell[1]+1)
# direction is west then row value remains the same and the column value will be decreased by 1
                if d=='W':
                    n_Cell=(currCell[0],currCell[1]-1)
# direction is north then column value remains the same and the row value will be incremented by 1

                if d=='N':
                    n_Cell=(currCell[0]-1,currCell[1])
# direction is north then column value remains the same and the row value will be decreased by 1

                if d=='S':
                    n_Cell=(currCell[0]+1,currCell[1])
# updating the new g(n) and f(N) values by generating new heuristic functions
                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(n_Cell,(1,1))
# if the f(n) is less than the previous one then update the values
                if temp_f_score < f_score[n_Cell]:
                    g_score[n_Cell]= temp_g_score
                    f_score[n_Cell]= temp_f_score
                    list.put((temp_f_score,h(n_Cell,(1,1)),n_Cell))
# the current cell is stored as value and next cell is stored as key in apath
                    aPath[n_Cell]=currCell
# the path we got will be in reverse direction we need to change o right direction
# initializing another dictionary rightpath
    rightPath={}
    cell=(1,1)
    while cell!=start:
        rightPath[aPath[cell]]=cell
        cell=aPath[cell]
    return rightPath

if __name__=='__main__':
# creating maze of 7*7 size
    m=maze(7,7)
    m.CreateMaze()
# path variable to store the right path
    path=aStaralgo(m)
# agent is created to trace the path
    a=agent(m,footprints=True)
    m.tracePath({a:path})
    l=textLabel(m,'A Star Path Length',len(path)+1)

    m.run()
