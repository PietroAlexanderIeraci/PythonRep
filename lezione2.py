def sum_list(lst):
    output = 0
    if not lst:
        return None
    for i in lst:
        if type(i) == int:
            output += i
        else:
            continue
    return output