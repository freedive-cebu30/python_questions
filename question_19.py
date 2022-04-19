# coding: utf-8

string_list = ["1", "12", "12", "13", "2", "3", "4", "5", "6", "7", "8", "9", "10", "5", "4", "3"]
int_list = list(map(int, string_list))

ascending_order_int = sorted(int_list)
print(ascending_order_int)

ascending_order_string = sorted(string_list)
print(ascending_order_string)
