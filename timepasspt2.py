import time
# mylist = ["Tanay","Kumar","Python"]
# for id,ele in enumerate(mylist):
#     print(id,ele)
currtime = time.time()
print(currtime)
while True:
    if time.time()-1 == currtime:
        print("1 second")
        currtime = time.time()