infile = open('ko_charset/ahn_b.txt', 'r')
outfile = open('korea.txt', 'w')
a = infile.read()
import random


for j in range(1000000):
    lenght = random.randrange(1, 7)
    out_str = ''
    for i in range(lenght):
        idx =  random.randrange(0, len(a))
        out_str += a[idx]
    out_str += '\n'
    outfile.write(out_str)
