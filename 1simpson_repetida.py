# Regra 1/3 de Simpson Repetida #

import math
e = 2.71828

b = int(input("b = ")) # b = limite de integração "b".
a = int(input("a = ")) # a = limite de integração "a".

def f(x): # Coloque a função f(x) depois de return
    #---------------------------------------------#

    return math.log(x+3)
    # Ex: return math.log(x+3)

    #---------------------------------------------#

n = int(input("n = ")) # = nº de subintervalos
h = (b-a)/n

x = [a]
for i in range(n):
    x.append(x[i]+h)

fx = []
for i in range(n+1):
    fx.append(f(x[i]))

print()
fx_impar,fx_par=[],[]
for i in range(n+1):
    print(f"x{i} = {x[i]} | f({i}) = {fx[i]:.7f} | ")
    if i%2!=0 and i!=0 and i!=n:
        fx_impar.append(fx[i])
    if i%2==0 and i!=0 and i!=n:
        fx_par.append(fx[i])

print("\n#--------------------------------------------------------------------------------------------#")

I = h/3*(fx[0] + 4*sum(fx_impar) + 2*sum(fx_par) + fx[-1])
print("\nI = h/3.[f(x0) + 4.f(xímpar) + 2.f(xpar) + f(xn)]]")
print(f"\nI = {h}/3*[{fx[0]:.7f} + 4*({str(fx_impar).replace(', ',' + ').strip('[]')}) + 2*({str(fx_par).replace(', ',' + ').strip('[]')}) + {fx[-1]:.7f}]")
print(f"\nI = {h}/3*[{fx[0]:.7f} + {4*sum(fx_impar):.7f} + {2*sum(fx_par):.7f} + {fx[-1]:.7f}]")
print(f"\n(I = {I:.7f})\n")
