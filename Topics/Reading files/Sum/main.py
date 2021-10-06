# read sums.txt
with open('sums.txt', 'r') as file:

    for line in file:
        nums = line.split(" ")
        print(int(nums[0]) + int(nums[1]))

    file.close()
