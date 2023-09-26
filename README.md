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
