import sys
s = str(int(str((int(''.join([str(ord(i)) for i in open(sys.argv[1], 'r').read() if i.isalpha()])) + 1) * 2004582342310635843922)[-22:]) + 2907326189180680668794)
i = 0
while i < 22:
    sys.stdout.write(chr(int(s[i:i+2])))
    i += 2
