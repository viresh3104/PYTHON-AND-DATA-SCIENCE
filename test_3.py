import numpy as np


curr_list = ['INR' ,'USD','EURO','KUWAIT DINAR','DIRHAM']
print(curr_list)
input_curr = input('Select the input curr type from above ::').upper()
amount = float(input('Enter the amount to be converted :: '))


conversion_curr = input('Select the input curr type from above ::').upper()


if (input_curr == 'INR') :                                        #for INR
    if(conversion_curr == 'USD'):
        output = float(amount * 0.012)
        print(f"{amount} in USD IS {output}")

    elif(conversion_curr == 'EURO'):
        output = float(amount * 0.011)
        print(f"{amount} in EURO IS {output}")

    elif(conversion_curr == 'KUWAIT DINAR'):
        output = float(amount * 0.003672)
        print(f"{amount} in KUWAIT DINAR IS {output}")

    elif(conversion_curr == 'DIRHAM'):
        output = float(amount * 0.044)
        print(f"{amount} in DIRHAM IS {output}")

    else : 
        print(f"{amount} in INR IS {amount}")



elif (input_curr == 'USD') :                                        #for USD
    if(conversion_curr == 'INR'):
        output = float(amount * 83.53)
        print(f"{amount} in INR IS {output}")

    elif(conversion_curr == 'EURO'):
        output = float(amount * 0.93)
        print(f"{amount} in EURO IS {output}")

    elif(conversion_curr == 'KUWAIT DINAR'):
        output = float(amount * 0.31)
        print(f"{amount} in KUWAIT DINAR IS {output}")

    elif(conversion_curr == 'DIRHAM'):
        output = float(amount * 3.67)
        print(f"{amount} in DIRHAM IS {output}")

    else : 
        print(f"{amount} in USD IS {amount}")



elif (input_curr == 'EURO') :                                        #for EURO
    if(conversion_curr == 'INR'):
        output = float(amount * 89.68)
        print(f"{amount} in INR IS {output}")

    elif(conversion_curr == 'USD'):
        output = float(amount * 1.07)
        print(f"{amount} in USD IS {output}")

    elif(conversion_curr == 'KUWAIT DINAR'):
        output = float(amount * 0.33)
        print(f"{amount} in KUWAIT DINAR IS {output}")

    elif(conversion_curr == 'DIRHAM'):
        output = float(amount * 3.94)
        print(f"{amount} in DIRHAM IS {output}")

    else : 
        print(f"{amount} in EURO IS {amount}")


elif (input_curr == 'KUWAIT DINAR') :                                        #for KUWAIT DINAR
    if(conversion_curr == 'INR'):
        output = float(amount * 272.35)
        print(f"{amount} in INR IS {output}")

    elif(conversion_curr == 'USD'):
        output = float(amount * 3.26)
        print(f"{amount} in USD IS {output}")

    elif(conversion_curr == 'EURO'):
        output = float(amount * 3.04)
        print(f"{amount} in EURO IS {output}")

    elif(conversion_curr == 'DIRHAM'):
        output = float(amount * 11.98)
        print(f"{amount} in DIRHAM IS {output}")

    else : 
        print(f"{amount} in KUWAIT DINAR IS {amount}")

elif (input_curr == "DIRHAM"):
    if(conversion_curr == 'INR'):
        output = float(amount * 22.74)
        print(f"{amount} in INR IS {output}")

    elif(conversion_curr == 'USD'):
        output = float(amount * 0.27)
        print(f"{amount} in USD IS {output}")

    elif(conversion_curr == 'EURO'):
        output = float(amount * 0.25)
        print(f"{amount} in EURO IS {output}")

    elif(conversion_curr == 'KUWAIT DINAR'):
        output = float(amount * 0.083)
        print(f"{amount} in DIRHAM IS {output}")

    else : 
        print(f"{amount} in DIRHAM IS {amount}")

else:
    if (input_curr not in curr_list) or (conversion_curr not in curr_list):
        print("wrong input type , enter again.")
    
    










