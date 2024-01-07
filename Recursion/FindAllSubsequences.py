def subsequences(string):
    if string == "":
        return [""]
    first_char = string[0]
    sub_list = subsequences(string[1:])
    final_list = list()
    for sub_string in sub_list:
        final_list.append(first_char + sub_string)
    final_list += sub_list
    return final_list

string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)
