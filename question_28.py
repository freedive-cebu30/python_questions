# coding: utf-8


string_country = "ph-cebu, japan-tokyo, japan-osaka, Taiwan-taipei, japan-kyoto"

arr_country = string_country.split(',')
arr_no_blank_country = [v.strip() for v in arr_country]
arr_japan = [v for v in arr_no_blank_country if v.startswith('japan')]
arr_big_letter_japan = list(map(str.capitalize, arr_japan))
answer = ','.join(arr_big_letter_japan)
print(answer)
