import sys
f = open(sys.argv[1], 'r')
c = f.read()
n = ""
for i in c:
    if i.isalpha():
        n += str(ord(i))
s = str(int(str((int(n) + 1) * 2004582342310635843922)[-22:]) + 2907326189180680668794)
i = 0
while i < 22:
    sys.stdout.write(chr(int(s[i:i+2])))
    i += 2
