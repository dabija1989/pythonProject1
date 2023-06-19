"""
Creați două liste care vor reprezenta numele participanților la două evenimente. Transformați-le apoi în seturi.
Utilizați operațiile cu seturi și afișați rezultatele:
    câți participanți au fost prezenți la ambele evenimente
    câți participanți au fost prezenți doar la primul eveniment
    câți participanți au fost prezenți doar la al doilea eveniment
"""
# Solution
# Creare lista eveniment 1
nume_ev1 = input("Introduceti numele participantilor prin virgula:\n")
eveniment_1 = nume_ev1.split(",")
nume_ev2 = input("Introduceti numele participantilor prin virgula:\n")
eveniment_2 = nume_ev2.split(",")

set1 = set(eveniment_1)
set2 = set(eveniment_2)

prezenti_la_ambele = len(set1.intersection(set2))
prezenti_doar_la_primul = len(set1.difference(set2))
prezenti_doar_la_al_doilea = len(set2.difference(set1))

print(f"Participanții prezenți la ambele evenimente: {prezenti_la_ambele}")
print(f"Participanții prezenți doar la primul eveniment: {prezenti_doar_la_primul}")
print(f"Participanții prezenți doar la al doilea eveniment: {prezenti_doar_la_al_doilea}")
