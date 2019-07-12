

unit_dic ={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand',0:''}


def word(n):
    result = None
    try:
        if n < 10 or unit_dic.get(n):
            if unit_dic.get(n)[0] + unit_dic.get(n)[1] == ('th'):
                return 'one thousand' 
            elif unit_dic.get(n)[0] + unit_dic.get(n)[1] == ('hu'):
                return 'one hundred'
            return unit_dic.get(n)

        check_len = len(str(n))
        get_num =[str(n) for n in str(n)]
        print("getnum",get_num)
        if check_len == 2:
            result = f"{unit_dic.get(int(get_num[0]+'0'))} {unit_dic.get(int(get_num[1]))}"
        elif check_len == 3:
            if get_num[1:]==['0','0']:
                result = f"{unit_dic.get(int(get_num[0]))} {unit_dic.get(int(100))}"
                return result.rstrip()

            elif int(get_num[1])> 0 and int(get_num[2]) == 0:
                    result = f"{unit_dic.get(int(get_num[0]))} {unit_dic.get(100)} and  {unit_dic.get(int(get_num[1] +'0'))}"
                    return result.rstrip()

            result = f"{unit_dic.get(int(get_num[0]))} {unit_dic.get(100)} and {unit_dic.get(int(get_num[1]+ '0')if int(get_num[1]) > 1 else int(get_num[1]+ get_num[2]))} {unit_dic.get(int(get_num[2]))if int(get_num[1]) > 1 else ''}"
        
        return result.rstrip()
    except:
        print('error')

print(word(205))

