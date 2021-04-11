with open('test.txt','r', encoding='utf-8') as file:
    r = file.readlines()
    for i in r:
        i.lower()
        print(i)