# This program removes the unnecessary values in the VariableNames.txt file

with open('VariableNames.txt', 'r+',  encoding="utf8") as f:
    contents = f.readlines()


def Remove_Number_Prefix():
    num_Prefix = 1
    with open('final00.txt', 'w', encoding="utf 8") as f:
        for i in contents:
            counter = str(num_Prefix)
            prefix = counter+";"
            temp = i.removeprefix(prefix)
            counter1 = int(counter)
            counter1 += 1
            num_Prefix = counter1
            f.write(temp)


def Remove_API_Prefix():
    with open('final00.txt', 'r+',  encoding="utf8") as f:
        contents = f.readlines()
    with open('final01.txt', 'w', encoding="utf 8") as f:
        for i in contents:
            prefix = "API;"
            temp = i.removeprefix(prefix)
            f.write(temp)


def Remove_DROP_Prefix():
    with open('final01.txt', 'r+',  encoding="utf8") as f:
        contents = f.readlines()
    with open('final02.txt', 'w', encoding="utf 8") as f:
        for i in contents:
            prefix = "DROP:"
            temp = i.removeprefix(prefix)
            f.write(temp)


def Remove_REG_DELETED_Prefix():
    with open('final02.txt', 'r+',  encoding="utf8") as f:
        contents = f.readlines()
    with open('final03.txt', 'w', encoding="utf 8") as f:
        for i in contents:
            prefix = "REG:DELETED:"
            temp = i.removeprefix(prefix)
            f.write(temp)


def Remove_REG_DELETED_Prefix():
    with open('final03.txt', 'r+',  encoding="utf8") as f:
        contents = f.readlines()
    with open('final04.txt', 'w', encoding="utf 8") as f:
        for i in contents:
            prefix = "REG:DELETED:"
            temp = i.removeprefix(prefix)
            f.write(temp)


def Remove_REG_OPENED_Prefix():
    with open('final03.txt', 'r+',  encoding="utf8") as f:
        contents = f.readlines()
    with open('final04.txt', 'w', encoding="utf 8") as f:
        for i in contents:
            prefix = "REG:OPENED:"
            temp = i.removeprefix(prefix)
            f.write(temp)


def Remove_REG_READ_Prefix():
    with open('final03.txt', 'r+',  encoding="utf8") as f:
        contents = f.readlines()
    with open('final04.txt', 'w', encoding="utf 8") as f:
        for i in contents:
            prefix = "REG:READ:"
            temp = i.removeprefix(prefix)
            f.write(temp)


def Remove_REG_WITTEN_Prefix():
    with open('final03.txt', 'r+',  encoding="utf8") as f:
        contents = f.readlines()
    with open('final04.txt', 'w', encoding="utf 8") as f:
        for i in contents:
            prefix = "REG:WRITTEN:"
            temp = i.removeprefix(prefix)
            f.write(temp)


def Remove_FILES_DELETED_Prefix():
    with open('final03.txt', 'r+',  encoding="utf8") as f:
        contents = f.readlines()
    with open('final04.txt', 'w', encoding="utf 8") as f:
        for i in contents:
            prefix = "FILES:DELETED:"
            temp = i.removeprefix(prefix)
            f.write(temp)


def Remove_FILES_OPENED_Prefix():
    with open('final03.txt', 'r+',  encoding="utf8") as f:
        contents = f.readlines()
    with open('final04.txt', 'w', encoding="utf 8") as f:
        for i in contents:
            prefix = "FILES:OPENED:"
            temp = i.removeprefix(prefix)
            f.write(temp)


def Remove_FILES_WRITTEN_Prefix():
    with open('final03.txt', 'r+',  encoding="utf8") as f:
        contents = f.readlines()
    with open('final04.txt', 'w', encoding="utf 8") as f:
        for i in contents:
            prefix = "FILES:WRITTEN:"
            temp = i.removeprefix(prefix)
            f.write(temp)


def Remove_FILES_READ_Prefix():
    with open('final03.txt', 'r+',  encoding="utf8") as f:
        contents = f.readlines()
    with open('final04.txt', 'w', encoding="utf 8") as f:
        for i in contents:
            prefix = "FILES:READ:"
            temp = i.removeprefix(prefix)
            f.write(temp)


"""

with open('Vout2.txt', 'r+',  encoding="utf8") as f:
    contents1 = f.readlines()

new_content = contents0+contents1
"""
# with open('Vout1.txt', 'r+',  encoding="utf8") as f:
#contents = f.readlines()
# print(contents)
# print(contents)

# for i in contents[14737::]:
# print(i)
