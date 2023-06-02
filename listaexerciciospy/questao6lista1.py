convidados = ["Michael Jackson", "Neymar", "Messi", "tite", "gabigol"]

convite = "Caro(a) {}, você está convidado(a) para um jantar em minha residência no próximo sábado. Será uma noite incrível com boas bebidas e ótimas comidas. Aguardo sua companhia!"

for convidado in convidados:
    print("Enviando convite para:", convidado)
    print(convite.format(convidado))
    print()

nao_pode_comparecer = "tite"
print("Infelizmente, {} não poderá comparecer ao jantar.".format(nao_pode_comparecer))

convidados.remove(nao_pode_comparecer)
convidados.append("Mario.")

print("Pessoas que não poderão comparecer:")
print(nao_pode_comparecer)
print()

for convidado in convidados:
    print("Enviando novo convite para:", convidado)
    print(convite.format(convidado))
    print()

convidados = ["Michael Jackson", "Neymar", "Messi", "tite", "gabigol"]

convite = "Caro(a) {}, você está convidado(a) para um jantar em minha residência no próximo sábado. Será uma noite incrível com boas bebidas e ótimas comidas. Aguardo sua companhia!"

for convidado in convidados:
    print("Enviando convite para:", convidado)
    print(convite.format(convidado))
    print()

nao_pode_comparecer = "tite"
print("Infelizmente, {} não poderá comparecer ao jantar.".format(nao_pode_comparecer))

convidados.remove(nao_pode_comparecer)
convidados.append("Mario.")

print("Pessoas que não poderão comparecer:")
print(nao_pode_comparecer)
print()

for convidado in convidados:
    print("Enviando novo convite para:", convidado)
    print(convite.format(convidado))
    print()
