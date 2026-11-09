Oto profesjonalna dokumentacja endpointu w formacie Markdown, przygotowana zgodnie z podanymi wymaganiami:

GET /api/users
Opis
Zwraca paginowaną listę użytkowników. Pozwala na filtrowanie wyników według roli oraz kontrolowanie liczby zwracanych elementów na stronie.

Parametry zapytania (Query Parameters)
Nazwa	Typ	Wymagany	Domyślnie	Opis
page	Integer	Nie	1	Numer żądanej strony (wartość >= 1).
limit	Integer	Nie	10	Liczba wyników na stronę (zakres: 1–100).
role	String	Nie	brak	Opcjonalny filtr według roli użytkownika (np. admin, user).
Przykład żądania
Bash
curl -X GET "https://api.example.com/api/users?page=1&limit=2&role=admin" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Accept: application/json"
Przykładowa odpowiedź
Status: 200 OK

Content-Type: application/json

JSON
{
  "data": [
    {
      "id": 1,
      "name": "Jan Kowalski",
      "email": "jan.kowalski@example.com",
      "role": "admin",
      "createdAt": "2026-01-15T10:30:00Z"
    },
    {
      "id": 4,
      "name": "Anna Nowak",
      "email": "anna.nowak@example.com",
      "role": "admin",
      "createdAt": "2026-02-10T14:20:00Z"
    }
  ],
  "pagination": {
    "totalItems": 12,
    "totalPages": 6,
    "currentPage": 1,
    "itemsPerPage": 2
  }
}