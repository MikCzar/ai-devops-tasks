Uruchomienie Jenkinsa z wykorzystaniem pliku JCasC (Jenkins Configuration as Code) w środowisku Docker to najszybszy sposób na uzyskanie w pełni powtarzalnej i skonfigurowanej instancji serwera CI/CD bez konieczności ręcznego klikania w interfejsie graficznym.Poniższy przewodnik krok po kroku wyjaśnia, jak przygotować i uruchomić takie środowisko.1.Stworzenie struktury katalogów i plików:Przygotowanie lokalnego workspace.Utwórz nowy katalog na swoim komputerze (np. jenkins-docker) i umieść w nim przygotowany wcześniej plik konfiguracyjny o nazwie jenkins.yaml.2.Przygotowanie pliku instalacji wtyczek (plugins.txt):Wymagane moduły dla JCasC i Job DSL.W tym samym katalogu utwórz plik plugins.txt. Pozwoli on na automatyczne pobranie wtyczek niezbędnych do obsługi kodu konfiguracyjnego oraz pipeline'ów:Plaintextconfiguration-as-code:latest
git:latest
workflow-aggregator:latest
job-dsl:latest
3.Konfiguracja pliku docker-compose.yml:Wiązanie wolumenów i zmiennych środowiskowych.Utwórz plik docker-compose.yml. Wskazujemy w nim zmienną CASC_JENKINS_CONFIG, która mówi Jenkinsowi, gdzie szukać pliku konfiguracyjnego YAML:YAMLversion: '3.8'

services:
  jenkins:
    image: jenkins/jenkins:lts
    container_name: jenkins-jcasc
    restart: unless-stopped
    ports:
      - "8080:8080"
      - "50000:50000"
    environment:
      - CASC_JENKINS_CONFIG=/var/jenkins_home/casc_configs/jenkins.yaml
      - ADMIN_PASSWORD=superTajneHaslo123
    volumes:
      - jenkins_home:/var/jenkins_home
      - ./jenkins.yaml:/var/jenkins_home/casc_configs/jenkins.yaml
      # Opcjonalnie: automatyczna instalacja wtyczek z pliku plugins.txt przy starcie
      # - ./plugins.txt:/usr/share/jenkins/ref/plugins.txt

volumes:
  jenkins_home:
4.Uruchomienie kontenera Jenkins:Start za pomocą Docker Compose.Otwórz terminal w katalogu z plikiem docker-compose.yml i uruchom kontener w tle:Bashdocker compose up -d
Pierwsze uruchomienie może potrwać kilkadziesiąt sekund, podczas których Jenkins pobiera obraz, inicjalizuje katalog domowy i przetwarza plik jenkins.yaml.5.Weryfikacja i logowanie do panelu:Dostęp przez przeglądarkę webową.Przejdź w przeglądarce pod adres http://localhost:8080.Dzięki konfiguracji JCasC pominięty zostaje kreator wstępnej konfiguracji oraz konieczność wpisywania jednorazowego klucza administratora. Zaloguj się danymi zdefiniowanymi w pliku YAML:Login: adminHasło: superTajneHaslo123 (zmienna środowiskowa z pliku docker-compose)Jak działa ta integracja?Automatyczne wczytanie: Podczas startu Jenkinsa wtyczka Configuration as Code odczytuje plik wskazany przez zmienną CASC_JENKINS_CONFIG.Brak konieczności konfiguracji ręcznej: Użytkownicy, narzędzia (Node.js, Maven) oraz przykładowe zadanie node-api-production-pipeline pojawią się w systemie w kilka sekund po uruchomieniu serwera, gotowe do natychmiastowego użycia.Modyfikacja konfiguracji: Jeśli zmienisz coś w pliku jenkins.yaml, wystarczy przejść w panelu Jenkinsa do zakładki Manage Jenkins -> Configuration as Code i kliknąć przycisk Reload, aby natychmiast wdrożyć zmiany bez restartowania kontenera.