questions = ["Theo é fofinho?",
             "Duke parece o beiçola?",
             "esta com sono?",
             "no segundo ano existe medo?"]

answers = ["sim",
           "sim",
           "sim",
           "sim"]

nota = 0

for i in range(4):
    x = input(questions[i])
    if x == answers[i]:
        print ("ta certo")
        nota = nota + 1
    else:
        print ("errouuuu")

if nota == 0:
    print (f"sua nota foi {nota}, tenha mais atençâo!")
else: 
    print (f"sua nota foi {nota}, Boa ")