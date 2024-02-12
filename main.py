
# Exercise #1
# Build a function that takes two parameters
# Parameters: List(int), num(int)
# From the list of integers, find the two numbers
# that adds up to the num
# If an answer exist: return True
# If no possible answer: return False

def twoSum(num_list, sum):
    num_list.sort() # O(nln(n))
    # initialize left and right index
    left = 0
    right = len(num_list) - 1

    while(left < right): # O(ln(n))
        answer = num_list[left] + num_list[right] # O(1)
        if(answer == sum):
            return True
        elif(answer > sum):
            right -= 1
        else:
            left += 1
    return False

    # put every number into dictionary (key = index, number = value)
    # hold onto first number, take the sum and minus that first number,
    # difference = sum - first_number
    # if difference is found in dict: return true
    # else: hold another number and try again

result = twoSum([1,2,4,5], 8)
assert result == False
result1 = twoSum([2,4, 47, 27, 1], 28)
assert result1 == True


# Exercise #2
# Given list of strings: ["hello", "help", "hell"]
# Find the longest common prefix string amongst the list of strings

def longestCommonPrefix(strings): # Return the longest prefix string
    pass
    # create an empty string
    # go through each character in shortest_word--> for-loop
    # go through each word in list --> for-loop
    # check if letter equals to the next
    # if not: return string
    # if so: add to empty string

strings = ["hello", "help", "hell", "heeeeee", "heel", "hi"]
print(strings[0][0])    # gets first letter in hello
print(strings[1][0])    # gets first letter in help
print(strings[2][0])    # gets first letter in hell














