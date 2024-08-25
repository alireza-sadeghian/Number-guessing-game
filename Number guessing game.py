import random as rand
while(True):
    try:
        num = rand.randint(1,20)
        inp_num = int(input("عددی بین 1 تا 20 وارد کن"))
        if inp_num == 0 :
            break
        while(True): 
            if inp_num == num:
                print("آفرین درست حدس زدی")
                break
            else :
                if inp_num > num:
                    pain = int(input("یکم بیا پایین تر"))
                    inp_num = pain
                elif inp_num < num:
                  bala = int(input("یکم بیا بالا تر"))
                  inp_num = bala

    except:
        print("خطا، لطفا عدد وارد کنید")
        
print("بازی تمام شد")
#علیرضا صادقیان