def search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0


n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
for num in input().split():
    print(search(a, int(num)))
