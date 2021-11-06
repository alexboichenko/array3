def input_data_to_list(size_list: int):
    try:
        user_list = []
        for i in range(size_list):
            user_list.append(int(input(f'Input number in list[{i}]: ')))
        return user_list
    except ValueError:
        print('You input wrong value, list is not be created')
