
original_number='123'



while True:
    
    guess_number=input('Enter your guess number 3 digits number')
    output=[]

    
    if len(original_number)!=len(guess_number):
        print("enter valid input")
        continue
    if len(set(guess_number))<3:
        print("Duplicate number")
        continue


   
    if guess_number==original_number:
        print('Fermi'*3)
        break

    
   
    for i in range(len(original_number)):
        if guess_number[i]==original_number[i]:
            output.append('Fermi')
    for x in guess_number:
        for y in original_number:
            if x==y:
                print('Pico')


 
    for j in range(len(output)):
        output_string=[]
        output_string.append(output[j])    



    if len(output)==0:
        print('Bagel')
