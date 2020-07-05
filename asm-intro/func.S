.global inc_func
	.text

inc_func:
        push %rbp                 # function prelog
	movq %rsp, %rbp           #
        adcq $0x1, %rdi
        movq %rdi, %rax
        pop %rbp                  # function epilog
        ret 

