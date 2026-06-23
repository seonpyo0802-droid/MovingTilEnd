import tkinter as tk
import os
import csv
import random

#2 is character
#1 is stone
#3 is goal

map_maker=[
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0]
]

window=tk.Tk()
window.geometry('920x650')
window.resizable(0,0)

grid_num=11

total_count=0

cor=[]

maps=[
    
]

map=[
    
]

done=[]

ending=tk.Label(window,text='')

#------------------------------------------------------------------------------------------------------#

#finding the number of maps
current_dir='c:\\Users\\220221\\Desktop\\python\\game\\movingTilEnd\\'
path=os.path.join(current_dir,'maps')
count_files=0
for file in os.listdir(path):
    count_files+=1
mapsNum=count_files

#--------------------------------------------------------------------------------#

#bringing maps
map_I_want=3
file_path=f'game/movingTilEnd/maps/map{map_I_want}.csv'
with open(file_path,mode='r',newline='') as file:
    reader=csv.reader(file)
    for lines in reader:
        ins=[]
        for i in lines:
            ins.append(int(i))
        map.append(ins)

#------------------------------------------------------------------------------------------------#

#finding the coordinate of the character
def find_cor():
    global map,cor
    cor=[]
    for y in range(0,11):
        for x in range(0,11):
            if map[y][x]==2:
                cor.append(x)
                cor.append(y)
find_cor()

#-----------------------------------------------------------------#

countL=tk.Label(window,font="Ariel 20")
countL.place(x=500,y=50)
#checking how many moves made'
count=0
countL.config(text=f'{count} moves')
#----------------------------------------------------------------------------------------------#

#the code to run when the goal is reached
def end():
    global count,total_count
    total_count+=count
    for i in window.place_slaves():
        i.destroy()
    for i in window.pack_slaves():
        i.destroy()
    ending=tk.Label(window,text=f'You completed\nAll maps\nTook {total_count} moves in Total', font='Ariel 50 bold')
    ending.place(x=100,y=200)

#-----------------------------------------------------------------------------------------------------#

#making the title
Title=tk.Label(window,text='Move Steve!',font='Ariel 30 bold')
Title.pack()

#-------------------------------------------------------------------------------#

#bringing pictures
current_dir = os.path.dirname(os.path.abspath(__file__))
grass_path = os.path.join(current_dir, "grass.png")
stone_path = os.path.join(current_dir, "stone.png")
face_path = os.path.join(current_dir, "face.png")

face_image=tk.PhotoImage(file=face_path)
grass_image=tk.PhotoImage(file=grass_path)
stone_image=tk.PhotoImage(file=stone_path)

#--------------------------------------------------------------------------------#

#making blocks and saving them
blocks=[]
def make_blocks():
    global blocks
    blocks=[]
    for j in range(11):
        blocks.append([])
        for i in range(11):
            button = tk.Button(window,width=50,height=50,image=grass_image)
            button.place(x=7+i*55,y=80+50*j)
            if map[j][i]==2:
                button.config(image=face_image)
            elif map[j][i]==1:
                button.config(image=stone_image)
            elif map[j][i]==3:
                button.config(bg='red')
            blocks[j].append(button)
make_blocks()

#---------------------------------------------------------------------------------#

#the codes to move
def up():
    global cor,face_image,grass_image,count,countL,blocks
    x=cor[0]
    y=cor[1]
    map[y][x]=0
    blocks[y][x].config(image=grass_image)
    count+=1
    countL.config(text=f'{count} moves')
    for i in range(y,-1,-1):
        y=i
        if map[y-1][x]==1:
            break
    if map[y][x]==3:
        for i in blocks:
            for j in i:
                j.destroy()
        end()
    else:
        map[y][x]=2
        cor[0]=x
        cor[1]=y
        blocks[y][x].config(image=face_image)
    

def right():
    global cor,face_image,grass_image,grid_num,count,blocks
    x=cor[0]
    y=cor[1]
    map[y][x]=0
    blocks[y][x].config(image=grass_image)
    count+=1
    countL.config(text=f'{count} moves')
    for i in range(x,grid_num):
        x=i
        if x+1 != grid_num:
            if map[y][x+1]==1:
                break
    if map[y][x]==3:
        for i in blocks:
            for j in i:
                j.destroy()
        end()
    else:
        map[y][x]=2
        cor[0]=x
        cor[1]=y
        blocks[y][x].config(image=face_image)
    

def left():
    global cor,face_image,grass_image,count,blocks
    x=cor[0]
    y=cor[1]
    map[y][x]=0
    blocks[y][x].config(image=grass_image)
    count+=1
    countL.config(text=f'{count} moves')
    for i in range(x,-1,-1):
        x=i
        if map[y][x-1]==1:
            break
    if map[y][x]==3:
        for i in blocks:
            for j in i:
                j.destroy()
        end()
    else:
        map[y][x]=2
        cor[0]=x
        cor[1]=y
        blocks[y][x].config(image=face_image)
    

def down():
    global cor,face_image,grass_image,grid_num,count,blocks
    x=cor[0]
    y=cor[1]
    map[y][x]=0
    blocks[y][x].config(image=grass_image)
    count+=1
    countL.config(text=f'{count} moves')
    for i in range(y,grid_num):
        y=i
        if y+1 != grid_num:
            if map[y+1][x]==1:
                break
    if map[y][x]==3:
        for i in blocks:
            for j in i:
                j.destroy()
        end()
    else:
        map[y][x]=2
        cor[0]=x
        cor[1]=y
        blocks[y][x].config(image=face_image)
    

#--------------------------------------------------------------------------------#

#buttons to move
def buttons():
    u_button=tk.Button(window,width=7,height=3,bg='gray',command=up)
    u_button.place(x=740,y=220)

    r_button=tk.Button(window,width=7,height=3,bg='gray',command=right)
    r_button.place(x=798,y=275)

    l_button=tk.Button(window,width=7,height=3,bg='gray',command=left)
    l_button.place(x=682,y=275)

    d_button=tk.Button(window,width=7,height=3,bg='gray',command=down)
    d_button.place(x=740,y=330)

    arrow_l=tk.Label(window,text='ARROW',font='Ariel 10 bold')
    arrow_l.place(x=742,y=290)
buttons()

#--------------------------------------------------------------------------------#

window.mainloop()

#-----------------------#

#아이디어 창