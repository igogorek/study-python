def unique(integers):
    res = []
    for num in integers:
        if res.count(num) == 0:
            res.append(num)
    return res