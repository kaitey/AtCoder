from copy import deepcopy


def main():
    n = int(input())

    state0 = [0, 0, 0]
    for i in range(n):
        state1 = list(map(int, input().split(" ")))
        if not judge_trip_possible(state0, state1):
            print("No")
            return
        state0 = deepcopy(state1)
    print("Yes")
    return


def judge_trip_possible(state0, state1):
    t = state1[0] - state0[0]
    x = state1[1] - state0[1]
    y = state1[2] - state0[2]
    distance = abs(x) + abs(y)
    for i in range((t - distance) // 2 + 1):
        if distance == t - 2 * i:
            return True
    return False


if __name__ == '__main__':
    main()
