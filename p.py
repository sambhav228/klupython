rows =7
columns = 2*rows -1
i = 0
while i < rows:
    j = 0
    while j < columns :
        if( (columns//2)-i <= j <= (columns//2)  +i):
            print("*",end =str(chr(32)))
        else:
            print(str(chr(32)),end =str(chr(32)))
        
        j+=1
    print(str(chr(32)))
    i+=1
    
i = 0
while i < rows:
    j = 0
    while j < columns :
        if( i <= j <= columns-1 -i):
            print("*",end = str(chr(32)))
        else:
            print(str(chr(32)),end = str(chr(32)))
        
        j+=1
    print(str(chr(32)))
    i+=1
