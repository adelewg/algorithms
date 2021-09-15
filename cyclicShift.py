""" 
A large binary number is represented by a string  of size  and comprises of  and . You must perform a cyclic shift on this string. The cyclic shift operation is defined as follows:

If the string  is , then after performing one cyclic shift, the string becomes .
You performed the shift infinite number of times and each time you recorded the value of the binary number represented by the string. The maximum binary number formed after performing (possibly ) the operation is . Your task is to determine the number of cyclic shifts that can be performed such that the value represented by the string  will be equal to  for the  time.

Input format

First line: A single integer  denoting the number of test cases
For each test case:
First line: Two space-separated integers  and 
Second line:  denoting the string
Output format

For each test case, print a single line containing one integer that represents the number of cyclic shift operations performed such that the value represented by string  is equal to  for the  time.

 """

t = int(input())

while t!= 0:
    N, K = map(int, input().split())
    A = input()
    max = ""
    p = -1
    for i in range(N):
        if A > max:
            max = A
            d = i
        elif max == A:
            p = i - d
            break
        A = A[1:] + A[:1]
    if p == -1:
        print(d + (K - 1) * N)
    else:
        print(d + (K-1))
    print("")
    print("")
    t -= 1

