dockerfile node

Oto prosty, zoptymalizowany przykład pliku Dockerfile dla aplikacji w Node.js, wraz z wyjaśnieniem kolejnych kroków oraz instrukcjami uruchomienia.

Przykładowy Dockerfile
Dockerfile
# 1. Wybierz oficjalny obraz bazowy Node.js (wersja LTS)
FROM node:20-alpine

# 2. Ustaw katalog roboczy wewnątrz kontenera
WORKDIR /app

# 3. Skopiuj pliki z definicją zależności (package.json i package-lock.json)
COPY package*.json ./

# 4. Zainstaluj zależności produkcyjne
RUN npm ci --only=production

# 5. Skopiuj pozostały kod źródłowy aplikacji
COPY . .

# 6. Określ port, na którym nasłuchuje aplikacja (np. 3000)
EXPOSE 3000

# 7. Zdefiniuj domyślną komendę uruchamiającą aplikację
CMD ["node", "server.js"]
Wyjaśnienie poszczególnych linijek:
FROM node:20-alpine – Korzystamy z lekkiej dystrybucji Linuksa (Alpine Linux) z zainstalowanym Node.js w wersji 20 LTS. Obrazy oparte na Alpine są bardzo małe, co przyspiesza pobieranie i zwiększa bezpieczeństwo.

WORKDIR /app – Tworzy katalog /app wewnątrz kontenera i ustawia go jako domyślny katalog dla wszystkich kolejnych poleceń.

COPY package*.json ./ – Kopiujemy najpierw same pliki menedżera pakietów. Dzięki temu Docker może wykorzystać cache warstw – jeśli zależności się nie zmieniły, ten krok nie wykona się ponownie przy kolejnym budowaniu obrazu.

RUN npm ci --only=production – Instaluje wyłącznie zależności produkcyjne (użycie npm ci jest szybsze i bezpieczniejsze w środowiskach CI/CD niż zwykłe npm install).

COPY . . – Kopiuje resztę plików projektu z komputera lokalnego do wnętrza kontenera.

EXPOSE 3000 – Informuje Dockera, że aplikacja wewnątrz kontenera nasłuchuje na porcie 3000 (jest to też dobra dokumentacja dla innych programistów).

CMD ["node", "server.js"] – Główna komenda uruchamiana w momencie startu kontenera (zakładając, że plik startowy Twojej aplikacji to server.js).

Jak zbudować obraz i uruchomić kontener?
Zbuduj obraz (znajdując się w folderze z plikiem Dockerfile i projektem):

Bash
docker build -t moja-aplikacja-node .
Uruchom kontener:

Bash
docker run -p 3000:3000 moja-aplikacja-node
Flaga -p 3000:3000 przekierowuje port 3000 z Twojego komputera na port 3000 wewnątrz kontenera.

Napisz prosty Dockerfile dla aplikacji Node.js, który:

używa Node 18 jako obrazu bazowego
kopiuje pliki package.json i package-lock.json
instaluje zależności
kopiuje resztę plików aplikacji
wystawia port 3000
uruchamia aplikację poleceniem "npm start" 
Oto gotowy, prosty Dockerfile spełniający wszystkie podane przez Ciebie wymagania:

Dockerfile
# 1. Użyj Node 18 jako obrazu bazowego
FROM node:18

# 2. Ustaw katalog roboczy wewnątrz kontenera
WORKDIR /app

# 3. Kopiuj pliki package.json i package-lock.json
COPY package*.json ./

# 4. Zainstaluj zależności
RUN npm install

# 5. Kopiuj resztę plików aplikacji
COPY . .

# 6. Wystaw port 3000
EXPOSE 3000

# 7. Uruchom aplikację poleceniem "npm start"
CMD ["npm", "start"]
Jak tego użyć?
Zapisz powyższy kod w pliku o nazwie dokładnie Dockerfile w głównym folderze swojej aplikacji Node.js.

Zbuduj obraz poleceniem:

Bash
docker build -t moja-app-node18 .
Uruchom kontener:

Bash
docker run -p 3000:3000 moja-app-node18