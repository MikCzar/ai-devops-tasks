Oto przekształcone dane z formatu JSON do formatu CSV. Ponieważ pole roles jest tablicą, zostało ono połączone przecinkami i ujęte w cudzysłów, co jest standardową praktyką w plikach CSV dla danych złożonych:

Fragment kodu
id,name,email,roles
1,Jan Kowalski,jan@example.com,"admin,user"
2,Anna Nowak,anna@example.com,"user"