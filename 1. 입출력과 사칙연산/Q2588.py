import sys

if __name__ == '__main__':
    num1 = int(sys.stdin.readline().rstrip())
    num2 = int(sys.stdin.readline().rstrip())
    num2_list = list(map(int, str(num2)))

    for now_num in num2_list[::-1]:
        print(num1*now_num)

    print(num1*num2)
