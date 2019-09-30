#Python file input and Output
import sys

def rememberer(thing):
    #open file
    # file = open("remember.txt", 'a')
    #     #write thing to file
    # file.write(thing+"\n")
    # #close file
    # file.close()
    #SAME AS USING WITH BELOW


    with open("remember.txt", 'a') as file:
        #write thing to file
        file.write(thing+"\n")

# if __name__ == '__main__':
#     rememberer(input("What should i remember? "))


def show():
    #open file
    #print out each line in file
    #close file
    with open("remember.txt") as file:
        for line in file:
            print(line)


if __name__ == '__main__':
    if sys.argv[1].lower() == '--list':
        show()
else:
    rememberer(' '.join(sys.argv[1:]))
