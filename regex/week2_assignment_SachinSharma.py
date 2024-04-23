#Program to find numbers in a file, calcualte their sum. Part of week2 assignment
#Author: Sachin Sharma
#email: sachin19183@gmail.com

import re
def calculateSum(numlist):
    if numlist == []:
        return numlist
    return sum(numlist)

def appendToList(numlist, nums):
    for n in nums:
        n=int(n)
        numlist.append(n)
    return numlist

def readDataFromFile(numlist):
    try:
        #with open('regex_sum_42.txt', 'r') as fh:
        with open('regex_sum_1995614.txt','r') as fh:
            for line in fh:
                line = line.rstrip()
                nums = re.findall('[0-9]+',line)   # nums is  a list containing all numbers in this line
                if nums:
                    appendToList(numlist,nums)
            return numlist
    except FileNotFoundError:
        print("The file does not exist")
    except Exception as e:
        print(" There is an error {e} ")

def main():
    print("This is week2 assignment program which reads data from file, fins any numbers and sums them up")
    numlist= []
    numlist = readDataFromFile(numlist)
    sum = calculateSum(numlist)
    print(sum)

if __name__ == '__main__':
    main()

