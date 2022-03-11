nums = list(map(int, input().split()))

if not nums:
    print([])
elif len(nums) == 1:
    print([str(nums[0])])
else:
    start = nums[0]
    stop = nums[0]

    output = []

    for i in range(1, len(nums)):
        if i == len(nums) - 1 and nums[i] == nums[i - 1] + 1:
            output.append(f"{start}->{nums[i]}")
        elif i == len(nums) - 1 and nums[i] != nums[i - 1] + 1:
            if start == stop:
                output.append(f"{start}")
            else:
                output.append(f"{start}->{stop}")
            output.append(f"{nums[i]}")
        elif nums[i] == nums[i - 1] + 1:
            stop = nums[i]
        elif start == stop:
            output.append(f"{start}")
            start = nums[i]
            stop = nums[i]
        else:
            output.append(f"{start}->{stop}")
            start = stop = nums[i]

    print(output)

