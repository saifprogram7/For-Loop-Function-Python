def cubingvalueuserinput(base_number, power_number):
    result = 1
    for i in range (power_number):
        result = result * base_number
    return result
print(cubingvalueuserinput(2, 2))
