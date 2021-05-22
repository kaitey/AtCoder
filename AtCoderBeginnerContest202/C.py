def main():
    N = int(input())
    A = list(map(int, input().split()))
    B_tmp = list(map(int, input().split()))
    C_tmp = list(map(int, input().split()))
    B = [0] * (N + 1)
    C = [0] * (N + 1)
    for i in range(N):
        C[C_tmp[i]] += 1
    for i, b in enumerate(B_tmp):
        B[b] += C[i+1]
    ans = 0
    for a in A:
        ans += B[a]
    print(ans)


if __name__ == '__main__':
    main()
