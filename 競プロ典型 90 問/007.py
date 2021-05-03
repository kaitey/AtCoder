def bin_search(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return max(left, right)

n = int(input())
A = list(map(int, input().split()))
A.sort()
q = int(input())
for _ in range(q):
    b = int(input())
    i = bin_search(A, b)
    try:
        print(min(abs(b - A[i - 1]), abs(b - A[i])))
    except IndexError:
        print(abs(b - A[i - 1]))
