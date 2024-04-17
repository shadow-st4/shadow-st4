def bigger(num1, num2):
    mylist = [num1, num2]
    print(f'biggest number is: {max(mylist)}')

def smaller(num1, num2):
    mylist = [num1, num2]
    print(f'smallest number is: {min(mylist)}')

input1 = int(input('please enter first number: '))
input2 = int(input('please enter second number: '))

bigger(input1, input2)
smaller(input1, input2)
