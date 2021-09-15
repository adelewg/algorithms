t = int(input())

while t!= 0:
    counter = 0
    N = int(input())
    #read N lines of integers
    arr = []
    for i in range(N):
        arr.append(map(int(input().split()))) 
        print(i)