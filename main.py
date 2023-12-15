import random
import re

instrucoes ='''
Insira o número de moedas a serem lançadas,
siga o padrão [Nt], onde N = número de moedas.
Exemplo: 3t
'''
print(instrucoes)
texto = input("Quantidade de lançamentos: ")

p = re.compile(r'[0-9]+[tT]')
correspondencias = p.finditer(texto)
verifica = p.search(texto)

e = re.compile(r'[a-sA-Su-zU-Z!@#$%&*()_{}§´`¨^~ºª|<>?/.,:;°]+')
verificaErro = re.search(e, texto)

if verificaErro:
  print('\nErro: Quantidade inválida' + '\n' + instrucoes)
else:
  if verifica:
    for c in correspondencias: 
      g = 0
      print(f"\n{c.group(g)}")

      m = re.compile(r'[0-9]+')
      mstr = c.group(g)
      mstr = str(m.findall(mstr)) 

      mstr = str(mstr[2:-2])
      
      try:
        mstr = int(mstr)
      except:
        mstr = 1

      print(f"Nº de moedas:   {mstr}")

      for i in range(mstr):
        resultado = random.randint(1, 2)
        if resultado == 1:
          resultado = 'Cara'
        if resultado == 2:
          resultado = 'Coroa'         
        print(f"Resultado {i+1}:    {resultado}")

      g += 1