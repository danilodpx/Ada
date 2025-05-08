# exercício 1

aluno = {
    "nome": "Danilo",
    "idade": 43,
    "nota": 8.5
}


print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])


# exercício 4
frutas = {"maçã": 3, "banana": 5, "laranja": 2}

nome_fruta = input("Digite o nome de uma fruta: ")

if nome_fruta in frutas:
    quantidade = frutas[nome_fruta]
    print(f"Temos {quantidade} unidades de {nome_fruta}.")
else:
    print(f"Desculpe, {nome_fruta} não está disponível.")

    

# exercício 5
    notas_alunos = {
    "Ana": 8.5,
    "João": 6.7,
    "Maria": 9.2,
    "Pedro": 5.8,
    "Carla": 7.1
}

print("Alunos com média maior ou igual a 7:")
for aluno, media in notas_alunos.items():
    if media >= 7:
        print(f"- {aluno}: {media}")