

# # class Persona: 
# #     def __init__(self,a,b): #ATTRIBUTI
# #         self.nome = a 
# #         self.eta = b

 
# # alessandro = Persona('Alessandro', 27)
# # # print(alessandro)
# # alessandro.nome
# # alessandro.eta

# class Rettangolo:
#     def __init__(self,b:float,h:float):
#         self.base = b
#         self.altezza = h 
# # classe dell'area utilizzando base e altezza

#     def calcoloArea(self):

#         return self.base*self.altezza
    


# rett = Rettangolo(2.3,5.6)

# print(rett.calcoloArea())

## PERCENTUALE

class Percentuale:
  def __init__(self,n,t,p=100):
     self.perc = n/t*p 
     
percento = Percentuale(10,140)
print(percento.perc) ## USARE PRINT PER AVERE NEI RISULTATI SE NON SEI SUL NOTEBOOK

class Unione:
  def __init__(self,x):
    self.quadrato = x**2
    self.per = self.quadrato*2

calcolo = Unione(12)
print(calcolo.per)







 


