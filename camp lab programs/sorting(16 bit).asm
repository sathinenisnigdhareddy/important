 ;sorting the list of elements
 
data segment
    LIST dw 0075h,0047h,0057h
    count dw EQU($-LIST) ;no of bytes
data ends

code segment
    assume cs:code,ds:data
    start: mov ax,data
           mov ds,ax
           mov dx,count/2 -1
           
    repeat:mov SI,offset LIST
           mov cx,dx
      
    again: mov ax,[SI]
           cmp ax,[SI+2]   
           jc next
           xchg ax,[SI+2]
           xchg ax,[SI]
           
     next:inc SI
          inc SI
     loop again  
     dec dx
     jnz repeat
     
     hlt
     end start
     
code ends;