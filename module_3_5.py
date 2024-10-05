def get_multiplied_digits(number):
    if len(str(number)) == 1:
        return number
    else:
        number1=str(number)
        int1= int(number1[0])
        int2 = int(number1[1:])
        return int1 * get_multiplied_digits(int2)


print(get_multiplied_digits(40203))