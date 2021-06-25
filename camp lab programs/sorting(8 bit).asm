 ;program to sort 8 bit numbers
 data segment
    LIST db 75h,47h,57h;defining the list to be sorted
    count db EQU<$-LIST>
    data ends;
 code segment
    assume cs:code,ds:data
    start:mov ax,data
          mov ds,ax
          mov dx,count-1
          
          repeat: mov SI,offset LIST ;si points to list
                  mov cx,dx
                  
                  again: mov al,[SI];al=75
                         cmp al,[SI+1]
                         jc next ;jc means jump of carry to next label
                         xchg al,[SI+1];al=47
                         xchg al,[SI];al=75 [si]=47
                         
                         next:inc SI
                         loop again
                         dec dx
                         
                         jnz repeat   ;jump on nonzero <dx register>
                         hlt
      end start              
      
   code ends;
                  