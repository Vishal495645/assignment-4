# Task 1: Read a File and Handle Errors

'''try:
    with open("smaple.txt", "r") as file:
        for line in file:
            print(line.strip())  # .strip() removes extra newline characters
except FileNotFoundError:
    print("Error: 'smaple.txt' file does not exist.")'''

    #task 2Write and Append Data to a File
data1=input('enter you data: ')
file1=open('output.txt', 'w')
file1.write(data1)
file1.close()
#append more data to same file
data2=input('enter you data: ')
file1=open('output.txt', 'a')
file1.write(data2)

file1.close()
file = open("output.txt", "r")
print("\nFinal content of the file:")
print(file.read())
file.close()
file = open("output.txt", "r")
print("\nFinal content of the file:")
print(file.read())
file.close()
