import json
import sys

def parse_bpe():
    bpe = {}
    infile = open(sys.argv[1], 'r', encoding='utf-8')
    line = infile.readline()
    i = 0
    bs = list(range(ord("!"), ord("~")+1))+list(range(ord("¡"), ord("¬")+1))+list(range(ord("®"), ord("ÿ")+1))
    remain = []
    for b in range(2**8): # ordinary char
        if b not in bs:
            remain.append(b)
        else:
            bpe[chr(b)] = i
            i += 1
    n = 0
    for b in remain: # control char
        bpe[chr(n+2**8)] = i
        n += 1
        i += 1
    while True:
        line = infile.readline()
        if len(line) == 0 : break
        word = line.split()[0] + line.split()[1]
        print(word)
        bpe[word] = i
        i += 1
    
    outfile = open(sys.argv[2], 'w', encoding='utf-8')
    print( json.dumps(bpe))
    outfile.write( json.dumps(bpe) )


if __name__ == "__main__":
    parse_bpe()