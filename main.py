import matplotlib as mpl
from random import randint
mpl.use('Agg')
import matplotlib.pyplot as plt
import timeit

def desenhaGrafico(x,y, yl = "Saídas",xl = "Entradas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(yl+'_graph.png')
 
def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def select(xb):
  count = 0
  for a in range(xb):
    minimo = lis[a]
    for b in range(a+1,xb):
      if (minimo > lis[b]):
        aux = lis[b]
        lis[b] = minimo
        minimo = aux
      count=count+1
      lis[a] = minimo
  return count

x = [1000, 2000, 4000, 6000]
y = []
z = []
for i in range(len(x)):
  lis = geraLista(x[i])
  y.append(select(x[i]))
  z.append(timeit.timeit('select({})'.format(x[i]),setup="from __main__ import select",number=1))

desenhaGrafico(x,y, "nops")
desenhaGrafico(x,z, "Tempo")