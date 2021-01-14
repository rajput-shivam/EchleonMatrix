def pivotList(matrix):
    pivotPos=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]!=0:
                pivotPos.append(j)
                break
            if j==len(matrix)-1:
                pivotPos.append(len(matrix))
    return pivotPos

def checkEchleon(matrix,l1):   
    a=False
    if l1==sorted(l1):
        a=True

    b=True
    for i in range(len(l1)-1):
        if l1[i]==l1[i+1] and l1[i]!=len(matrix):
            b=False

    if a and b:
        return True
    else:
        return False


def shufflingRow(matrix,pivot):
    print("\n\n")
    print(pivot)
    print(matrix)
    n=len(pivot)
    for i in range(n):
        for j in range(n-i-1):
            if pivot[j+1]<pivot[j]:
                pivot[j+1],pivot[j]=pivot[j],pivot[j+1]
                matrix[j+1],matrix[j]=matrix[j],matrix[j+1]
    print("after shuffling")
    print(pivot)
    print(matrix)



def rowOperation(matrix,pivot):
    print("\n\n")
    print(pivot)
    print(matrix)
    n=len(pivot)
    for i in range(n-1):
        if pivot[i]==pivot[i+1]:
            x1=i
            x2=i+1
            y=pivot[i]
            p1=matrix[x1][y]
            p2=matrix[x2][y]
            l1=matrix[x1].copy()
            l2=matrix[x2].copy()
            l1=[p2*i for i in l1]
            l2=[p1*i for i in l2]
            for i in range(len(l2)):
                l2[i]=l2[i]-l1[i]
            matrix[x2]=l2
            pivot=pivotList(matrix)
            print("after row-operation")
            print(pivot)
            print(matrix)
    return pivot
    
    

def convertEchleon(matrix,pivot):
    while True:
        if checkEchleon(matrix,pivot)==False:
            shufflingRow(matrix,pivot)
        if checkEchleon(matrix,pivot)==False:
            pivot=rowOperation(matrix,pivot)
        if checkEchleon(matrix,pivot)==True:
            break
    return matrix




matrix=[[0,0,6],[3,4,5],[2,1,5]]
pivot=pivotList(matrix)
matrix=convertEchleon(matrix,pivot)

print("\n\n\n")
print("FINAL ECHLEON MATRIX")
for i in matrix:
    print(i)



    

    

