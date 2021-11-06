def input_data_to_list(size_list: int):
    user_list = []
    for i in range(size_list):
        user_list.append(input(f'Input data in list[{i}]: '))
    return user_list
