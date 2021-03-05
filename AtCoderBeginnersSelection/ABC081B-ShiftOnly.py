def main():
    n = int(input())
    nums = list(map(int, input().split(" ")))
    count = 0
    while True:
        if not check_if_gross_even_number(nums):
            print(count)
            return
        count += 1
        nums = [num / 2 for num in nums]


def check_if_gross_even_number(nums):
    for num in nums:
        if num % 2 == 1:
            return False
    return True


if __name__ == '__main__':
    main()
