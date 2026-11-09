Oto szczegółowa interpretacja zebranych metryk serwera API oraz identyfikacja kluczowych problemów wraz z rekomendacjami optymalizacyjnymi.

🔍 Interpretacja danych i zidentyfikowane problemy
Krytyczne zużycie pamięci RAM (Największy problem)

Stan faktyczny: Maksymalne użycie pamięci osiągnęło 3.5 GB z 4 GB dostępnych (87.5%).

Problem: Dla aplikacji w środowisku Node.js (szczególnie przy limicie 4 GB na całym kontenerze/serwerze) zbliżenie się do 90% pojemności sterty (heap) oznacza drastyczny wzrost aktywności mechanizmu Garbage Collection (GC). Zatrzymania GC powodują nagłe skoki opóźnień (co tłumaczy wysoki p99) oraz grożą awarią typu OOM (Out Of Memory) i nagłym restartem kontenera przez system orkiestracji (np. Dockera).

Wysokie opóźnienia ogonowe (Tail Latency - p99 = 1200ms)

Stan faktyczny: Średni czas odpowiedzi (230ms) i p95 (450ms) wyglądają rozsądnie, ale p99 wynoszące 1.2 sekundy oznacza, że co setne zapytanie czeka bardzo długo.

Problem: Przy 15 000 zapytań na dobę (~0.17 req/s – ruch jest relatywnie nieduży) wynik powyżej 1 sekundy wskazuje na blokujące operacje synchroniczne, cykle Garbage Collection wywołane brakiem pamięci lub nieindeksowane zapytania do bazy danych MongoDB (np. kosztowne skany całej kolekcji).

Współczynnik błędów 5xx (120 błędów)

Stan faktyczny: 120 błędów serwera na 15 000 zapytań daje wskaźnik na poziomie ok. 0.8%.

Problem: Chociaż to poniżej 1%, przy tak niskim ruchu 120 błędów wewnętrznych to sygnał, że część zapytań kończy się wyjątkiem (prawdopodobnie timeouty połączeń z bazą danych lub błędy braku pamięci podczas przetwarzania większych ładunków danych).

🚀 Sugestie poprawy wydajności
1. Rozwiązanie problemów z pamięcią (Memory & Garbage Collection)
Zwiększenie zasobów: Jeśli to możliwe w środowisku Docker/chmurze, zwiększ limit pamięci RAM z 4 GB do co najmniej 6 GB or 8 GB.

Jawne ograniczenie sterty Node.js: Skonfiguruj flagę --max-old-space-size w Node.js, aby proces nie próbował pochłonąć całej pamięci maszyny, zanim zadziała systemowy OOM Killer:

Bash
node --max-old-space-size=3072 server.js
Audyt pod kątem wycieków pamięci: Przeanalizuj zużycie pamięci w czasie – jeśli rośnie ono liniowo bez spadków po GC, w kodzie występuje memory leak (np. rosnące tablice cache, niezamykane strumienie lub nasłuchiwacze zdarzeń).

2. Optymalizacja bazy danych (MongoDB)
Indeksowanie: Upewnij się, że pola wykorzystywane w zapytaniach do MongoDB (szczególnie te filtrowane i sortowane, np. w endpointach typu /api/users czy endpointach zadań) posiadają odpowiednie indeksy. Brak indeksów przy rosnącej bazie danych gwałtownie zwiększa zużycie CPU i RAM oraz wydłuża czas odpowiedzi.

Paginacja i limity: Wymuś stosowanie paginacji (np. ograniczenie limit do max 100 elementów), aby aplikacja nie próbowała ładować do pamięci RAM tysięcy dokumentów naraz.

3. Diagnostyka błędów 5xx
Przejrzyj logi błędów aplikacji z ostatnich 24 godzin, aby powiązać momenty wystąpienia 120 błędów 5xx ze skokami użycia pamięci lub konkretnymi endpointami.