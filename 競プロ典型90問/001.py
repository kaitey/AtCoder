def cutting(min_len):
    cut_num, cut_pos = 0, 0
    lens = []
    for a in A:
        leng = a - cut_pos
        if leng >= min_len:
            cut_num += 1
            cut_pos = a
            lens.append(leng)
    leng = L - cut_pos
    if leng < min_len:
        cut_num -= 1
        lens[-1] += leng
    else:
        lens.append(leng)
    return cut_num, lens


N, L = list(map(int, input().split()))
K = int(input())
A = list(map(int, input().split()))
mini, maxi = 1, L
while maxi > mini:
    mid = (mini + maxi) // 2
    cut_num, lens = cutting(mid)
    if cut_num >= K:
        if mini != min(lens):
            mini = min(lens)
        else:
            cut_num, lens = cutting(mid + 1)
            if cut_num >= K:
                mini = maxi
            else:
                maxi = mini
    else:
        maxi = mid - 1
print(mini)
