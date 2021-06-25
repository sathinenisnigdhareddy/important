def count_digits(number,digits):
    i=0
    while(number!=0):
       temp= number%10       
       digits.append(temp)
       i=i+1
       number=number//10
    return i    

def dec_to_bcd(digits,bcd,n):
    for i in range(n):
        bcd[(4*i)]=((digits[i] >> 3) & 1)
        bcd[(4*i)+1]=((digits[i] >> 2) & 1)
        bcd[(4*i)+2]=((digits[i] >> 1) & 1)
        bcd[(4*i)+3]=(digits[i] & 1)
        print('list=',bcd)
    return bcd    
        
       
    
number=int(input("Enter the positive whole decimal number to be converted into BCD:\t\n"))
digits=[]
n=count_digits(number,digits)
digits.reverse()
bcd=[]
for i in range(4*n):
    bcd.append(0)
print('n',n)
print('bcd',bcd)
print('digits',digits)
dec_to_bcd(digits,bcd,n)
for i in range(4*n):
    if i%4 == 3:
       print(bcd[i],end=" ")
    else:  
       print(bcd[i],end="")






