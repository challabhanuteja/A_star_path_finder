import pygame
import random
n = 10
def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

#a[][0]=-1
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def main():

    a     = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
    #a = [[random.choice([0,1])]*n for i in range(n)]
    # a= random.choice([0,1])
    start = (0, 0)
    end = (0, 9)

    pygame.init()

    white = (255,255,255)
    red = (255,0,0)
    green =(0,255,0)
    blue = (0,0,255)
    black = (0,0,0)
    grey = (128,128,128)
    window_width=400
    window_height=400
    gameDisplay = pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption('A* path finder')
    pygame.display.update() #or pygame.display.flip()
    clock = pygame.time.Clock()


    w=window_width/n
    h=window_height/n
    gameDisplay.fill(white)
    x,y=0,0
    for row in a:
        for col in row:
            pygame.draw.rect(gameDisplay,black,[x,y,w,h],2)
            if col==1:
                gameDisplay.fill(grey,[x,y,w,h])

            x+=w
        x=0
        y=y+h
    gameDisplay.fill(blue,[start[1]*w,start[0]*h,w,h])
    gameDisplay.fill(blue,[end[1]*w,end[0]*h,w,h])
    pygame.display.update()


    def game_loop():
        completed = False
        gameExit = False
        closed1=  astar(a, start, end)
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True

            for i in closed1:
                x,y= i
                gameDisplay.fill(green,[y*h,x*w,w,h])
                clock.tick(1)
                pygame.display.update()
            completed=True
            if completed ==True:
                break

    game_loop()



if __name__ == '__main__':
    main()
