# -*- coding: cp936 -*-
import os
#path=input('�������ļ�·��(��β����/)��')
path="./myPicture/"

#��ȡ��Ŀ¼�������ļ��������б���
f=os.listdir(path)

n=0
for i in f:
    
    #���þ��ļ���������·��+�ļ�����
    oldname=path+f[n]
    
    #�������ļ���
    newname=path+str(n+1)+'.JPG'
    
    #��osģ���е�rename�������ļ�����
    os.rename(oldname,newname)
    print(oldname,'======>',newname)
    
    n+=1
