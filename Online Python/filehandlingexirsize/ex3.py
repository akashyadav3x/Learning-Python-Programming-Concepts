a = 'X-DSPAM-Confidence: 89.98'

for i in a.split():
    try:
        i = float(i)
        if type(i) != str:
            print(i)

    except:
        #print("error occured")
        continue
    # print(i)
