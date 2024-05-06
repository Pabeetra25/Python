import os
def current_directory():#to retrieve current working directory
    cwd=os.getcwd()
    print(cwd) #cwd-current working directory
current_directory()

def file_path(filemname):#to retrieve path of particular file
    path=os.path.abspath((filemname)) 
    print(path)   
filename='poems.txt'
file_path(filename)    
