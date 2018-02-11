def file_read(file_name):
    try:
        f = open(file_name, 'r')
    except IOError:
        return 404
    else:
        dots_list = [[int(x) for x in list(line[:-1].split())] for line in f]
        return dots_list