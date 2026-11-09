Dlaczego to lepsze podejście?
Lepsza czytelność i czystość kodu (Clean Code): Usunięto powtarzające się słowa kluczowe return oraz warunki if-else. Całość ma teraz strukturę prostego słownika (mapy).

Łatwiejsza rozszerzalność (Zasada otwarto-zamknięta): Jeśli w przyszłości zechcesz dodać nowe środowisko (np. qa albo loadtest), wystarczy dopisać jedną linię w obiekcie environments, zamiast dopisywać kolejny blok else if.

Bezpieczny fallback: Zapis environments[env] || environments.development elegancko obsługuje sytuację, w której przekazano nieznane środowisko (lub undefined), automatycznie zwracając bezpieczną konfigurację domyślną.