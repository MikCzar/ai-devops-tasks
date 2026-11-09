function findPairsOptimized(arr, targetSum) {
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