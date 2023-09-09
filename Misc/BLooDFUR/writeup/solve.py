file_names = ["back", "left", "bottom", "front", "top", "right"]
data = []

for file_name in file_names:
    with open(f"../public/{file_name}.txt", "r") as notes:
        side = [i.strip().split() for i in notes.readlines()]
        data.append(side)

b, l, d, f, u, r = data

def cetak():
    sides = (b, l, d, f, u, r)
    for side in sides:
        for i in side:
            print(i)
        print()

def R():
    global f, u, b, d, r
    # muter sisi kanan
    temp = [[r[i][j] for i in range(3)[::-1]] for j in range(3)]
    r = temp

    # muter sisi lainnya
    temp = [f[i][2] for i in range(3)]
    for i in range(3):
        f[i][2] = d[i][2]
        d[i][2] = b[2-i][0]
        b[2-i][0] = u[i][2]
        u[i][2] = temp[i]

def R_():
    global f, u, b, d, r
    # muter sisi kanan
    temp = [[r[i][j] for i in range(3)] for j in range(3)[::-1]]
    r = temp

    # muter sisi lainnya
    temp = [f[i][2] for i in range(3)]
    for i in range(3):
        f[i][2] = u[i][2]
        u[i][2] = b[2-i][0]
        b[2-i][0] = d[i][2]
        d[i][2] = temp[i]
    
def L():
    global f, u, b, d, l
    # muter sisi kiri
    temp = [[l[i][j] for i in range(3)[::-1]] for j in range(3)]
    l = temp

    # muter sisi lainnya
    temp = [f[i][0] for i in range(3)]
    for i in range(3):
        f[i][0] = u[i][0]
        u[i][0] = b[2-i][2]
        b[2-i][2] = d[i][0]
        d[i][0] = temp[i]

def L_():
    global f, u, b, d, l
    # muter sisi kiri
    temp = [[l[i][j] for i in range(3)] for j in range(3)[::-1]]
    l = temp

    # muter sisi lainnya
    temp = [f[i][0] for i in range(3)]
    for i in range(3):
        f[i][0] = d[i][0]
        d[i][0] = b[2-i][2]
        b[2-i][2] = u[i][0]
        u[i][0] = temp[i]
    
def U():
    global f, u, b, l, r
    # muter sisi atas
    temp = [[u[i][j] for i in range(3)[::-1]] for j in range(3)]
    u = temp

    # muter sisi lainnya
    temp = [f[0][i] for i in range(3)]
    for i in range(3):
        f[0][i] = r[0][i]
        r[0][i] = b[0][i]
        b[0][i] = l[0][i]
        l[0][i] = temp[i]

def U_():
    global f, u, b, l, r
    # muter sisi atas
    temp = [[u[i][j] for i in range(3)] for j in range(3)[::-1]]
    u = temp

    # muter sisi lainnya
    temp = [f[0][i] for i in range(3)]
    for i in range(3):
        f[0][i] = l[0][i]
        l[0][i] = b[0][i]
        b[0][i] = r[0][i]
        r[0][i] = temp[i]
    
def D():
    global f, l, b, d, r
    # muter sisi bawah
    temp = [[d[i][j] for i in range(3)[::-1]] for j in range(3)]
    d = temp

    # muter sisi lainnya
    temp = [f[2][i] for i in range(3)]
    for i in range(3):
        f[2][i] = l[2][i]
        l[2][i] = b[2][i]
        b[2][i] = r[2][i]
        r[2][i] = temp[i]

def D_():
    global f, l, b, d, r
    # muter sisi bawah
    temp = [[d[i][j] for i in range(3)] for j in range(3)[::-1]]
    d = temp

    # muter sisi lainnya
    temp = [f[2][i] for i in range(3)]
    for i in range(3):
        f[2][i] = r[2][i]
        r[2][i] = b[2][i]
        b[2][i] = l[2][i]
        l[2][i] = temp[i]

def F():
    global f, u, l, d, r
    # muter sisi depan
    temp = [[f[i][j] for i in range(3)[::-1]] for j in range(3)]
    f = temp
    
    # muter sisi lainnya
    temp = [r[i][0] for i in range(3)]
    for i in range(3):
        r[i][0] = u[2][i]
        u[2][i] = l[2-i][2]
        l[2-i][2] = d[0][2-i]
        d[0][2-i] = temp[i]

def F_():
    global f, u, l, d, r
    # muter sisi depan
    temp = [[f[i][j] for i in range(3)] for j in range(3)[::-1]]
    f = temp
    
    # muter sisi lainnya
    temp = [r[i][0] for i in range(3)]
    for i in range(3):
        r[i][0] = d[0][2-i]
        d[0][2-i] = l[2-i][2]
        l[2-i][2] = u[2][i]
        u[2][i] = temp[i]

def B():
    global f, l, b, d, r
    # muter sisi belkang
    temp = [[b[i][j] for i in range(3)[::-1]] for j in range(3)]
    b = temp

    # muter sisi lainnya
    temp = [r[i][2] for i in range(3)]
    for i in range(3):
        r[i][2] = d[2][2-i]
        d[2][2-i] = l[2-i][0]
        l[2-i][0] = u[0][i]
        u[0][i] = temp[i]

def B_():
    global f, l, b, d, r
    # muter sisi belkang
    temp = [[b[i][j] for i in range(3)] for j in range(3)[::-1]]
    b = temp

    # muter sisi lainnya
    temp = [r[i][2] for i in range(3)]
    for i in range(3):
        r[i][2] = u[0][i]
        u[0][i] = l[2-i][0]
        l[2-i][0] = d[2][2-i]
        d[2][2-i] = temp[i]

notation = {
    "R": R,
    "L": L,
    "U": U,
    "D": D,
    "F": F,
    "B": B,
    "R'": R_,
    "L'": L_,
    "U'": U_,
    "D'": D_,
    "F'": F_,
    "B'": B_,
}

def run_move(moves):
    for move in moves:
        if "2" in move:
            notation[move[0]]()
            notation[move[0]]()
        else:
            notation[move]()

# cetak()

solve = "D' R F R2 B2 U L2 D' B L' F2 R2 U2 B2 D' F2 U B2 L2".split()
run_move(solve)

# cetak()

sides = (b, l, d, f, u, r)
with open("equations.txt", "w") as final:
    for side in sides:
        for row in side:
            for sq in row:
                final.write(sq.replace("|", "\n"))
