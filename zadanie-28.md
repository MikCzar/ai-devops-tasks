Oto szczegółowe wyjaśnienie działania wcześniej zaprezentowanego skryptu, użytych bibliotek oraz instrukcja, jak go uruchomić i z niego korzystać.

📚 Jakie biblioteki są używane?
Skrypt opiera się na jednej, niezwykle potężnej i standardowej w ekosystemie Pythona bibliotece do obsługi protokołu HTTP:

requests: Najpopularniejsza biblioteka HTTP w Pythonie. Służy do wysyłania żądań do serwera Jenkins (GET, POST) oraz odbierania odpowiedzi.

requests.auth.HTTPBasicAuth: Moduł pomocniczy z pakietu requests, który odpowiada za bezpieczne przekazywanie danych uwierzytelniających (login i token API) w nagłówku HTTP Authorization w formacie Basic Auth.

⚙️ Jak działa skrypt krok po kroku?
Skrypt został napisany z wykorzystaniem programowania zorientowanego obiektowo (OOP) w postaci klasy JenkinsManager, co pozwala utrzymać porządek w kodzie i wielokrotnie używać sesji HTTP.

1. Inicjalizacja (__init__)
Tworzy instancję menedżera, przyjmując adres URL serwera Jenkins, login oraz wygenerowany w panelu API Token.

Wykorzystuje requests.Session(), co pozwala na utrzymanie stałego połączenia (tzw. connection pooling), przyspieszając kolejne zapytania, oraz automatyczne dołączanie danych autoryzacyjnych do każdego żądania.

2. Obsługa ochrony CSRF (_get_crumb)
Nowoczesne wersje Jenkinsa posiadają domyślnie włączoną ochronę przed fałszowaniem żądań międzywitrynowych (CSRF).

Zanim skrypt wyśle żądanie typu POST (np. w celu uruchomienia buildu), metoda ta odpytuje endpoint /crumbIssuer/api/json, aby pobrać specjalny token bezpieczeństwa (tzw. Crumb) i umieścić go w nagłówkach żądania. Bez tego Jenkins odrzuciłby żądanie uruchomienia zadania, zwracając błąd 403.

3. Listowanie zadań (list_jobs)
Wysyła żądanie GET na adres /api/json?tree=jobs[name,color,url].

Ważna optymalizacja Jenkins API: Parametr ?tree=... instruuje Jenkinsa, aby zwrócił wyłącznie wybrane pola (nazwę, kolor statusu i adres URL), co drastycznie zmniejsza ilość przesyłanych danych (wielkość odpowiedzi JSON), jeśli serwer ma setki zadań.

Kolor w Jenkinsie (blue = sukces, red = błąd, notbuilt = brak buildów) pozwala szybko ocenić stan projektu.

4. Sprawdzanie statusu ostatniego buildu (get_last_build_status)
Odpytuje konkretne zadanie pod adresem /job/{job_name}/api/json?tree=lastBuild[...].

Pobiera numer ostatniego buildu, jego wynik (SUCCESS, FAILURE, itp.) oraz czas trwania, a następnie wypisuje je w czytelnej formie w konsoli.

5. Uruchamianie zadania (trigger_job)
Wysyła żądanie POST na endpoint /job/{job_name}/build wraz z pobranym wcześniej nagłówkiem CSRF Crumb. Pomyślne zlecenie skutkuje uruchomieniem procesu budowania na serwerze Jenkins.

🚀 Jak używać tego skryptu? (Przykładowe polecenia)
Krok 1: Instalacja zależności
Upewnij się, że masz zainstalowanego Pythona oraz bibliotekę requests. W terminalu wpisz:

Bash
pip install requests
Krok 2: Przygotowanie Tokenu w Jenkinsie
Zanim uruchomisz skrypt, musisz wygenerować token API w Jenkinsie:

Zaloguj się do Jenkinsa.

Kliknij na swoją nazwę użytkownika w prawym górnym rogu -> Configure (Konfiguracja).

Znajdź sekcję API Token i kliknij Add new Token.

Skopiuj wygenerowany token (będzie potrzebny w skrypcie).

Krok 3: Uruchomienie skryptu
Zapisz kod skryptu w pliku o nazwie np. jenkins_manager.py.

Otwórz plik i w sekcji __main__ na samym dole uzupełnij swoje dane:

Python
JENKINS_URL = "http://localhost:8080"
USERNAME = "twoj_login"
API_TOKEN = "1122334455aabbcc..."  # Twój wygenerowany token
TARGET_JOB = "nazwa-twojego-zadania"
Uruchom skrypt w terminalu:

Bash
python jenkins_manager.py
Krok 4: Testowanie uruchomienia zadania
Jeśli chcesz, aby skrypt nie tylko odczytywał dane, ale także uruchomił zadanie, odkomentuj ostatnią linijkę w pliku:

Python
# Zmień to:
# jenkins.trigger_job(TARGET_JOB)

# Na to:
jenkins.trigger_job(TARGET_JOB)
Po ponownym uruchomieniu skryptu zadanie natychmiast zleci się w Jenkinsie.