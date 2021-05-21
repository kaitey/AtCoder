N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
shift = 0
for i in range(Q):
  T, x, y = list(map(int, input().split()))
  if T == 1:
    A[(x - 1 - shift) % N], A[(y - 1 - shift) % N] = A[(y - 1 - shift) % N], A[(x - 1 - shift) % N]
  elif T == 2:
    shift += 1
  else:
    print(A[(x - 1 - shift) % N])
