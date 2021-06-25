   ;sum of n natural numbers
   data segment
    num1 dw 01h ;db is for define the byte
    sum dw dup<0>;means duplicate with 0
    data ends; 
   code segment
    assume cs:code,ds:data;linking user defines segments to memory segments
    start:mov ax,data
          mov ds,ax
          
          mov ax,0Ah  ;sum of 10 natural numbers
          mov cx,ax   ;cx register works as a counter
          
          run:mov ax,num1
              add ax,sum
              mov sum, ax
              
              inc num1
          loop run   ;loop will run based on cl register
          hlt
          
          
     end start
    code ends ;