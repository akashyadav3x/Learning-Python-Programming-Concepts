
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, 'r')
count = 0
avg = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1

    for i in line.split():
        try:
            i = float(i)
            if type(i) != str:
                avg += i

        except:
            continue

print("Average spam confidence:", avg/count)
