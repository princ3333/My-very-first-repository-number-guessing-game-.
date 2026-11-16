import random
ran = random.randint(1,100) 
tries = 0                                           
while True:

    tries = tries + 1
    hum = int(input("Please Enter Your Number:- "))

    if ran == hum :
        print(f"Correct Prediction ! you take {tries} tries. ") 
        break            
    elif ran > hum :                              
        print("Wrong prediction Go Higher ! ")       
    elif ran < hum :                                
        print("Wrong prediction Go Lower ! ")