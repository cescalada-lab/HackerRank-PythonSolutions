if __name__ == '__main__':
    lista=[]
    scores1=set()
    scores2=[]
    ordenar=[]

    for _ in range(int(input())):
        name = str(input())
        score = float(input())
        lista.append([name,score])
        scores1.add(score)
    scores2=sorted(scores1)

    for x in range(len(lista)):
      if scores2[1]==lista[x][1]:
        ordenar.append(lista[x][0])
        ordenar.sort()
        
    for name in ordenar:
      print(name)
