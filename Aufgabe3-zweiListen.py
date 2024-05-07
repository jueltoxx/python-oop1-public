# Aufgabe: ToDo-Liste Schreibe ein Python-Programm, das eine einfache ToDo-Liste verwaltet.
# Der Benutzer sollte in der Lage sein, Aufgaben hinzuzufügen, sie als erledigt zu markieren und die Liste anzuzeigen.
# Verwende dazu eine Liste und möglicherweise eine Verzweigung für die Erledigungsmarkierung.

toDos = ["Blumen giessen", "Hund laufen"]
done = []

def addToDo():
    print()
    newToDo = input("Aufgabe hinzu: ")
    toDos.append(newToDo)
    print("Neue Liste:")
    printToDos()
    print()

def printToDos():
    print()
    for i, todo in enumerate(toDos):
        print(i, todo)

def toDone(index):
    print()
    for i, todo in enumerate(toDos):
        print(i, todo)
    toDone = toDos.pop[index]
    done.append(toDone)

print(done)

printToDos()

addToDo()

toDone(input("was ist gemacht?"))

print(done)
printToDos()

