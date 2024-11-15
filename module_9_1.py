def apply_all_func(int_list, *function):
    results = dict()
    for i in function:
        results.update({i.__name__: i(int_list)})
    return   results

print(apply_all_func([5,2,3],max, min, sum, len, sorted))