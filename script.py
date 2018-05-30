'''
    @author anooppoommen
    usage python script.py <commit-message> <no-push>
'''
import os
import sys
import time

if(len(sys.argv) > 1):
    if(sys.argv[1] == 'n'):
        msg = "Auto commit message @ " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    else:    
        msg = sys.argv[1] + " @ "+time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
else:
    msg = "Auto commit message @ " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

add = os.system("git add .")

if not (add == 0):
    print("Failed to add")
    exit(0)

commit = os.system("git commit -am \""+msg+"\"")

if not (commit == 0):
    print("Failed to commit")

if(len(sys.argv)  > 1):
    if sys.argv[1] == 'n':
        print("All saved bose!.")
        exit();

if(len(sys.argv) > 2):
    print("All done boss!")
    exit(0);
    
print("Trying to push changes to repository")    
# 1=>push ,128=> no internet
while 1:
    push  = os.system("git push origin master") 
    if push == 0 :
        print("All done bose!")
        break;
    elif push == 1:
        pull = os.system("git pull origin master")
        add  = os.system("git add .")
        commit = os.system("git commit -am \"merge fixes\"")
    else:
        os.system("clear");
        print("Something terrible has Happened. I can't connect to the internet boss!!")
        break;