
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

    # O(n)

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

def longestCommonPrefix(strings):  # return the longest prefix string
    shortest = 9999             # O(1)
    for x in strings:           # O(n)
        if len(x) < shortest:
            shortest = len(x)
    # by here shortest word length is found
    prefix = ""
    for y in range(shortest):   # O(n^2)
        letter_y = strings[0][y]
        for x in range(len(strings)):   # O(n)
            # print(strings[x][y])
            temp = strings[x][y]
            if temp != letter_y:
                return prefix
        prefix += letter_y

    # create an empty string
    # go through each character in shortest_word--> for-loop
    # go through each word in list --> for-loop
    # check if letter equals to the next
    # if not: return string
    # if so: add to empty string

    # More optimal solution
    # 1. Sort the list of strings alphabetically
    # 2. check first and last word for longest common prefix
    # 3. Return longest

# strings = ["hello", "help", "hell"]
# print(strings[0][0])    # gets first letter in hello
# print(strings[1][0])    # gets first letter in help
# print(strings[2][0])    # gets first letter in hell


solution = longestCommonPrefix(["hell", "hello", "help"])
assert solution == "hel"


# Exercise #3
# Best time to buy and sell stock
# input: list of integers --> price of that stock per day
# output: find maximum profit where you will buy from the cheapest and sell at a later time

def maxProfit(prices):
    # profit = 0
    # for each number in prices:
    #   temp = number
    #   for every number after temp:
    #       get diff between number and temp
    #       update profit variable
    # return profit

    # O(n * m)
    # profit = 0
    # for x in range(len(prices)): # O(n)
    #     temp = prices[x]
    #     for y in range(x+1, len(prices)):  # O(m)
    #         diff = prices[y] - temp
    #         if diff > profit:
    #             profit = diff
    # return profit

    # Goal: O(n)
    # loop through each number in list
    # at each iteration, update the maximum profit
    # AND find out minimum price
    # maximum profit = max(profit, number-minimum)
    minimum = prices[0]
    profit = 0
    for price in prices[1:]:
        profit = max(price-minimum, profit)
        minimum = min(price, minimum)

    return profit

profit = maxProfit([7,1,5,3,6,4])
assert profit == 5

profit = maxProfit([7,6,4,3,1])
assert profit == 0


# Exercise #4
# Merge and sort two lists
# Given two lists, merge them into one list and sorted

def bubbleSort(final_list): # O(N^2)
    for x in range(len(final_list)):
        for y in range(len(final_list) - x - 1):
            if (final_list[y] > final_list[y + 1]):
                # QUICK SWAP
                # a, b = b, a
                final_list[y], final_list[y + 1] = final_list[y + 1], final_list[y]
    return final_list

def selectionSort(list): # O(N^2)
    # repeatedly selects the smallest element from list and
    # swaps it with first element (or index)
    # Loops through input list
    for x in range(len(list)):
        # Find smallest element to swap
        smallest = x
        for y in range(x+1, len(list)):
            if(list[smallest] > list[y]):
                smallest = y

        # Conduct swapping here since smallest is found
        list[x], list[smallest] = list[smallest], list[x]
    return list

def insertionSort(list): # O(N^2)
    # it attempts to maintain ascending order
    for x in range(1, len(list)):
        key = list[x]

        # Loop to move element to proper place
        index = x - 1
        while key < list[index]:
            list[index+1] = list[index]
            index -= 1
        list[index+1] = key
    return list

# index = 2
# key = 5
# 5 < list[2] --> yes
# list[3] = 13
# index = 1
# 5 < list[1] --> yes
# list[2] = 12
# index = 0

# [38, 27, 43, 10]
# [38, 27]          [43, 10]
# [38] [27]         [43]  [10]
# [27, 38]          [10, 43]

def mergeSort(list):
    if len(list) > 1:
        mid = len(list)//2
        left = list[0:mid]
        right = list[mid:]

        mergeSort(left)
        mergeSort(right)

        #### Algorithm of mergesort
        # [38] [27]
        x = 0
        y = 0
        z = 0
        while x < len(left) and y < len(right):
            if left[x] <= right[y]:
                list[z] = left[x]
                x += 1
            else:
                list[z] = right[y]
                y += 1
            z += 1
        while x < len(left):
            list[z] = left[x]
            x += 1
            z += 1
        while y < len(right):
            list[z] = right[y]
            y += 1
            z += 1

    return list

def mergeSortList(list1, list2):
    final_list = list1 + list2
    return mergeSort(final_list)

# [1,5,3,2]
# [1,5,3,2]
# [1,2,3,5]

answer = mergeSortList([1,3,5,7], [2,4,6,8])
print(answer)
# assert answer == [1,2,3,4,5,6,7,8]


