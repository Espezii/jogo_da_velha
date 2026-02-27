print ("Jogo da velha X inicia",'\n1_|2_|3_','\n4_|5_|6_'+ '\n7 |8 |9')
t=1
dic={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
while t <=9:
    if t%2==0:
        xo = "O"
    else: xo ="X"    
    
    pos = input("Qual posição:")

    dic[int(pos)] = str(xo)
       
    print (f'\n{dic[1]}_|{dic[2]}_|{dic[3]}_ \n{dic[4]}_|{dic[5]}_|{dic[6]}_ \n{dic[7]} |{dic[8]} |{dic[9]}')
    t=t+1
    if dic[1] == dic[2] == dic[3] or dic[1] == dic[4] == dic[7] or dic[1] == dic[5] == dic[9] :
        print(f'{dic[1]} Venceu')
        break
    elif dic[9] == dic[6] == dic[3] or dic[9] == dic[8] == dic[7] :
        print(f'{dic[9]} Venceu')
        break
    elif dic[4] == dic[5] == dic[6] or dic[2] == dic[5] == dic[8] or dic[3] == dic[5] == dic[7] :
        print(f'{dic[5]} Venceu')
        break
else: print ("EMPATE")
