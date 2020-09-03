nums = [3,2,1,0,1,2,3]
n = len(nums)

stack = []
for i in range(n):
    while stack and nums[stack[-1]] <= nums[i]:
        curr = stack.pop()
        if not stack:
            break
        left, right = stack[-1], i
        print(left, curr, right)
    stack.append(i)