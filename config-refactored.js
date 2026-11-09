function getEnvironmentConfig(env) {
    const environments = {
      development: {
        apiUrl: 'http://localhost:3000/api',
        debug: true,
        timeout: 5000
      },
      testing: {
        apiUrl: 'http://test-server:3000/api',
        debug: true,
        timeout: 5000
      },
      staging: {
        apiUrl: 'https://staging.example.com/api',
        debug: false,
        timeout: 10000
      },
      production: {
        apiUrl: 'https://api.example.com',
        debug: false,
        timeout: 15000
      }
    };
  
    // Zwraca konfigurację dla żądanego środowiska lub domyślną (development), jeśli klucz nie istnieje
    return environments[env] || environments.development;
  }