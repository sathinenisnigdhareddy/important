   ;sum of n natural numbers
   data segment
    num1 db 01h ;db is for define the byte
    sum db dup<0>;means duplicate with 0
    data ends; 
   code segment
    assume cs:code,ds:data;linking user defines segments to memory segments
    start:mov ax,data
          mov ds,ax
          
          mov al,0Ah  ;sum of 10 natural numbers
          mov cl,al   ;cl register works as a counter
          
          run:mov al,num1
              add al,sum
              mov sum, al
              
              inc num1
          loop run   ;loop will run based on cl register
          hlt
          
          
     end start
    code ends ;