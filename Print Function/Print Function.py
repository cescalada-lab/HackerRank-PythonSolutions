if __name__ == '__main__':
    n = int(input())
    if (n>=1 and n<=150):
        list=[]
        for i in range(1,n+1):
            list.append(i)
        print(*list,sep="")
        
        
