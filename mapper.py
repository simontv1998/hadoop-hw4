import sys

for line in sys.stdin:
    line = line.strip()
    temperature = int(line[87:92])
    if (temperature == 9999):
        continue
    qualityFlag = int(line[92])
    if (qualityFlag != 0 and qualityFlag != 1 \
        and qualityFlag != 4 and qualityFlag != 5 \
        and qualityFlag != 9):
        continue
    print('%s\t%d' % (line[15:23], int(line[87:92])))