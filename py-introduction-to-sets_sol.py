#py-introduction-to-sets : Calculate the avarges of items present inside a python set

def average(array):
    st = set(array)
    n = len(st)
    sun = sum(st)
    avg = sun / n
    return avg
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)