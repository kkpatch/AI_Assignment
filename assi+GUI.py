#import necessary lib
import pygame
import os 
import random
import time
#import puzzel generetor
from word_search_puzzle.utils import display_panel
from word_search_puzzle.algorithms import create_panel

pygame.font.init()
myfont = pygame.font.SysFont("comicsans",40)

position = ""

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)


WIDTH,HEIGHT = 400,400
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Test")


blockSize = 80 #Set the size of the grid block
def redraw(PosX,PosY):    
    SCREEN.fill(BLACK)

    drawGrid()
    circle(PosX,PosY)

    pygame.display.update()

def main():
    FPS = 60
    CLOCK = pygame.time.Clock()

    puzzle_gen()


    while True:
        CLOCK.tick(FPS)
        s()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

def drawGrid():
    for x in range(5):
        for y in range(5):
            #rect = pygame.Rect(x*blockSize, y*blockSize,blockSize, blockSize)
            #pygame.draw.rect(SCREEN, WHITE, rect, 1)
            textsurface = myfont.render(table[x][y], True, (255, 255, 255)) #text / Anti aliasing / color (in this case it's white)
            SCREEN.blit(textsurface,(y*blockSize+30,x*blockSize+30))

def puzzle_gen():
    global words,table
    words = ['cat', 'bear', 'tiger', 'lion']
    table = [['0' for i in range(5)] for i in range(5)]
    result = create_panel(height=5, width=5, words_value_list=words)

    display_panel(result.get('panel'))
    #convert into 2d array
    for i in range(0,5):
        for j in range(0, 5):
            table[i][j] = result.get('panel').cells[i,j]

def circle(PosX,PosY):    
    #for i in range(0,5):
        #for j in range(0,5):            
            #screen.blit(my_image, another_position)
    pygame.draw.circle(SCREEN, (0,255,0), (PosY*blockSize+blockSize//2,PosX*blockSize+blockSize//2), blockSize//4,2)
            #print('Root:',i,j)
            #DFS(i,j,"")

def s():
    for i in range(0,5):
        for j in range(0, 5):
            print('Root:',i,j)
            IDDFS(i,j,"",0,0)

#initial search
def DFS(PosX,PosY,string):
    position = ""
    print("NorthEast: ", end="")
    search(PosX, PosY, string, 'NorthEast', position)
    print()
    print("East: ",end="")
    search(PosX,PosY,string,'East', position)
    print()
    print("SouthEast: ", end="")
    search(PosX,PosY,string,'SouthEast', position)
    print()
    print("South: ", end="")
    search(PosX,PosY,string,'South', position)
    print()
    
#recursion
def search(PosX,PosY,string,dir,position):
    if(PosX >= 0 and PosX <= 4):
        if (PosY >= 0 and PosY <= 4):
            #print(table[PosX][PosY], end=" ")
            string = string + table[PosX][PosY]
            print(string)
            redraw(PosX,PosY)
            time.sleep(0.5)
            if string in words:
                print("------------------------------------------------------")
            if (dir == 'NorthEast'):
                search(PosX-1, PosY+1, string, dir, position)
            if (dir == 'East'):
                search(PosX, PosY+1, string, dir, position)
            if (dir == 'South'):
                search(PosX+1, PosY, string, dir, position)
            if (dir == 'SouthEast'):
                search(PosX + 1, PosY+1, string, dir, position)

def DFSsearch(row,column,string,dir):
    if(row >= 0 and row <= 9):
        if (column >= 0 and column <= 9):
            #print(table[PosX][PosY], end=" ")
            string = string + table[row][column]
            print(string)

            if string in words:
                global position
                if(dir == 'NorthEast'):
                    position = position + string + " at " + str(row+len(string)-1) + ',' + str(column-len(string)+1) + ' direction: NorthEast' +'\n'
                if(dir == 'East'):
                    position = position + string + " at " + str(row) + ',' + str(column - len(string) + 1) + ' direction: East' +'\n'
                if(dir == 'South'):
                    position = position + string + " at " + str(row - len(string)+1) + ',' + str(column) + ' direction: South' +'\n'
                if (dir == 'SouthEast'):
                    position = position + string + " at " + str(row - len(string) + 1) + ',' + str(column - len(string) + 1) + ' direction: SouthEast' +'\n'
            if (dir == 'NorthEast'):
                DFSsearch(row-1, column+1, string, dir)
            if (dir == 'East'):
                DFSsearch(row, column+1, string, dir)
            if (dir == 'South'):
                DFSsearch(row+1, column, string, dir)
            if (dir == 'SouthEast'):
                DFSsearch(row + 1, column+1, string, dir)

def IDDFS(row,column,string,tmp_round,last_round):
    print('round: ',last_round)
    print("-NorthEast: ")
    IDDFSSearch(row, column, string, 'NorthEast', tmp_round, last_round)
    print("-East: ")
    IDDFSSearch(row, column, string, 'East',tmp_round,last_round)
    print("-SouthEast: ")
    IDDFSSearch(row, column, string, 'SouthEast', tmp_round, last_round)
    print("-South: ")
    IDDFSSearch(row, column, string, 'South', tmp_round, last_round)
    print('----------')
    tmp = row - column
    #if (last_round < 9):
    if(last_round<4-min(row,column)):                           #ใช้ในการลดการทำงานซ้ำโดยไม่จำเป็น เช่น (7,2) จะวนซ้ำ 9-2 = 7 ครั้ง
        IDDFS(row, column, string, tmp_round, last_round + 1)
    # if(row>=column):
    #      if(row-column>last_round):
    #          IDDFS(row, column, string, tmp_round, last_round+1)

def IDDFSSearch(row,column,string,dir,tmp_round,last_round):
    if(tmp_round <= last_round):
        if(row >= 0 and row <= 4):
            if (column >= 0 and column <= 4):
                # print(table[row][column],(row,column), end=" ")
                string = string + table[row][column]    #Stack
                print(string)
                redraw(row,column)
                time.sleep(0.1)
                # print(tmp_round,last_round,end = " ")
                # print(row,column,end = "\n")
                if string in words:                     #หาว่า string(stack)ที่ได้จากการ Search ตรงกับคำที่อยู่ใน list หรือไม่
                    global position
                    if string not in position:          #ใช้ในการเลือก Save ประโยคที่่ไม่ซ้ำกับประโยคที่มีอยู่แล้ว
                        if(dir == 'NorthEast'):
                            position = position + string + " at " + str(row+len(string)-1) + ',' + str(column-len(string)+1) + ' direction: NorthEast' +'\n'
                        if(dir == 'East'):
                            position = position + string + " at " + str(row) + ',' + str(column - len(string) + 1) + ' direction: East' +'\n'
                        if(dir == 'South'):
                            position = position + string + " at " + str(row - len(string)+1) + ',' + str(column) + ' direction: South' +'\n'
                        if (dir == 'SouthEast'):
                            position = position + string + " at " + str(row - len(string) + 1) + ',' + str(column - len(string) + 1) + ' direction: SouthEast' +'\n'
                if(dir == 'NorthEast'):
                    IDDFSSearch(row-1, column+1, string, dir ,tmp_round+1,last_round)
                if (dir == 'East'):
                    IDDFSSearch(row, column+1, string, dir,tmp_round+1,last_round)
                if (dir == 'South'):
                    IDDFSSearch(row+1, column, string, dir,tmp_round+1,last_round)
                if (dir == 'SouthEast'):
                    IDDFSSearch(row + 1, column+1, string, dir,tmp_round+1,last_round)
main()