# coding: utf-8


num_string = '99,100,201,101,9999,2,5,6'
string_num_arr = num_string.split(',')
num_list = list(map(int, string_num_arr))
minmum_100_list = list(filter(lambda v: v > 100, num_list))
minmum_100_list.sort(reverse = True)
string_minmum_100_list = list(map(str, minmum_100_list))
answer = ' '.join(string_minmum_100_list)
print(answer)
