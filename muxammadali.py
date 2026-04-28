import random
import tkinter as tk
from tkinter import messagebox

def dunyo(n, m, qoida):
    q = format(qoida, '08b')
    print("qoida:", q)

    d = []
    for i in range(m):
        d.append([0]*n)

    d[0] = []
    for i in range(n):
        d[0].append(random.randint(0,1))

    for i in range(m-1):
        for j in range(n):

            chap = d[i][j-1]
            orta = d[i][j]
            ong = d[i][(j+1)%n]

            s = str(chap)+str(orta)+str(ong)
            ind = 7 - int(s,2)

            d[i+1][j] = int(q[ind])

    return d

def qadam(matritsa):
    yangi = []
    for q in matritsa:
        yangi.append(q[:])

    n = len(matritsa)
    m = len(matritsa[0])

    for i in range(1,n-1):
        for j in range(1,m-1):

            s = 0
            s += matritsa[i-1][j-1]
            s += matritsa[i-1][j]
            s += matritsa[i-1][j+1]
            s += matritsa[i][j-1]
            s += matritsa[i][j+1]
            s += matritsa[i+1][j-1]
            s += matritsa[i+1][j]
            s += matritsa[i+1][j+1]

            if matritsa[i][j] == 1:
                if s==2 or s==3:
                    yangi[i][j] = 1
                else:
                    yangi[i][j] = 0
            else:
                if s==3:
                    yangi[i][j] = 1

    return yangi

class App:
    def init(self, root, tarix):
        self.root = root
        self.tarix = tarix
        self.i = 0
        self.k = 15

        self.c = tk.Canvas(root,
                           width=len(tarix[0][0])*self.k,
                           height=len(tarix[0])*self.k,
                           bg="white")
        self.c.pack()

        f = tk.Frame(root)
        f.pack()

        tk.Button(f,text="old",command=self.old).pack(side="left")
        tk.Button(f,text="next",command=self.next).pack(side="left")

        self.l = tk.Label(root,text="")
        self.l.pack()

        self.draw()

    def draw(self):
        self.c.delete("all")
        m = self.tarix[self.i]

        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == 1:
                    x = j*self.k
                    y = i*self.k
                    self.c.create_rectangle(x,y,x+self.k,y+self.k,fill="black")

        self.l.config(text="qadam: "+str(self.i))

    def next(self):
        if self.i < len(self.tarix)-1:
            self.i += 1
            self.draw()
        else:
            messagebox.showinfo("ok","tamom")

    def old(self):
        if self.i > 0:
            self.i -= 1
            self.draw()

n = int(input("Qatorlar sonini kiriting: "))
m = int(input("Ustunlar sonini kiriting: "))
q = int(input("qoida = "))

d0 = dunyo(n,m,q)

print("boshlanish:")
for x in d0:
    print(x)

tarix = [d0]

for i in range(100):
    y = qadam(tarix[-1])
    if y == tarix[-1]:
        break
    tarix.append(y)

root = tk.Tk()
root.title("hayot")
app = App(root, tarix)
root.mainloop()