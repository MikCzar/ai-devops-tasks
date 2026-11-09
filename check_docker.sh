#!/bin/bash

# Sprawdź, czy usługa Docker jest aktywna
if systemctl is-active --quiet docker; then
    echo "Usługa Docker już działa."
else
    echo "Usługa Docker nie działa. Próbuję uruchomić..."
    
    # Uruchom usługę Docker (wymaga uprawnień roota)
    sudo systemctl start docker

    # Sprawdź czy operacja się powiodła
    if systemctl is-active --quiet docker; then
        echo "Sukces! Usługa Docker została pomyślnie uruchomiona."
    else
        echo "Błąd: Nie udało się uruchomić usługi Docker." >&2
        exit 1
    fi
fi