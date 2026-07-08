import subprocess

while True:
    args = input("kabimaru-dev@MacBook-Pro ~ % ")
    string_array = []
    string = ''

    for i in range(len(args)):
        if args[i] == " ":
            string_array.append(string)
            string = ''
        else:
            string += args[i]

    if(len(string) > 0):
        string_array.append(string)
        string = ''


    # print(string_array)
    try:
        subprocess.run(string_array)
        
    except:
        if not (string_array == ['exit']):
            print("Wrong writing command, please check the output step by step: ")
            print(string_array)
        else:
            print("Use 'CTRL + C' for exit")
    