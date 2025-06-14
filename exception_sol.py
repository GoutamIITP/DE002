# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
for i in range(N):
    try:
        a, b = input().split()
        res = int(a) // int(b)
        print(res)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as v:
        print("Error Code:", v)