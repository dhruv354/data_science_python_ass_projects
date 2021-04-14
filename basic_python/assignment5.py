
#taking a list from user
#size
n = int(input('Enter your list size: '))
nums = input()
# for i in range(0, n):
#     num = raw_input()
#     my_list.append(num)

nums = nums.split('Enter your input list : ')
my_list = [int(num) for num in nums]
# print(nums)

#function to check prime number

def isPrime(num):
    num_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            num_divisors += 1
    if num_divisors == 1:
        return True
    return False

#return a list of prime numbers from our list
def returnPrimeList(my_list):
    output = [i for i in my_list if isPrime(i)]
    print(output)
returnPrimeList(my_list)