def create_list(number_range):
    num_list = []
    for i in range(number_range):
        new_num = input('Enter a number: ')
        num_list.append(new_num)
    return num_list


def max_func(num_list):
    result = num_list[0]
    for num in num_list:
        if num > result:
            result = num
    return result


number_amount = input('Enter a number amount: ')


print(max_func(create_list(number_amount)))
