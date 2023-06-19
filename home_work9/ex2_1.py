"""
Creati un program care va analiza urmatorul text: https://www.gutenberg.org/cache/epub/1513/pg1513.txt
Progrmaul va trebui sa gaseasca:
• numarul total de cuvinte din text.
• top 30 cele mai utilizate cuvinte
• top 30 cele mai putin utilizate cuvinte
Pentru a stoca informatia, puteti utiliza doua liste.
Exemplu:
list_cuvinte = ['cuvant1', 'cuvant2', 'cuvant3', ...]
list_ori = [10, 20, 30, ...]
Astfel fiecare indice din list_cuvinte va corespunde cu indicele in list_ori, unde cuvant3 e intalnit de 30 ori.
"""
# Solution
import urllib.request # importa textul dintro sursa web folosind modulul "urllib.request"
from collections import Counter # importam clasa "counter" din "collections" pentru numararea elementelor dintr-o lista.
from collections import Counter
import operator
# descaracam
url = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"
sursa = urllib.request.urlopen(url) # Folosim functia "urlopen()" pentru a deschide conexiunea catre URL nostru.
text = sursa.read().decode("utf-8") # Citim continutul folosind metoda "read()" si decodam textulfolosind functia decode.

# Divizare text în cuvinte
cuvinte = text.lower().split()

# Eliminare caractere speciale și punctuație
cuvinte = [cuvant.strip(".,:;!?'\"()[]{}") for cuvant in cuvinte]
# Număr total de cuvinte
total_cuvinte = len(cuvinte)
print("---------------------------------")
print("Număr total de cuvinte:", total_cuvinte)
print("---------------------------------")

cuvinte_dict = dict(Counter(cuvinte))
sorted_counts = sorted(cuvinte_dict.items(), key=operator.itemgetter(1), reverse=True)

print("Top 30 cuvinte cele mai des utilizate:")
for i, (key, value) in enumerate(sorted_counts[:30], 1):
    print(f"{i}. {key}: {value}")
print("---------------------------------")
print("Top 30 cuvinte cele mai rar utilizate:")
for i, (key, value) in enumerate(sorted_counts[-30:], 1):
    print(f"{i}. {key}: {value}")
print("---------------------------------")
