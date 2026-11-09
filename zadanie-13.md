Co oznaczają użyte znaczniki JSDoc?
@param {string|number} userId – określa, że funkcja przyjmuje argument userId, który może być ciągiem znaków (string) lub liczbą (number).

@returns {Promise<...|null>} – informuje, że funkcja zwraca obiekt typu Promise, którego wynik (po rozwiązaniu) będzie albo zmapowanym obiektem użytkownika, albo wartością null (w przypadku złapania błędu w bloku .catch).