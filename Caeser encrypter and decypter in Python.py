def incrementer(a,i):
    return(chr(ord(a)+i))
def decrementer(a,i):
    return(chr(ord(a)-i))

def encrypter(message):
    l=len(message)
    for x in range(1,27):
        temp=""		
	for y in range(0,l):
            temp=temp+incrementer(message[y],x)
	print("ROT "+str(x)+" "+temp)
    

def decrypter(message):
    l=len(message)
    for x in range(1,27):
        temp=""		
	for y in range(0,l):
            temp=temp+decrementer(message[y],x)
	print("ROT "+str(x)+" "+temp)


choice=input("WELCOME  \n  Press 1 for encryption and 2 for decryption ")
while(input):
       
    if (choice==1):
        
        text=raw_input("enter the message ")
        encrypter(text)
    
    if(choice==2):
        text=raw_input("enter the encrypted message ")
        encrypter(text)

    choice=input("WELCOME  \n  Press 1 for encryption and 2 for decryption ")

    

    
