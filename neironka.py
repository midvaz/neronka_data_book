with open('new_book.txt','r', encoding='utf-8') as file:
    with open('new_test.txt','w', encoding='utf-8') as new_file:
        r = file.readlines()
        count = -1
        for i in r:
            if i != '':
                count +=1
                print(count)
                i = i.lstrip()
                i = i.lower()
                i = i.replace("\n",'')
                i = i.replace("."," .PERIOD \n")
                i = i.replace(","," ,COMMA ")
                i = i.replace(":"," :COLON")
                i = i.replace(";"," ;SEMICOLON")
                i = i.replace("?"," ?QUESTION \n")
                i = i.replace("!"," !EXCLAMATION \n")
                i = i.replace("..."," ...ELIPSIS \n")

                new_file.write(i)
        # except Exception as e:
        #     print('erroe is: ', e)