def longest_al_sub(string):
    # return a list of the longest alphabetical substrings in the specified string
    n = len(string)
    i = j = 0
    max_len = 0

    while i <= n - 1:
        temp_len = 0
        while True:
            temp_len += 1
            j += 1
            if  j > n - 1 or string[j] < string[j - 1]:
                break
        if temp_len > max_len:
            max_len = temp_len
            list_of_sub = [string[i:j]]
        elif temp_len == max_len:
            list_of_sub.append(string[i:j])
        i = j
        
    return list_of_sub

