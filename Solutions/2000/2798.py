n, m = map(int, input().split())
nums = list(map(int, input().split()))
curr = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            score = nums[i] + nums[j] + nums[k]
            if curr < score <= m:
                curr = score
print(curr)
