import TK_1
import TK_2
import TK_3
import TK_4
import importlib


def main():
    TK_5 = importlib.import_module('TK-5')
    test_list = TK_1.input_data_to_list(5)
    print(test_list)
    print(TK_2.search_min_max_value_in_list(test_list))
    print(TK_3.list_mean_value(test_list))
    print(TK_4.list_multi_values_with_mean_value(test_list))
    print(TK_5.list_square_root_values(test_list))


if __name__ == '__main__':
    main()
