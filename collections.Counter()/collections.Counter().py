if __name__ == '__main__':
  from collections import Counter
  
  Cant_Zapatos= int(input("Ingrese cantidad de zapatillas en stock: "))  
  Talles_Zapatos= Counter(map(int, input("ingrese talle de zapatillas: ").split()))
  Cant_Clientes= int(input("ingrese cantidad de clientes: "))
  Ganancia=0
  
  for i in range(Cant_Clientes):
    Talles_elegidos , Precio_Zapatos= list(map(int, input("ingrese Talles elegidos y precio de zapatillas:: ").split()))
    if Talles_Zapatos[Talles_elegidos]:
      Ganancia= Ganancia+Precio_Zapatos
      Talles_Zapatos[Talles_elegidos]=Talles_Zapatos[Talles_elegidos]-1
    #print(Ganancia)
    
print(Ganancia)

