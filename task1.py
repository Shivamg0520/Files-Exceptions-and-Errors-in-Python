try:
    file = open('sample.txt', 'r')
    reading_file = file.readlines()
    # print(reading_file)
    for line in reading_file:
        print(line.strip())
    file.close()
except FileNotFoundError:
    print("The file 'sample.txt' does not found.")