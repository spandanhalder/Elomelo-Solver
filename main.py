#!/usr/bin/python3

def isMatched(a, b, n):
    l = list(b)
    for i in a:
        if i in l:
            l.remove(i)
            continue
        else:
            return False
    if(len(l) == n):
        return True
    else:
        return False

n = int(input("Enter extra characters to be searched: "))
input_count = 1
with open("INP.txt","r",encoding="utf-8") as r:
    with open("WORDLIST.txt","r",encoding="utf-8") as d:
        with open("OUT.txt","w",encoding="utf-8") as w:
            ip_line = r.read().splitlines()
            d_line = d.read().splitlines()
            for x in ip_line:
                count = 0
                for y in d_line:
                    if(isMatched(x,y,n)):
                        w.write(str(input_count)+ ": " + str("".join(y)) + '\n')
                        count += 1
                print("Found Words:", count)
                input_count += 1