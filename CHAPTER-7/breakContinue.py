print("---------Break Keyword---------")
for i in range(10):
    if(i==5):
        break # exit the loop right now
    print(i)

print("---------Continue Keyword---------")
for i in range(10):
    if(i==5):
        continue # skip the loop iteration
    print(i)