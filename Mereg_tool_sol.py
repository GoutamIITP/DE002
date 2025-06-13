def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        unique_list = []
        str_list = list(string[i:i+k])
        for c in str_list:
            if c not in unique_list:
                unique_list.append(c)
        print("".join(unique_list))