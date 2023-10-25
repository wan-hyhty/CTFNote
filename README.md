# CTFNote

## [Johnathan Huu Tri](https://github.com/nhtri2003gmail/CTFNote)

## [open-read-write](https://tripoloski1337.github.io/ctf/2021/07/12/bypassing-seccomp-prctl.html)

## [arm-syscall](https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#linux-system-call-table)

## [FSOP-leak-stack](https://github.com/wan-hyhty/CTFs_competition/tree/main/ImaginaryCTF2023/mailman)

```python
f = FileStructure()
f.flags = 0xfbad1800
f._IO_read_base = libc.sym['environ']
f._IO_read_ptr = libc.sym['environ']+8
```

## [rand-vulnerability](https://hackmd.io/@whoisthatguy/rand)

```python
from ctypes import CDLL
libc = CDLL("/lib/x86_64-linux-gnu/libc.so.6")
libc.srand(libc.time(0))
```

## [race-condition](https://hackmd.io/@whoisthatguy/toctou?utm_source=preview-mode&utm_medium=rec)

## [ret2csu](https://hackmd.io/@whoisthatguy/ret2csu)

## [ret2dlresolve](https://hackmd.io/@whoisthatguy/ret2dlresolve)

## [rop-arm](http://blog.perfect.blue/ROPing-on-Aarch64)

## [Linux Privilege Escalation](https://github.com/RoqueNight/Linux-Privilege-Escalation-Basics)

`https://gtfobins.github.io/`

## [shellcode](https://docs.pwntools.com/en/stable/shellcraft.html)

```
32 bit: \x31\xC0\x50\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x31\xDB\x31\xC9\x31\xD2\x89\xE3\x83\xC0\x0B\xCD\x80
64 bit: \x48\x31\xFF\x57\x48\xBF\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x57\x48\x31\xF6\x48\x31\xD2\x48\x89\xE7\x48\x31\xC0\x48\x83\xC0\x3B\x0F\x05
```

## AARCH64
### LDR X0, X1, [SP], #16
- pop x0, x1
- Remember that in AArch64 the stack-pointer must be 128-bit aligned.
### STP X0, X1, [SP, #-16]!
- push x0, x1
### MOV X0, #1
- sets: X0 = 1
### MVN W0, W1
- sets: W0 = ~W1