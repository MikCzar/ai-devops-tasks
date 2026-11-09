1. Analiza złożoności obecnego algorytmuZłożoność czasowa: $O(n^2)$ (kwadratowa)
Algorytm posiada dwie zagnieżdżone pętle. Zewnętrzna wykonuje się $n$ razy, a wewnętrzna średnio $n/2$ razy. Liczba operacji rośnie kwadratowo wraz ze wzrostem liczby elementów w tablicy (arr), co przy dużych tablicach mocno spowalnia działanie.Złożoność pamięciowa:Pamięć pomocnicza (auxiliary space): $O(1)$ – algorytm nie tworzy dodatkowych struktur danych poza zmiennymi licznikowymi.Pamięć całkowita: $O(n^2)$ w najgorszym przypadku (gdy niemal wszystkie pary sumują się do targetSum, tablica wynikowa pairs przechowuje bardzo dużo elementów).2. Czy można go zoptymalizować?Tak, algorytm można znacząco zoptymalizować, redukując złożoność czasową do $O(n)$ (liniową) poprzez użycie struktury danych typu Hash Map (lub Map w JavaScript) do śledzenia napotkanych elementów.Zoptymalizowana wersja ($O(n)$):JavaScriptfunction findPairsOptimized(arr, targetSum) {
  const map = new Map();
  const pairs = [];

  for (const num of arr) {
    const complement = targetSum - num;

    // Sprawdzamy, czy dopełnienie istnieje w mapie i ma dostępne wystąpienia
    if (map.has(complement) && map.get(complement) > 0) {
      pairs.push([complement, num]);
      // Zmniejszamy licznik dopełnienia, aby uniknąć ponownego użycia tego samego elementu
      map.set(complement, map.get(complement) - 1);
    } else {
      // Dodajemy bieżącą liczbę do mapy (lub zwiększamy jej licznik)
      map.set(num, (map.get(num) || 0) + 1);
    }
  }

  return pairs;
}
Jak działa optymalizacja?Zamiast sprawdzać każdą parę osobno za pomocą drugiej pętli, przechodzimy przez tablicę tylko raz ($O(n)$).Dla każdej liczby num obliczamy jej „dopełnienie” (complement = targetSum - num).Sprawdzamy w stałym czasie $O(1)$, czy to dopełnienie było już wcześniej widoczne w tablicy (dzięki obiektowi Map).Użycie licznika wystąpień pozwala poprawnie obsłużyć duplikaty w tablicy wejściowej.