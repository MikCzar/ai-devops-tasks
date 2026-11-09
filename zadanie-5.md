Stwórz prosty diagram ASCII Art przedstawiający połączenie klienta, serwera aplikacji i bazy danych.

Oto prosty diagram ASCII Art przedstawiający przepływ żądań w architekturze trójwarstwowej:

Plaintext
+-----------+            +--------------------+            +-------------+
|  Klient   |  ------->  |  Serwer Aplikacji  |  ------->  | Baza Danych |
| (Przegląd/API) |  HTTP/HTTPS |   (Backend/Logika) |   SQL    |  (MySQL/PG) |
+-----------+            +--------------------+            +-------------+

Dodaj do diagramu opisy elementów i kierunki przepływu danych.

Oto rozbudowany diagram ASCII Art, który uwzględnia zarówno kierunki przepływu danych (w obie strony), jak i opis poszczególnych etapów komunikacji w architekturze trójwarstwowej:

Plaintext
+------------+       1. Żądanie HTTP/HTTPS (np. GET /users)      +------------------+       2. Zapytanie SQL (np. SELECT...)     +-------------+
|   Klient   | ------------------------------------------------> | Serwer Aplikacji | -----------------------------------------> | Baza Danych |
| (Frontend) | <------------------------------------------------ |    (Backend)     | <----------------------------------------- |  (Storage)  |
+------------+       4. Odpowiedź z danymi (np. JSON / HTML)     +------------------+       3. Zwrócenie wyników z bazy          +-------------+
Opis przepływu danych krok po kroku:
Klient 
→ Serwer Aplikacji (Żądanie): Przeglądarka internetowa, aplikacja mobilna lub zewnętrzny klient wysyła żądanie HTTP/HTTPS do serwera (np. żądanie pobrania listy użytkowników).

Serwer Aplikacji 
→ Baza Danych (Zapytanie): Serwer odbiera żądanie, przetwarza logikę biznesową i generuje odpowiednie zapytanie bazodanowe (np. w języku SQL).

Baza Danych 
→ Serwer Aplikacji (Odpowiedź): Baza przetwarza zapytanie, odnajduje rekordy w tabelach i odsyła surowe dane z powrotem do serwera aplikacji.

Serwer Aplikacji 
→ Klient (Wynik): Serwer formatuje otrzymane dane (najczęściej do formatu JSON lub HTML) i odsyła gotową odpowiedź do klienta, który wyświetla ją użytkownikowi.