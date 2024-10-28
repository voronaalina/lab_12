num = int(input("Введіть натуральне число:"))

def print_digits(number):
    for digit in str(number):
        print(digit)
        
def digits_descending_order(number):
    for digit in sorted(str(number), reverse=True):
        print(digit)
    
print("Усі цифри числа ")
print_digits(num)

print("цифри у порядку спадання: ")
digits_descending_order(num)  
