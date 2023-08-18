import time
a = [5,2,3,4,10,11,5,2,3,4,10,11]
b = [5,7,26,5,7,26]
c = []

start_time = time.time()
for h in b:
    h_append = False
    i_break = False
    for i in a:
        if i_break:
            break
        j_break = False
        for j in a:
            if j_break:
                break
            for k in a:
                if i+j+k == h:
                    c.append(1)
                    h_append = True
                    i_break = True
                    j_break = True
                    break
    if not h_append:
        c.append(0)
end_time = time.time()

print(f"Process time: {end_time - start_time} sec")
print("c :",c)

