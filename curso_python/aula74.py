def criar_sadacao(saudacao):
    def saudar(nome):
      return f'{saudacao}, {nome}!'  
    return saudar
    

falar_bom_dia = criar_sadacao('Bom dia')

print(falar_bom_dia('Eduardo'))