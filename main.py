
# Exercise #1
# Build a function that takes two parameters
# Parameters: List(int), num(int)
# From the list of integers, find the two numbers
# that adds up to the num
# If an answer exist: return True
# If no possible answer: return False

def twoSum(num_list, sum):
    num_list.sort()
    left = 0
    right = len(num_list) - 1
    while(left < right):
        answer = num_list[left] + num_list[right]
        if(answer == sum):
            return True
        elif(answer > sum):
            right -= 1
        else:
            left += 1
    return False



result = twoSum([1,2,5], 7)
assert result == True
result1 = twoSum([2,4, 47, 27, 1], 28)
assert result1 == True

# length of input = n
# O(n^2)
# O(n)







