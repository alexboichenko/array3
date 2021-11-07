def list_multi_values_with_mean_value(user_list: list):
    size_list = len(user_list)
    sum_values_list = 0
    for value in user_list:
        sum_values_list += value
    mean_value = sum_values_list/size_list
    list_result = []
    for value in user_list:
        list_result.append(value*mean_value)
    return list_result
