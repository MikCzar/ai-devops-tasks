Jak rozwiązać problem z dużym zużyciem pamięci przez kontener Docker?

Wysokie zużycie pamięci RAM przez kontener Docker to częsty problem, który najczęściej wynika z braku limitów zasobów, wycieków pamięci w samej aplikacji lub niewłaściwej konfiguracji środowiska uruchomieniowego (np. maszyny wirtualnej Node.js czy bazy danych).

Oto sprawdzone kroki diagnostyczne i naprawcze, ułożone od najprostszych i najmniej inwazyjnych:

1
Sprawdź aktualne zużycie zasobów w czasie rzeczywistym
Krok diagnostyczny
Uruchom w terminalu polecenie monitorujące, aby zobaczyć, które kontenery faktycznie zużywają najwięcej pamięci RAM:

Bash
docker stats
Verification: Zobaczysz listę uruchomionych kontenerów wraz z bieżącym zużyciem pamięci oraz ustalonymi dla nich limitami (kolumna LIMIT).

2
Ustaw twardy limit pamięci dla kontenera
Najszybsze zabezpieczenie systemowe
Jeśli kontener nie ma ograniczeń, może zużyć całą dostępną pamięć hosta i doprowadzić do awarii systemu (lub zamknięcia procesu przez mechanizm OOM Killer). Ogranicz pamięć przy ponownym uruchomieniu kontenera, np. do 512 megabajtów:

Bash
docker run -d --memory="512m" --memory-swap="512m" --name moja-aplikacja -p 3000:3000 moj-obraz
Wskazówka: W przypadku pliku docker-compose.yml dodaj sekcję deploy.resources.limits lub mem_limit: 512m.
Verification: Ponowne wywołanie docker stats pokaże nową, ustaloną wartość w kolumnie LIMIT.

3
Zoptymalizuj pamięć podręczną maszyny wirtualnej (np. Node.js)
Rozwiązanie specyficzne dla aplikacji
Wiele technologii (np. Node.js, Java JVM) domyślnie dopasowuje swoje limity pamięci do zasobów całego hosta, a nie ograniczeń kontenera. Przykładowo, w aplikacjach Node.js warto jawnie ograniczyć stertę pamięci (Heap), dodając flagę --max-old-space-size:

Dockerfile
# W pliku Dockerfile lub jako argument CMD:
CMD ["node", "--max-old-space-size=384", "server.js"]
Verification: Zużycie pamięci przez proces wewnątrz kontenera powinno ustabilizować się poniżej zadanego progu.

4
Sprawdź logi pod kątem wycieków pamięci
Diagnostyka kodu
Jeśli pamięć stale rośnie aż do osiągnięcia limitu, w aplikacji prawdopodobnie występuje wyciek pamięci (memory leak). Sprawdź logi kontenera pod kątem nieskończonych pętli, narastających buforów lub błędów:

Bash
docker logs --tail 100 -f <nazwa_kontenera>
Verification: Otrzymasz podgląd ostatnich komunikatów aplikacji pomagający zlokalizować miejsce, w którym zasoby nie są zwalniane.

Ryzyko zamknięcia kontenera (OOM Killed)
Jeśli kontener przekroczy ustawiony limit pamięci (np. --memory="512m"), system operacyjny natychmiast ubije proces aplikacji, a kontener zakończy działanie z kodem błędu 137.

Jesteś doświadczonym DevOps Engineerem z 10-letnim doświadczeniem. Jak rozwiązać problem z dużym zużyciem pamięci przez kontener Docker?

Wysokie zużycie pamięci RAM przez kontener Docker to klasyczny problem operacyjny. Jako DevOps Engineer podszedłbym do tego metodycznie: od natychmiastowego zabezpieczenia systemu, przez diagnozę, aż po trwałe rozwiązanie w kodzie lub konfiguracji.

Oto sprawdzony proces radzenia sobie z tym problemem:

1
Sprawdź aktualne zużycie zasobów
Krok diagnostyczny
Uruchom polecenie monitorujące w czasie rzeczywistym, aby zidentyfikować, który kontener pożera pamięć i jak blisko jest limitu:

Bash
docker stats
Verification: Zobaczysz listę kontenerów z ich bieżącym zużyciem pamięci RAM oraz wartością w kolumnie LIMIT (jeśli jest ustawiona).

2
Ustaw twardy limit pamięci dla kontenera
Ochrona systemu hosta
Jeśli kontener nie ma limitów, może doprowadzić do wyczerpania pamięci na całej maszynie (hostcie) i zresetowania innych usług. Ogranicz pamięć przy starcie kontenera (np. do 1 GB):

Bash
docker run -d --memory="1g" --memory-swap="1g" --name moja-aplikacja -p 3000:3000 moj-obraz
Wskazówka: W środowiskach produkcyjnych zawsze definiuj limity w pliku docker-compose.yml (sekcja deploy.resources.limits) lub w manifeście Kubernetes (resources.limits.memory).
Verification: Ponowne uruchomienie docker stats potwierdzi, że limit został nałożony.

3
Dopasuj parametry maszyn wirtualnych (np. Node.js, Java)
Optymalizacja środowiska wykonawczego (Runtime)
Wiele języków i środowisk (np. Node.js, JVM) domyślnie alokuje pamięć na podstawie zasobów całego hosta, a nie kontenera. Przykładowo, w aplikacjach Node.js jawnie ogranicz maksymalną stertę pamięci (Heap):

Dockerfile
# W pliku Dockerfile lub bezpośrednio w parametrach CMD:
CMD ["node", "--max-old-space-size=768", "server.js"]
Verification: Proces wewnątrz kontenera nie będzie bez limitu rozszerzał swojej sterty, co ustabilizuje zużycie pamięci poniżej progu odcięcia.

4
Zdiagnozuj potencjalny wyciek pamięci (Memory Leak)
Analiza kodu i logów
Jeśli pamięć stale rośnie bez względu na ruch, w aplikacji występuje wyciek. Sprawdź logi pod kątem błędów lub narastających kolejek:

Bash
docker logs --tail 100 -f <nazwa_kontenera>
Verification: Otrzymasz podgląd ostatnich zdarzeń i cykli pracy aplikacji pomagający zlokalizować miejsce, w którym zasoby nie są zwalniane przez Garbage Collector.

Ryzyko zamknięcia kontenera (OOM Killed)
Gdy kontener przekroczy twardy limit pamięci ustawiony flagą --memory, jądro systemu operacyjnego natychmiast zatrzyma proces aplikacji, a kontener zakończy działanie z kodem wyjścia 137.