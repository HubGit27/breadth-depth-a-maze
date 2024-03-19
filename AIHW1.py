import argparse
import heapq

'''
1 are walls, 
0 is open path, 
2 is where the alg has been, 
5 is the final path without backtracking.
The directional priority must be: up, right, left, down.
'''
class a_cell:
    def __init__(self, parent=None):
        self.t = float('inf')  # Total cost (g + h)
        self.g = float('inf')  # Cost from start
        self.h = 0  # Heuristic
        self.pos0 = 0 # row
        self.pos1 = 0 # column
        self.parent = parent
        

    def __lt__(self, other):
        return self.t < other.t
    def __eq__(self, other):
        return self.t == other.t

def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))

def depthSeach(maze):
    print("depth")

    for i in (range(len(maze[9]))):
        if (maze[9][i] == 0):
            entrance = [9, i]
            break
    '''    
    iteration = 0
    '''
    stack = [entrance]
    all_paths = {(entrance[0], entrance[1]): []}
    while stack:
        temp_cord = stack.pop()

        #exit found
        if (temp_cord[0] == 0):
            #Loop through all the paths an change the path it took to get to exit with 5
            for i in all_paths[(temp_cord[0], temp_cord[1])]:
                maze[i[0]][i[1]] = 5
            maze[temp_cord[0]][temp_cord[1]] = 5
            break

        #Move down
        if (temp_cord[0]+1 <= 9) and maze[temp_cord[0]+1][temp_cord[1]] == 0:
            stack.append([temp_cord[0]+1, temp_cord[1]])
            all_paths[(temp_cord[0]+1, temp_cord[1])] = all_paths[temp_cord[0], temp_cord[1]] + [[temp_cord[0], temp_cord[1]]]
        #Move left
        if (temp_cord[1]-1 >= 0) and maze[temp_cord[0]][temp_cord[1]-1] == 0:
            stack.append([temp_cord[0], temp_cord[1]-1])
            all_paths[(temp_cord[0], temp_cord[1]-1)] = all_paths[temp_cord[0], temp_cord[1]] + [[temp_cord[0], temp_cord[1]]]
        #Move right
        if (temp_cord[1]+1 <= 9) and maze[temp_cord[0]][temp_cord[1]+1] == 0:
            stack.append([temp_cord[0], temp_cord[1]+1])
            all_paths[(temp_cord[0], temp_cord[1]+1)] = all_paths[temp_cord[0], temp_cord[1]] + [[temp_cord[0], temp_cord[1]]]
        #Move vertical
        if (temp_cord[0]-1 >= 0) and (maze[temp_cord[0]-1][temp_cord[1]] == 0):
            stack.append([temp_cord[0]-1, temp_cord[1]])
            all_paths[(temp_cord[0]-1, temp_cord[1])] = all_paths[temp_cord[0], temp_cord[1]] + [[temp_cord[0], temp_cord[1]]]

        '''
        #uncomment to see each iteration of maze
        print("iteration " + str(iteration))
        iteration = iteration + 1
        print_maze(maze)
        '''

        maze[temp_cord[0]][temp_cord[1]] = 2

def breadthSearch(maze):
    print("breadth")
    for i in (range(len(maze[9]))):
        if (maze[9][i] == 0):
            entrance = [9, i]
            break

    '''    
    iteration = 0
    ''' 
    queue = [entrance]
    all_paths = {(entrance[0], entrance[1]): []}
    while queue:
        temp_cord = queue.pop(0)

        #exit found
        if (temp_cord[0] == 0):
            #Loop through all the paths an change the path it took to get to exit with 5
            for i in all_paths[(temp_cord[0], temp_cord[1])]:
                maze[i[0]][i[1]] = 5
            maze[temp_cord[0]][temp_cord[1]] = 5
            break

        #Move vertical
        if (temp_cord[0]-1 >= 0) and (maze[temp_cord[0]-1][temp_cord[1]] == 0):
            queue.append([temp_cord[0]-1, temp_cord[1]])
            all_paths[(temp_cord[0]-1, temp_cord[1])] = all_paths[temp_cord[0], temp_cord[1]] + [[temp_cord[0], temp_cord[1]]]
        #Move right
        if (temp_cord[1]+1 <= 9) and maze[temp_cord[0]][temp_cord[1]+1] == 0:
            queue.append([temp_cord[0], temp_cord[1]+1])
            all_paths[(temp_cord[0], temp_cord[1]+1)] = all_paths[temp_cord[0], temp_cord[1]] + [[temp_cord[0], temp_cord[1]]]
        #Move left
        if (temp_cord[1]-1 >= 0) and maze[temp_cord[0]][temp_cord[1]-1] == 0:
            queue.append([temp_cord[0], temp_cord[1]-1])
            all_paths[(temp_cord[0], temp_cord[1]-1)] = all_paths[temp_cord[0], temp_cord[1]] + [[temp_cord[0], temp_cord[1]]]
        #Move down
        if (temp_cord[0]+1 <= 9) and maze[temp_cord[0]+1][temp_cord[1]] == 0:
            queue.append([temp_cord[0]+1, temp_cord[1]])
            all_paths[(temp_cord[0]+1, temp_cord[1])] = all_paths[temp_cord[0], temp_cord[1]] + [[temp_cord[0], temp_cord[1]]]
        
        ''' 
        #uncomment to see each iteration of maze
        print("iteration " + str(iteration))
        iteration = iteration + 1
        print_maze(maze)
        ''' 

        maze[temp_cord[0]][temp_cord[1]] = 2

def calculate_euclidean(cur, dest):
    return ((cur[0] - dest[0]) ** 2 + (cur[1] - dest[1]) ** 2) ** 0.5

def aSearch(maze):
    for i in (range(len(maze[9]))):
        if (maze[9][i] == 0):
            entrance = [9, i]
        if (maze[9][i] == 0):
            exit = [0, i]

    '''    
    iteration = 0
    '''

    entranceCell = a_cell()
    entranceCell.g = -1
    entranceCell.h = calculate_euclidean(entrance, exit)
    entranceCell.t = entranceCell.g + entranceCell.h
    entranceCell.pos0 = entrance[0]
    entranceCell.pos1 = entrance[1]
    entranceCell.parent = entranceCell

    open_list = [entranceCell]
    heapq.heapify(open_list)
    all_paths = {(entrance[0], entrance[1]): []}

    while open_list:
        temp_cord = heapq.heappop(open_list)

        #exit found
        if (temp_cord.pos0 == 0):
            #Loop through all the paths an change the path it took to get to exit with 5
            for i in all_paths[(temp_cord.pos0, temp_cord.pos1)]:
                maze[i[0]][i[1]] = 5
            maze[temp_cord.pos0][temp_cord.pos1] = 5
            break

        #Move vertical
        if (temp_cord.pos0-1 >= 0) and (maze[temp_cord.pos0-1][temp_cord.pos1] == 0):
            new_cell = a_cell(temp_cord)
            new_cell.pos0 = temp_cord.pos0 - 1
            new_cell.pos1 = temp_cord.pos1
            new_cell.g = new_cell.parent.g + 1
            new_cell.h = calculate_euclidean([new_cell.pos0, new_cell.pos1], exit)
            new_cell.t = new_cell.g + new_cell.h
            heapq.heappush(open_list, new_cell)
            
            all_paths[(temp_cord.pos0-1, temp_cord.pos1)] = all_paths[temp_cord.pos0, temp_cord.pos1] + [[temp_cord.pos0, temp_cord.pos1]]
        #Move right
        if (temp_cord.pos1+1 <= 9) and maze[temp_cord.pos0][temp_cord.pos1+1] == 0:
            new_cell = a_cell(temp_cord)
            new_cell.pos0 = temp_cord.pos0 
            new_cell.pos1 = temp_cord.pos1 + 1
            new_cell.g = new_cell.parent.g + 1
            new_cell.h = calculate_euclidean([new_cell.pos0, new_cell.pos1], exit)
            new_cell.t = new_cell.g + new_cell.h
            heapq.heappush(open_list, new_cell)
            all_paths[(temp_cord.pos0, temp_cord.pos1+1)] = all_paths[temp_cord.pos0, temp_cord.pos1] + [[temp_cord.pos0, temp_cord.pos1]]
        #Move left
        if (temp_cord.pos1-1 >= 0) and maze[temp_cord.pos0][temp_cord.pos1-1] == 0:
            new_cell = a_cell(temp_cord)
            new_cell.pos0 = temp_cord.pos0 
            new_cell.pos1 = temp_cord.pos1 - 1 
            new_cell.g = new_cell.parent.g + 1
            new_cell.h = calculate_euclidean([new_cell.pos0, new_cell.pos1], exit)
            new_cell.t = new_cell.g + new_cell.h
            heapq.heappush(open_list, new_cell)
            all_paths[(temp_cord.pos0, temp_cord.pos1-1)] = all_paths[temp_cord.pos0, temp_cord.pos1] + [[temp_cord.pos0, temp_cord.pos1]]
        #Move down
        if (temp_cord.pos0+1 <= 9) and maze[temp_cord.pos0+1][temp_cord.pos1] == 0:
            new_cell = a_cell(temp_cord)
            new_cell.pos0 = temp_cord.pos0 + 1
            new_cell.pos1 = temp_cord.pos1
            new_cell.g = new_cell.parent.g + 1
            new_cell.h = calculate_euclidean([new_cell.pos0, new_cell.pos1], exit)
            new_cell.t = new_cell.g + new_cell.h
            heapq.heappush(open_list, new_cell)
            all_paths[(temp_cord.pos0+1, temp_cord.pos1)] = all_paths[temp_cord.pos0, temp_cord.pos1] + [[temp_cord.pos0, temp_cord.pos1]]
        
        '''
        #uncomment to see each iteration of maze
        print("iteration " + str(iteration))
        iteration = iteration + 1
        print_maze(maze)
        '''
        maze[temp_cord.pos0][temp_cord.pos1] = 2

def main():
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    # Take in command line arguments when starting program
    parser = argparse.ArgumentParser(description='Search a maze with BDS(b), DPS(d), or A*(a)')
    parser.add_argument('input', help='Choice of algorithim. b, d, or a')
    args = parser.parse_args()

    search_alg = args.input
    valid_search = False
    while (valid_search == False):
        if (search_alg == "d"):
            valid_search = True
            depthSeach(maze)
        elif(search_alg == "b"):
            valid_search = True
            breadthSearch(maze)
        elif(search_alg == "a"):
            valid_search = True
            aSearch(maze)
        else:
            search_alg = input('Unknown input. Please enter b, d, or a \n')
    
    # maze_name = input("Enter the file of the maze")
    print("Final maze: ")
    print_maze(maze)
if __name__ == '__main__':
    main()
