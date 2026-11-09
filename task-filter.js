/**
 * Przetwarza tablicę zadań: filtruje ukończone, sortuje po id rosnąco i zwraca same tytuły.
 * 
 * @param {Array<{id: number, title: string, status: string}>} tasks - Tablica obiektów zadań
 * @returns {string[]} Tablica tytułów ukończonych zadań posortowanych po id
 */
function getCompletedTaskTitles(tasks) {
    return tasks
      .filter(task => task.status === 'completed')
      .sort((a, b) => a.id - b.id)
      .map(task => task.title);
  }