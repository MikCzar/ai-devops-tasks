def find_duplicates(list_of_items):
    duplicates = []
    for i in range(len(list_of_items)):
        for j in range(i+1, len(list_of_items)):
            if list_of_items[i] == list_of_items[j] and list_of_items[i] not in duplicates:
                duplicates.append(list_of_items[i])
    return duplicates

    Tak, ten kod można znacznie zoptymalizować.Dlaczego obecna wersja jest niewydajna?Złożoność obliczeniowa $O(n^2)$: Posiada dwie zagnieżdżone pętle (for), co oznacza, że dla listy o długości $n$ wykona się około $\frac{n^2}{2}$ porównań. Przy dużych listach (np. kilkadziesiąt tysięcy elementów) taki program będzie działał bardzo wolno.Operacja not in duplicates: Sprawdzanie, czy element już znajduje się w liście wyników, ma złożoność $O(n)$ dla każdego znalezionego duplikatu, co jeszcze bardziej pogarsza wydajność.Optymalna wersja (złożoność $O(n)$)Najbardziej wydajnym podejściem w Pythonie jest wykorzystanie zestawów (set) lub liczenia wystąpień. Użycie set pozwala na znalezienie duplikatów w jednym przejściu przez listę z liniową złożonością czasową $O(n)$:Pythondef find_duplicates(list_of_items):
    seen = set()
    duplicates = set()
    
    for item in list_of_items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
            
    return list(duplicates)
Alternatywne rozwiązanie (krótsze, z użyciem collections.Counter)Jeśli zależy Ci na zwięzłości kodu, możesz użyć wbudowanej klasy Counter z modułu collections:Pythonfrom collections import Counter

def find_duplicates(list_of_items):
    counts = Counter(list_of_items)
    return [item for item, count in counts.items() if count > 1]
Podsumowanie korzyści:Wydajność: Zamiast tysięcy operacji dla dużych list, nowa wersja przechodzi przez listę tylko raz.Skalowalność: Świetnie radzi sobie nawet z bardzo dużymi zbiorami danych.