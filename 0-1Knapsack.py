
if __name__=='__main__':
    m = int(input("Enter the capacity: "))
    n = int(input("Enter the number of items : "))
    C = []
    W = []
    for i in range(n):
        C[i]=int(input("Enter the cost of item ",i, " : "))
        W[i]=int(input("Enter the weight of item ",i, " : "))
    KnapSack(C,W,m,n)
