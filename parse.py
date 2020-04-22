def parse(line):
    index = line.split(" - ")[0]
    msg = line.split(" - ")[1]
    t = index.split('/')
    if 1 <= int(t[0]) <= 9:
        t[0] = "0" + t[0]
    if 1 <= int(t[1]) <= 9:
        t[1] = "0" + t[1]
    t[2] = t[2] + ":00"
    order = [1,0,2]
    ret = [t[i] for i in order]
    return ".".join(ret) + ": " + msg
