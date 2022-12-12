def sum_csv(file):
    x = open(file)
    l = []
    for line in x:
        elements = line.split (",")
        l.append(elements[1])
    x = 0
    for n in l[1:]:
        try:
            x += float(n)
        except ValueError:
            continue
    if x == 0:
        return None
    return x
