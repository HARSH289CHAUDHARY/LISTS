# list1=[3, 4, 10, 9, 18, 66, 13, 15]
# evenNum=list1(filter(lambda i : i>5, list1))
# print(evenNum)

# squareNum = list1(map(lambda i,j : i + 2, list1))
# print(squareNum)
# def isEven(i):
#     return i%2==0




# list1  = [10,20,30,40,50]
# tripleNum = list(map(lambda i : i*3, list1))
# print(tripleNum)


# list2  = ["a","B","c","D","e"]
# capital = list(map(lambda i :i.swapcase()))
# print(capital)


def div(a,b):
    print(a/b)

def good_div(func):
    def inner_div(a,b):
        if a < b:
            a,b=b,a
        return func(a,b)    
    return inner_div
 
output = good_div(div)
div(2,4)   