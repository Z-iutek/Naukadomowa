##                                                   ZADANIE PAWEŁ NAGALEWSKI GRUPA  L_I_NWh_INF_K3 ALGORYTMIKA I STRUKTURA DANYCH 
# ______________________________________________________________________PODSUOMOWANIE PROGRAMU NA SAMYM DOLE ____________________________________________________________

import random
import time
print("\n")
rozmiar_listy = int(input(" Podaj rozmiar listy: "))
listaSequential = list(range(rozmiar_listy))
lista = list(range(rozmiar_listy))
listaCopy = [] 
Converging = list(range(rozmiar_listy))

for i in range(len(lista)):
    lista[i] = random.randint(0,100)

wartosc_smiec = random.randint(0,100)
kopia_listy = lista
print("\n")
print("------------------------Czyszczenie listy z losowanej wartośći: ------------------------")

print(" Wartość odrzucana: ", wartosc_smiec)
# print(lista)

for i in range(len(listaSequential)):
    listaSequential[i] = random.randint(0,100)

for i in range(len(Converging)):
    Converging[i] = random.randint(0,100)

def binarySearch(kopia_listy, szukana):
    lo = 0
    hi = len(kopia_listy) - 1
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if kopia_listy[mid] < szukana:
            lo = mid + 1
        else:
            hi = mid
 
    if kopia_listy[lo] == szukana:
        print(" Binadry Search: Szukana liczba znajduje sie na ineksie:    ", lo)
    elif kopia_listy[hi] == szukana:
        print(" Binadry Search: Szukana liczba znajduje sie na ineksie:    ", hi)
    else:
        print(" Binadry Search: Szukana liczba nie znajduje się w liście :/ ")

def CopyOver(CopyOver):
    L = 0
    for i in range (len(CopyOver)):
        if CopyOver[L] != wartosc_smiec:
            listaCopy.append(CopyOver[L])
            L+=1
        else:L+=1

def ConvergingPointers(Converging):

    legit = len(Converging)
    L = 0
    R = len(Converging) -1
    while L < R:
        if Converging[L] != wartosc_smiec:
            L+=1
        elif Converging[L] == wartosc_smiec:
            legit -= 1
            Converging[L] = Converging[R]
            R-=1
            del Converging[-1]
    if Converging[L] == wartosc_smiec:
        legit-=1
        return

def InsertionSort(Insertion):

    for i in range(1, len(Insertion)):
        key = Insertion[i]
        j = i-1
        while j >= 0 and key < Insertion[j] :
             Insertion[j + 1] = Insertion[j]
             j -= 1
        Insertion[j + 1] = key

def mergeSort(Merge):
    if len(Merge) > 1:
        mid = len(Merge)//2
        L = Merge[:mid]
        R = Merge[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                Merge[k] = L[i]
                i += 1
            else:
                Merge[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            Merge[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            Merge[k] = R[j]
            j += 1
            k += 1

def Sequential_Search(dlist, item):

    pos = 0
    found = False
    
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1

    print(" Sequential Search: Szukana wartość znajduje się na indexie:", pos)

def LinearSearch1(lista, szukana):
    for i in range(len(lista)):
        if lista[i] == szukana:
            print(" LinearSearch: Szukana wartość znajduje się na indexie:", i)
    return (" ")
def LinearSearch2(lista, szukana):
    for i in range(len(lista)):
        if lista[i] == szukana:
            print(" LinearSearch: Szukana wartość znajduje się na indexie:", i)
            return (" ")

timerCopyOver1 = time.time()
CopyOver(lista)
timerCopyOver2 = time.time()
ENDtimerCopyOver = timerCopyOver2 - timerCopyOver1

# print(listaCopy)
print("\n", "CopyOver wyczyściło liste w:                  ", round(ENDtimerCopyOver,5), " sekund" )

timerConverging1 = time.time()
ConvergingPointers(Converging)
timerConverging2 = time.time()
ENDtimerConverging = timerConverging2 - timerConverging1
print(" ConvergingPointers wyczyściło liste w:        ", round(ENDtimerConverging,5), " sekund" )
# print(Converging)

print("\n", "Lista używająca metode Converging odrzuciła: ", rozmiar_listy - int(len(Converging)), " elementów")
print(" Lista używająca metode CopyOver odrzuciła:  ", rozmiar_listy - int(len(listaCopy)), " elementów")

print("\n")
print("------------------------Sortowanie list: ------------------------")

odp1 = int(input("Jeśli chcesz posortowac liste funkcją Insertion wpisz 1: "))
if odp1 == 1:
    timerInsertion1 = time.time()
    InsertionListaCopy = listaCopy
    InsertionSort(InsertionListaCopy)
    timerInsertion2 = time.time()
    ENDtimerInsertion = timerInsertion2 - timerInsertion1
    print("\n","InsertionSort posortowało liste CopyOver w:   ", round(ENDtimerInsertion,5), " sekund" )
    # print(InsertionListaCopy)

    timerInsertion3 = time.time()
    InsertionConverging = Converging
    InsertionSort(InsertionConverging)
    timerInsertion4 = time.time()
    ENDtimerInsertion2 = timerInsertion4 - timerInsertion3
    print(" InsertionSort posortowało liste Converging w: ", round(ENDtimerInsertion2,5), " sekund" )
    # print(InsertionConverging)

print("\n")

odp2 = int(input("Jeśli chcesz posortowac liste funkcją Merge wpisz 1: "))
if odp2 == 1:
    MergeListaCopy = listaCopy
    MergeConverging = Converging

    timerMerge1 = time.time()
    mergeSort(MergeListaCopy)
    timerMerge2 = time.time()
    ENDtimerMerge = timerMerge2 - timerMerge1
    print("\n", "MergeSort posortował liste CopyOver w:        ", round(ENDtimerMerge,5), " sekund" )
    # print(MergeListaCopy)

    timerMerge3 = time.time()
    mergeSort(MergeConverging)
    timerMerge4 = time.time()
    ENDtimerMerge2 = timerMerge4 - timerMerge3
    print(" MergeSort posortował liste Converging w:      ", round(ENDtimerMerge2,5), " sekund" )
    # print(MergeConverging)

print("\n")
print("------------------------Szukanie wartości: ------------------------")
mergeSort(kopia_listy)
szukana_losowa_wartosc = random.randint(0,100)
print("\n","Szukana wartosc to: ", szukana_losowa_wartosc)


timerBineary1 = time.time()
binarySearch(kopia_listy, szukana_losowa_wartosc)
timerBineary2 = time.time()
ENDtimerBineary = timerBineary2-timerBineary2

timerSequential1 = time.time()
Sequential_Search(listaSequential,szukana_losowa_wartosc)
timerSequential2 = time.time()
ENDtimerSequential = timerSequential2 - timerSequential1

pyt = int(input("Jeśli chcesz zobaczyć wszystkie wyniki LinearSearch wpisz 1 jeśli tylko 1 wpisz 2: "))
if pyt == 1:
    timerLinear1 = time.time()
    print(LinearSearch1(listaSequential,szukana_losowa_wartosc))
    timerLinear2 = time.time()
    ENDtimerLinear = timerLinear2 - timerLinear1
else:
    timerLinear1 = time.time()
    print(LinearSearch2(listaSequential,szukana_losowa_wartosc))
    timerLinear2 = time.time()
    ENDtimerLinear = timerLinear2 - timerLinear1


print("Czas szukania metod: ", "\n", "BinearySearch:    ", ENDtimerBineary, "\n", "SequentialSearch: ", ENDtimerSequential, "\n", "LinearSearch:     ", ENDtimerLinear)
print("\n")

print("Czas czyszczenia metod: ", "\n", "CopyOver:           ", ENDtimerCopyOver, "\n", "ConvergingPointers: ", ENDtimerConverging,)
if ENDtimerCopyOver < ENDtimerConverging:
    print("Metoda CopyOver jest szybsza do wielkości listy:", rozmiar_listy)
else:
     print("Metoda ConvergingPointers jest szybsza do wielkości listy:", rozmiar_listy)


print("\n")

print("Czas sortowania metod: ")
if odp1 !=1:
    print("Sortowanie Insertion się nie odbyło")
else:
    print(" Insertion1: ", ENDtimerInsertion,"\n","Insertion2: ", ENDtimerInsertion2,"\n")
if odp2 !=1:
    print("Sortowanie Merge się nie odbyło")
else:
    print(" MergeSort1: ", ENDtimerMerge,"\n","MergeSort2: ", ENDtimerMerge2)

if odp1 == 1 and odp2 == 1 and ENDtimerInsertion<ENDtimerMerge:
    print(" Sortowanie InsertionSort jest szybsze dla listy o wielkości: ",rozmiar_listy)
elif odp1 == 1 and odp2 == 1 and ENDtimerInsertion>ENDtimerMerge:
    print(" Sortowanie MergeSort jest szybsze dla listy o wielkości: ",rozmiar_listy)
elif odp1 == 1 and odp2 == 1 and ENDtimerInsertion==ENDtimerMerge:
    print("Czasy sortowania są takie same")
else:
    print(" ")





# ---------------------------------------------------------------------
#                        PODSUMOWANIE:
#  CZAS WYSZUKIWANIA ELEMENTÓW DLA WYŻEJ ZAIMPLEMENTOWANYCH FUNKCJI WYNOSI 0 SEKUND
# 
# 100      Elementów:
#          WSZYSTKIE CZASY WYNOSZĄ 0 SEKUND (Komputer "gamingowy")
# 
# 10000    Elementów: 
#          Czas sortowania:
#          InsertionSort         ~ 1.5sekundy
#          MergeSort             ~ 0,01sekundy
#          Czas czyszczenia:
#          CopyOver              ~ 0.001 sekund
#          ConvergingPointers    ~ 0.001 sekund
# 
# 50 000  Elementów:
#         Czas sortowania:
#         InsertionSort         ~ 37 sekund
#         MergeSort             ~ 0.08 sekund
#         Czas czyszczenia:
#         CopyOver              ~ 0.00503 sekund
#         ConvergingPointers    ~ 0.00652 sekund
# 
# 500 000 Elementów:
#         Czas sortowania:
#         InserionSort          ~ 3862 sekund
#         MergeSort             ~ 1.3 sekund
#         Czas czyszczenia:
#         CopyOver              ~ 0.0526 sekund
#         ConvergingPointers    ~ 0.0631 sekund
# 
#  Funckja InsertionSort sprawdza się przy małych listach lecz przy większych przykładowo składająca się z 500 000 elementów
#  wynosi to już 3862 sekund co daje 64 MINUT przy czym bardziej złożona funkcja MargeSort wykonuje sortowanie listy o tej 
#  samej ilości elementów w 1,3 sekundy.
# 
#  Funkcje czyszczenia list przy tak "małych" listach stosunkowo nie różnią się prędkością działania lecz metoda CopyOver 
#  jest stosunkowo prosta i dla takich małych list wydajna lecz przy ogromnych dla większych list, koszt kopiowania i alokacji 
#  pamięci może być znaczny, co może wpłynąć na czas wykonania funkcji.
#  Funkcja ConvergingPointers jest bardziej wydajna dla dużych list, ponieważ nie wymaga kopiowania elementów i alokacji pamięci. 
#  Jednakże, może być mniej wydajna dla mniejszych list, ponieważ wymaga dodatkowego czasu na poruszanie się po liście.
# 
#  Funkcja szukania BinearySearch jest bardzo wydajna lecz potrzebuje uporządkowanej listy co wymaga dodatkowego sortowania,
#  Funkcje LinearSearch i SequentialSearch są praktycznie identycznie pod względem wydajności