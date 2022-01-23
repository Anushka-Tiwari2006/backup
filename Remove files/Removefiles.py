import time,os,shutil

path = "C:\Downloads\Thumbs"
days = 30

time_seconds = time.time()
os.path.exists(path)
os.walk(path)
os.path.join(path,"C:\\Users\\dell")

def compare_time():
    ctime = os.stat(path).st_ctime
    return ctime

compare_time()

def removePath():
    if(time.ctime > days):
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path) 
    else:
        if os.path.exists(path): 
           print ("File exist")
        else:
           print ("File not exist")
           
removePath()
            
        

