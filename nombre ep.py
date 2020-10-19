                                                        """           #mathématiques orsay            """
N = 10
repetition = 0
condition = 1
while condition != 0:
    
    length = len(str(N))+1                          #future length of the list containing D AND N together
    
    for dpos in range(1, length-1):                 #nb of conditions to be checked depending on the length of the number
        
        for D in range(1,10):
            
            li = [0]*length                         #creates list with a number 'length' of 0s
            a = [str(D) for D in str(N)]            #converts the Nb N into a list containing all of it's individual characters in a different spot

            for box in range(length):
                
                if box == dpos:                     #if the indices are the same, put the D in that spot
                    li[box] = str(D)
                    
                else:
                    li[box] = a[box]

            concatenation = int(''.join(li))        #converts all the elements in the list into one integer

            if concatenation%D==0:
                repetition +=1
            
    if repetition == 9:
        condition = 0                               #found answer
        break

    else:
        repetition = 0                              #reset repetition counter
        
    N+=10                                           #if find properties then make sure to change the ten to a bigger number so that the computer can go faster

print(N)


#sandbox

while box < length:
    if box == dpos:
        li[box] = str(D)
    
