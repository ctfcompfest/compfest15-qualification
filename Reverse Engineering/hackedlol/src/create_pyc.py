import base64, random, py_compile, os

source = open("source.py").read()
source64 = base64.b64encode(source.encode())
source64_list = list(source64.decode())

for i in range(len(source64_list)):
    if random.randint(0, 3) == 2:
        source64_list[i] = f"\\x{hex(ord(source64_list[i]))[2:]}"

first_level = f"""q=__import__('\\x62\\x61\\x73\\x65\\x36\\x34', globals(), locals());z=__import__('\\x6fs', globals(), locals());x=q.b64decode(\"""" + "".join(source64_list) + """");f=open("\\x68\\x65\\x6c\\x70\\x65\\x72\\x2e\\x70\\x79", "w");f.write(x.decode());f.close();z.system("\\x70\\x79\\x74\\x68\\x6f\\x6e\\x33\\x20\\x68\\x65\\x6c\\x70\\x65\\x72\\x2e\\x70\\x79")"""

chall_code = f"p=__import__('base64', globals(), locals());exec(p.b64decode('{base64.b64encode(first_level.encode()).decode()}'))"

with open("hackedlol.py", "w") as chall:
    chall.write(chall_code)
os.system("python3 hackedlol.py")
py_compile.compile("hackedlol.py", "hackedlol.pyc")
os.remove("hackedlol.py")
os.system("mv hackedlol.pyc ../../public/hackedlol.pyc")
os.system("mv important_file.hackedlol ../../public/important_file.hackedlol")