   ;Arithematic operationson 16 bit data
 data segment
    num1 dw 0006h;db means define the byte
    num2 dw 0004h
    sum dw dup<0>; dup<0) means duplicate with 0
    diff dw dup<0>               /
    product dw dup<0>
    division dw dup<0>
 data ends;      
 code segment
    assume cs:code,ds:data
    start: mov ax,data
           mov ds,ax
           mov ax,num1
           add ax,num2
           mov sum,ax
           
           mov ax,num1
           sub ax,num2
           mov diff,ax
           
           mov ax,num1
           mul num2
           mov product,ax
           
           mov ax,num1
           div num2
           mov division,ax
           
           hlt ;end of instructions
    end start           
 code ends;