/**
 * Pobiera dane użytkownika z zewnętrznego API na podstawie jego unikalnego identyfikatora.
 * 
 * @param {string|number} userId - ID użytkownika, którego dane mają zostać pobrane.
 * @returns {Promise<{name: string, email: string, lastLogin: Date}|null>} Obiekt zawierający przetworzone dane użytkownika (w tym obiekt Date dla ostatniego logowania) lub null w przypadku błędu sieciowego lub HTTP.
 */
function fetchUserData(userId) {
    return fetch(`https://api.example.com/users/${userId}`)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        return {
          name: data.name,
          email: data.email,
          lastLogin: new Date(data.lastLoginTimestamp)
        };
      })
      .catch(error => {
        console.error('Fetch error:', error);
        return null;
      });
  }