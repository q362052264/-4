#coding=gbk
import os
import argparse


parse=argparse.ArgumentParser()
parse.add_argument("-l",help="这是层数",type=int,default=0)
parse.add_argument("path",help="这是你选择的路径",type=str,default="0")
args=parse.parse_args()
print(args.l)
print(args.path)
def la(form,chengji):
    ff=os.listdir(form)
    global args
    if chengji>args.l*3:
        return None
    for i in ff:
        for z in range(chengji):
            print(" ", end="")
        print(i)
        if os.path.isdir(form+'/'+i):
            x=form+'/'+i
            la(x,chengji+3)
if __name__=='__main__':
    la(args.path,0)





