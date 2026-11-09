Przykład użycia:
JavaScript
const tasks = [
  { id: 3, title: 'Zbudować aplikację', status: 'pending' },
  { id: 1, title: 'Napisać dokumentację', status: 'completed' },
  { id: 2, title: 'Przetestować API', status: 'completed' },
  { id: 4, title: 'Wdrożyć na produkcję', status: 'pending' }
];

const result = getCompletedTaskTitles(tasks);
console.log(result); 
// Wynik: ['Napisać dokumentację', 'Przetestować API']
Jak to działa krok po kroku?
.filter(...) – wybiera z tablicy wyłącznie te obiekty, których pole status ma wartość "completed".

.sort(...) – porządkuje przefiltrowane elementy rosnąco według pola id (odejmując a.id - b.id).

.map(...) – przekształca tablicę obiektów w tablicę samych łańcuchów znaków zawierających wartości pola title.