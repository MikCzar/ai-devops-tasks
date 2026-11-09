services:
  web:
    image: nginx
    ports:
      - "80:80"
  app:
    build: .
    ports
      - "3000:3000"
    depends_on:
      - db
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD=password

Nie, ten plik nie jest poprawny i zawiera kilka błędów składniowych związanych z wcięciami w formacie YAML oraz brakami w strukturze.

Oto poprawiona, w pełni działająca wersja tego pliku:

YAML
version: '3.8'

services:
  web:
    image: nginx
    ports:
      - "80:80"

  app:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - db

  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: password
Co było nie tak w Twojej wersji?
Błędy wcięć (indentation): W YAML wcięcia mają kluczowe znaczenie. Listy (elementy zaczynające się od myślnika -) muszą być wcięte głębiej niż klucz, do którego należą (np. pod ports: czy depends_on:). W Twoim pliku myślniki były wyrównane z kluczami, co powodowało błąd parsowania.

Brak dwukropka: W linijce z ports pod usługą app zapomniałeś dodać dwukropka (ports: zamiast ports).

Składnia zmiennych środowiskowych: W sekcji db zapis POSTGRES_PASSWORD=password zadziała w Dockerze, ale dobrą i bardziej czytelną praktyką jest użycie dwukropka: POSTGRES_PASSWORD: password.