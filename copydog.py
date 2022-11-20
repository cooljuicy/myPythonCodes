from pyperclip import copy
while True:
    quest=input('?')
    if quest=='1':
        copy(r'C:\Users\liuchenyue\Desktop')
    elif quest=='21':
        copy('pyinstaller -F')
    elif quest=='22':
        copy('pyinstaller -F -w')