#include <iostream>
#include <iomanip>
#include <string>
#include "nodo.h"

using namespace std;

bool hayGanador(Resultado r) {
    return r.resultado == "JUGADOR 1" || r.resultado == "JUGADOR 2";
}

bool debeIrDespues(Resultado a, Resultado b) {
    bool ganaA = hayGanador(a);
    bool ganaB = hayGanador(b);

    if (ganaA && !ganaB) {
        return false;
    }
    if (!ganaA && ganaB) {
        return true;
    }
    if (ganaA && ganaB && a.tiempo_segundos != b.tiempo_segundos) {
        return a.tiempo_segundos > b.tiempo_segundos;
    }
    return a.id > b.id;
}

void ordenarLista(Nodo* cabeza) {
    bool huboCambio = true;

    while (huboCambio) {
        huboCambio = false;
        Nodo* actual = cabeza;

        while (actual != NULL && actual->siguiente != NULL) {
            if (debeIrDespues(actual->dato, actual->siguiente->dato)) {
                Resultado temporal = actual->dato;
                actual->dato = actual->siguiente->dato;
                actual->siguiente->dato = temporal;
                huboCambio = true;
            }
            actual = actual->siguiente;
        }
    }
}

void mostrarRanking(Nodo* cabeza) {
    ordenarLista(cabeza);

    cout << fixed << setprecision(2);

    int puesto = 1;
    Nodo* actual = cabeza;

    while (actual != NULL) {
        cout << puesto << "|"
             << actual->dato.id << "|"
             << actual->dato.resultado << "|"
             << actual->dato.tiempo_segundos << "|"
             << actual->dato.fecha << endl;

        puesto++;
        actual = actual->siguiente;
    }
}
