questions = ["Mc Donalds é melhor que Burguer King?",
             "Wesley é fofinho?",
             "William usa aparelho?",
             "O notebook do sesi presta?",
             "Jennifer é crente?",
             "Giva é legal?",
             "O orgulho foi cansativo?",
             "Essa atividade demora?",
             "Oi como vai sua linda?",
             "A muriçoca?"]

Answers = ["sim",
           "sim",
           "sim",
           "sim",
           "sim",
           "sim",
           "sim",
           "sim",
           "oi",
           "soca"]

nota = 0

for i in range(10):
    x = input(questions[i])
    if x == Answers[i]:
        print("tá certo")
        nota = nota + 1
    else:
        print("tá errado mlk")

if nota == 0:
    print(f"sua nota foi {nota}, preste mais atenção!!!!!")
else:
    print(f"sua nota foi {nota}, BOA.")