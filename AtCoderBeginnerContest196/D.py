import operator


def calc(box, baggage):
    box.sort()
    value = 0
    i = 0
    while box and i < len(baggage):
        for j, b in enumerate(box):
            if b >= baggage[i][0]:
                value += baggage[i][1]
                box.pop(j)
                break
        i += 1
    print(value)


def main():
    n, m, q = list(map(int, input().split()))
    baggage = [list(map(int, input().split())) for _ in range(n)]
    baggage = sorted(baggage, key=operator.itemgetter(1, 0))
    baggage.reverse()
    boxes = list(map(int, input().split()))
    for _ in range(q):
        l, r = list(map(int, input().split()))
        calc(boxes[:l-1] + boxes[r:], baggage)


if __name__ == '__main__':
    main()
