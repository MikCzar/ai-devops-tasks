import requests
from requests.auth import HTTPBasicAuth

class JenkinsManager:
    def __init__(self, base_url, username, api_token):
        """
        Inicjalizacja menedżera Jenkins API.
        
        :param base_url: Adres URL serwera Jenkins (np. 'http://localhost:8080')
        :param username: Nazwa użytkownika Jenkins
        :param api_token: Token API użytkownika (zalecane zamiast hasła)
        """
        self.base_url = base_url.rstrip('/')
        self.auth = HTTPBasicAuth(username, api_token)
        self.session = requests.Session()
        self.session.auth = self.auth

    def _get_crumb(self):
        """
        Pobiera CSRF Crumb wymagany przez Jenkinsa do żądań typu POST (np. uruchamianie buildu).
        """
        try:
            response = self.session.get(f"{self.base_url}/crumbIssuer/api/json")
            if response.status_code == 200:
                data = response.json()
                return {data['crumbRequestField']: data['crumb']}
        except requests.exceptions.RequestException:
            # Jeśli ochrona CSRF nie jest włączona w Jenkinsie, zwracamy pusty słownik
            pass
        return {}

    def list_jobs(self):
        """
        Listuje wszystkie zadania (jobs) na serwerze Jenkins wraz z ich statusem.
        """
        endpoint = f"{self.base_url}/api/json?tree=jobs[name,color,url]"
        try:
            response = self.session.get(endpoint)
            response.raise_for_status()
            jobs = response.json().get('jobs', [])
            
            print("\n=== LISTA ZADAŃ W JENKINS ===")
            for job in jobs:
                # Kolor w Jenkinsie określa status ostatniego buildu (np. blue = sukces, red = błąd)
                print(f"- Nazwa: {job['name']} | Status (Kolor): {job['color']}")
            return jobs
        except requests.exceptions.RequestException as e:
            print(f"[BŁĄD] Nie udało się pobrać listy zadań: {e}")
            return []

    def get_last_build_status(self, job_name):
        """
        Sprawdza status ostatniego buildu dla konkretnego zadania.
        """
        endpoint = f"{self.base_url}/job/{job_name}/api/json?tree=lastBuild[number,result,timestamp,duration]"
        try:
            response = self.session.get(endpoint)
            if response.status_code == 404:
                print(f"[INFO] Zadanie '{job_name}' nie posiada jeszcze żadnych buildów.")
                return None
            
            response.raise_for_status()
            build_info = response.json().get('lastBuild')
            
            if not build_info:
                print(f"[INFO] Brak historii buildów dla zadania '{job_name}'.")
                return None

            print(f"\n=== OSTATNI BUILD DLA: {job_name} ===")
            print(f"  Numer buildu: #{build_info.get('number')}")
            print(f"  Wynik: {build_info.get('result') or 'W TRAKCIE / NIEZNANY'}")
            return build_info
        except requests.exceptions.RequestException as e:
            print(f"[BŁĄD] Nie udało się pobrać statusu buildu dla '{job_name}': {e}")
            return None

    def trigger_job(self, job_name):
        """
        Uruchamia wybrane zadanie w Jenkinsie.
        """
        endpoint = f"{self.base_url}/job/{job_name}/build"
        headers = self._get_crumb()
        
        try:
            response = self.session.post(endpoint, headers=headers)
            # Jenkins zwraca kod 201 Created lub 200 OK przy pomyślnym zleceniu buildu
            response.raise_for_status()
            print(f"\n[SUKCES] Zadanie '{job_name}' zostało pomyślnie uruchomione!")
            return True
        except requests.exceptions.RequestException as e:
            print(f"\n[BŁĄD] Nie udało się uruchomić zadania '{job_name}': {e}")
            if response.status_code == 403:
                print("[Wskazówka] Sprawdź uprawnienia użytkownika lub poprawność tokena API.")
            return False


# --- PRZYKŁAD UŻYCIA ---
if __name__ == "__main__":
    # Konfiguracja połączenia (uzupełnij własnymi danymi)
    JENKINS_URL = "http://localhost:8080"
    USERNAME = "twoj_login"
    API_TOKEN = "twoj_api_token"  # Wygeneruj w Jenkins: User -> Configure -> API Token
    TARGET_JOB = "moje-pierwsze-zadanie"

    # Inicjalizacja klienta
    jenkins = JenkinsManager(JENKINS_URL, USERNAME, API_TOKEN)

    # 1. Listowanie wszystkich zadań
    jobs_list = jenkins.list_jobs()

    # 2. Sprawdzanie statusu ostatniego buildu dla wybranego zadania
    if jobs_list:
        jenkins.get_last_build_status(TARGET_JOB)

    # 3. Uruchomienie wybranego zadania
    # jenkins.trigger_job(TARGET_JOB)