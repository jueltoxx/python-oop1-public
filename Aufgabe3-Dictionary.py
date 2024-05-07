# Aufgabe: ToDo-Liste Schreibe ein Python-Programm, das eine einfache ToDo-Liste verwaltet.
# Der Benutzer sollte in der Lage sein, Aufgaben hinzuzufügen, sie als erledigt zu markieren und die Liste anzuzeigen.
# Verwende dazu eine Liste und möglicherweise eine Verzweigung für die Erledigungsmarkierung.

toDos = [
    {"Titel":"Aufgabe A","Status":"offen"},
    {"Titel":"Aufgabe A","Status":"offen"}
]

print(toDos[0]["Titel"])

toDos[0]["Status"] = "Done"

print(toDos[0])




