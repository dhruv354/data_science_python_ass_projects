def factor(num):
    #base cases
    if num < 0:
        return 'Not Defined'
    if num <= 1:
        return 1
    return num * factor(num-1)

# print(factor(5))
def check_string(string):
    if 's' in string:
        print('string is containing letter s')
    else:
        print('string is not containing letter s')
        
class student():
    
    def fun1(self, num):
        print(num)
    
    
    
        