if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

sort_arr = sorted(arr)
max_num = sort_arr[-1]

for num in range(len(sort_arr) - 2, -1, -1):
    if sort_arr[num] < max_num:
        print(sort_arr[num])
        break
    else:
        continue
