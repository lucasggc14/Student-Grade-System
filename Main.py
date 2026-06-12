alunos = {}

while True:
    print("1- Digitar notas")
    print("2- Consultar aluno")
    print("3- Listar alunos")
    print("4- Sair")
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        
        if nome not in alunos:
            alunos[nome] = []
            
        alunos[nome].append([nota1, nota2, nota3])
        print("Notas adicionadas ao histórico do aluno!")
        
    elif opcao == "2":
        nome = input("Nome do aluno: ")
        if nome in alunos:
            print(f"\nHistórico de {nome}: ")
            
            for i, nota in enumerate(alunos[nome],start=1):
                media = sum(nota) / len(nota)
                print(f"{i}ª entrada -> Notas: {nota} | Média: {media: .2f}")
        else:
                print("Aluno não emcontrado")
    elif opcao == "3":
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado")
        else:
            print("\nAlunos:")
            for nome in alunos:
                print("-", nome)
    elif opcao == "4":
        print("Encerrando o programa...")
    break
