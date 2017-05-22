"""
interact w/ file system
====
via file objects

* some _thing_ (object - data and methods/actions)
* that represents an actual file
* and allows you to read/write/manipulate the data in that file

how do we get a file object?

* use open
* 2 parameters
    * name of file (a string)
    * "mode" -> 'r', 'w', 'a' (a string)
    * what's the difference write and append
        * write overwrites file, append adds to it
        * for write and append, if file doesn't exist, it'll get created
* return a file object
"""

"""
file_object = open('/tmp/class28/test.txt', 'r')
result = file_object.read().strip()
lines_list = result.split('\n')
print(lines_list)
for line in lines_list:
    print(line + "!")
"""
"""
file_object = open('/tmp/class28/test.txt', 'r')
lines_list = file_object.readlines()
print(lines_list)
for line in lines_list:
    print(line.strip() + '!')
"""
"""
file_object = open('/tmp/class28/test.txt', 'r')
for line in file_object:
    print(line.strip() + '!')
"""

"""
file_object = open('/tmp/class28/test.txt', 'r')
line1 = file_object.readline()
print('line1', line1)
line2 = file_object.readline()
print('line2', line2)
line3 = file_object.readline()
print('line3', line3)
line4 = file_object.readline()
print('line4', line4)
line5 = file_object.readline()
print('line5', line5)
"""
"""
file_object = open('/tmp/class28/test.txt', 'r')
while True:
    line = file_object.readline()
    if len(line) == 0:
        break;
    print(line)
"""
"""
input:
100,20,39
10,1,87

8,8,8

output (to a file called out.txt):
100
87

8
"""

file_object = open('/tmp/class28/test.txt', 'r')
file_object_out = open('/tmp/class28/out.txt', 'w')
for line in file_object:
    line = line.strip()
    """extract the data from the line"""
    line_parts = line.split(',')
    """ handle a list that looks like ['']"""
    if line_parts[0] == "":
        # write out a new line to file
        file_object_out.write('\n')
        continue
    else:
        max_number = int(line_parts[0])
        for element in line_parts:
            if int(element) > max_number:
                max_number = int(element)
        file_object_out.write(str(max_number) + '\n')
        # write out max number to new file
file_object.close()
file_object_out.close()












