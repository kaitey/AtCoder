n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
diff = 0
for a, b in zip(A, B):
    diff += abs(a - b)
if diff > k or (diff - k) % 2 == 1:
    print("No")
else:
    print("Yes")
