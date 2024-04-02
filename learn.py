with open('myfile.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)