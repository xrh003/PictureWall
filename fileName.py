# -*- coding: cp936 -*-
import os

def fileRename_():
	#path=input('�������ļ�·��(��β����/)��')
	path="./myPicture/"

	#��ȡ��Ŀ¼�������ļ��������б���
	f=os.listdir(path)

	n=0
	for i in f:
	    
	    #���þ��ļ���������·��+�ļ�����
	    oldname=path+f[n]
	    
	    #�������ļ���
	    newname=path+'a'+str(n+1)+'.JPG'
	    
	    #��osģ���е�rename�������ļ�����
	    os.rename(oldname,newname)
	    print(oldname,'======>',newname)
	    
	    n+=1

def fileRename():
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

if __name__ == '__main__':
	fileRename_()
	fileRename()
