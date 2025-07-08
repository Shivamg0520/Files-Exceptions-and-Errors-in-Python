file = open('output.txt', 'w')
file.write(str(input("Enter text to write to file: ")))
print("Data successfully written to output.txt")
file.close

file = open('output.txt', 'a')
file.write(str(input("Enter additional text to append: ")))
print("Data successfully appended")
file.close()

file = open('output.txt', 'r')
reading_file = file.readlines()
# print(reading_file)
for line in reading_file:
    print("Final content of output.txt", line.strip())
file.close