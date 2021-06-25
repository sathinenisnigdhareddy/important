; to display the characters using keyboard interrupt

data segment
    
data ends

code segment
    
    assume cs:code,ds:data
    start:
    mov ah,1
    int 21h;listen mode   
    
    mov dl,al ;clear the buffer
    mov ah,2
    int 21h ;to display mode
    
    mov al,4ch
    int 21h ;exit the program
    
    end start
    
code ends