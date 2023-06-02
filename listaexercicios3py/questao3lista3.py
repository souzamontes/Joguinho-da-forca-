arquivo = open("frase.txt", "a+")
novo_texto = "\nBRASIL TE DAREI COM AMOR TODA A SEIVA E VIGOR EM QUE MEU PEITO SE ENCERRA, INFANTARIA INFERNO VERDE"
arquivo.write(novo_texto)
arquivo.seek(0)
novo_conteudo = arquivo.read()
print("Novo conteúdo:")
print(novo_conteudo)
arquivo.close()
