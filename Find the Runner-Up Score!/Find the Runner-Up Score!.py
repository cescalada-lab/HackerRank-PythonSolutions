if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    arr.remove(max(set(arr)))
    print(max(set(arr)))
