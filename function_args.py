def input_number(num):
    return int(input("Enter a number: ")) * num

result = input_number(2)
print(result)

def input_number1(num=2):
    return int(input("Enter a number: ")) * num

result2 = input_number1()
print(result2)