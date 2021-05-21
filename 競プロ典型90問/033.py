h, w = list(map(int, input().split()))
ans = -(-h // 2) * -(-w // 2)
if h==1 or w==1:
  ans = h * w
print(ans)
