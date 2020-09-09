import time

from word_search_puzzle.utils import display_panel
from word_search_puzzle.algorithms import create_panel

words = ['cat', 'dog', 'tiger', 'lion']

table = [['0' for i in range(10)] for i in range(10)]
result = create_panel(height=10, width=10, words_value_list=words)
position = ""
import math

# print('Attempts: {}'.format(result.get('attempts')))
# print('Solution took: {} ms'.format(result.get('elapsed_time')))
display_panel(result.get('panel'))
#print(result.get('panel').cells[0,0])
#print(type(result.get('panel')))

for i in range(0,10):
    for j in range(0, 10):
        table[i][j] = result.get('panel').cells[i,j]
#
# #print(table[0][0])
# print()
def DFS(row,column,string):
    print("NorthEast:\n", end="")
    DFSsearch(row,column, string, 'NorthEast')
    print("East:\n",end="")
    DFSsearch(row,column,string,'East')
    print("SouthEast:\n", end="")
    DFSsearch(row,column,string,'SouthEast')
    print("South:\n", end="")
    DFSsearch(row,column,string,'South')

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
    print(row, column, tmp_round, last_round)
    if(last_round > 0):
        print("NorthEast: ")
        IDDFSSearch(row, column, string, 'NorthEast', tmp_round, last_round)
        print("East: ")
        IDDFSSearch(row, column, string, 'East',tmp_round,last_round)
        print("SouthEast: ")
        IDDFSSearch(row, column, string, 'SouthEast', tmp_round, last_round)
        print("South: ")
        IDDFSSearch(row, column, string, 'South', tmp_round, last_round)
        print('----------')
    #tmp = row - column
    #if (last_round < 9):
    if(last_round<9-min(row,column)):                           #ใช้ในการลดการทำงานซ้ำโดยไม่จำเป็น เช่น (7,2) จะวนซ้ำ 9-2 = 7 ครั้ง
        IDDFS(row, column, string, tmp_round, last_round + 1)
    # if(row>=column):
    #      if(row-column>last_round):
    #          IDDFS(row, column, string, tmp_round, last_round+1)

def IDDFSSearch(row,column,string,dir,tmp_round,last_round):
    if(tmp_round <= last_round):
        if(row >= 0 and row <= 9):
            if (column >= 0 and column <= 9):
                # print(table[row][column],(row,column), end=" ")
                string = string + table[row][column]    #Stack
                print(string)
                time.sleep(0.5)
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

# for row in range(0,10):
#     for column in range(0,10):
#         print('Root:',row,column)
#         DFS(row,column,"")
# print(position)
for row in range(0,10):
    for column in range(0,10):
        print('___Root:',row,column)
        IDDFS(row,column,"",0,0)
        print('-------------------------------------------')
print(position)