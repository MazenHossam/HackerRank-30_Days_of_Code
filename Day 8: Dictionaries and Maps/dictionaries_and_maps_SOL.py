import sys

n = int(input())

phonebook={}
for _ in range(n):
    name,num= input().split()
    phonebook[name]=num

requests=[]
while True:
    input_ = sys.stdin.readline().replace('\n', '')
    if input_ == '':
        break
    requests.append(input_)
        
for i in requests:
    if i in phonebook:
        print("{}={}".format(i , phonebook[i]))
    else:
        print("Not found")
