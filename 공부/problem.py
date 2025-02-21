# newfile.py
f = open("/Users/jh/shuttle-app/doit.txt", 'w')
for i in range(1,11):
    data = '%d번째 줄입니다. \n'%i
    print(data) 