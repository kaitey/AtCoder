def main():
    h, w = list(map(int, input().split()))
    s = [["."] * w for _ in range(h)]
    c = [[] for _ in range(h)]
    num = 0
    for i in range(h):
        for j in range(w-1):
            if s[j][i] != s[j+1][i]:
                c[i].append(i)
    for i in range(h-1):
        diff = list(set(s[i]) ^ set(s[i+1]))
        diff.sort(reverse=True)
        for l in reversed(range(1, len(diff))):
            if diff[l] - diff[l-1] > 1:
                num += 1



if __name__ == '__main__':
    main()
