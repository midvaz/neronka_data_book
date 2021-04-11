print("start")

with open("avidreaders.ru__graf-monte-kristo.txt","r", encoding='utf-8') as file :
    with open("new_avidreaders.ru__graf-monte-kristo.txt","w", encoding='utf-8') as new_file:
            r =file.readlines()
        
        # try:
            count = -1
            for i in r :
                count +=1
                print(i)
                if i != '\n':
                    i = i.lower()
                    i.split('.')
                    if  i.find(',') != -1:
                        pass
                    new_file.write(i)
print("end")

        # except Exception as e:
        #     print('erroe is: ', e)