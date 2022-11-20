def encipherment(data,excursion_left):
    alpha='abcdefghijklmnopqrstuvwxyz'
    def indexinstr(aim,thestr=alpha):
        for i in range(len(thestr)):
            if thestr[i]==aim:
                return i
    out=''
    for i in data:
        if i.isalpha():
            place=indexinstr(i)
            out+=alpha[place-excursion_left]
        else:
            out+=i
    return out
print(encipherment('woshiyigeshabi',11))