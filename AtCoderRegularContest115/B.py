def main():
    n = int(input())
    C = [[0] * n for _ in range(n)]
    C[0] = list(map(int, input().split()))
    min_id = C[0].index(min(C[0]))
    base = [0] * n
    diff = [0] * n
    for i in range(n):
        base[i] = C[0][i] - C[0][min_id]
    for i in range(1, n):
        C[i] = list(map(int, input().split()))
        for j in range(n):
            diff[j] = C[i][j] - C[i][min_id]
        if diff != base:
            print("No")
            return
    B = base
    A = [C[i][min_id] for i in range(n)]
    print("Yes")
    print(*A)
    print(*B)


if __name__ == '__main__':
    main()
