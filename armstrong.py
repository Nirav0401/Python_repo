# number which is sum of the individual number of its digit's power
# 153 = 1^3 + 5^3 + 3^3
def armstrong(num):
    # while(1):
        # num = int(input("Enter the number : \n"))
    number = int(num)
    count = len(str(num))
    # print(count)
    sum = 0
    while(num>0):
        digit = num%10
        sum += digit**count
        num = num//10
        # print(sum)

    if(sum==number):
        print(f"{number} is an armstrong number\n")
    else:
        print(f"{number} is not an armstrong number\n")    

if __name__ == "__main__":
    armstrong(40)



# def armstrong(num):
#     while(1):
#         num = int(input("Enter the number : \n"))
#         number = num
#         count = len(str(num))
#         # print(count)
#         sum = 0
#         while(num>0):
#             digit = num%10
#             sum += digit**count
#             num = num//10
#             # print(sum)

#         if(sum==number):
#             print(f"{number} is an armstrong number\n")
#         else:
#             print(f"{number} is not an armstrong number\n")     