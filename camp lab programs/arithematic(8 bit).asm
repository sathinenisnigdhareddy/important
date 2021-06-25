 ;Arithematic operationson 8 bit data
 data segment
    num1 db 06h;db means define the byte
    num2 db 04h
    sum db dup<0>; dup<0) means duplicate with 0
    diff db dup<0>               /
    product db dup<0>
    division db dup<0>
 data ends;      
 code segment
    assume cs:code,ds:data
    start: mov ax,data
           mov ds,ax
           mov al,num1
           add al,num2
           mov sum,al
           
           mov al,num1
           sub al,num2
           mov diff,al
           
           mov al,num1
           mul num2
           mov product,al
           
           mov al,num1
           div num2
           mov division,al
           
           hlt ;end of instructions
    end start           
 code ends;