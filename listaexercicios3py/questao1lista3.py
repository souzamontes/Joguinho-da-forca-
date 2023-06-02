arquivo = open("frase.txt", "w")

frase = "BRASIL TE DAREI COM AMOR TODA A SEIVA E VIGOR EM QUE MEU PEITO SE ENCERRA"
arquivo.write(frase)

arquivo.close()

arquivo = open("frase.txt", "r")
frase_lida = arquivo.read()
print(frase_lida)

arquivo.close()
