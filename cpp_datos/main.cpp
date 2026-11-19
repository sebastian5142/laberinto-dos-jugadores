#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include "nodo.h"

using namespace std;

void mostrarRanking(Nodo* cabeza);

bool separarLinea(string linea, string campos[6]) {
    int numero = 0;
    string actual = "";

    for (int i = 0; i < (int)linea.length(); i++) {
        char c = linea[i];
        if (c == ',') {
            if (numero >= 5) {
                return false;      
            }
            campos[numero] = actual;
            numero++;
            actual = "";
        } else if (c != '\r') {
            actual = actual + c;
        }
    }

    campos[numero] = actual;
    numero++;

    return numero == 6;
}
Nodo* cargarHistorial(string nombreArchivo) {
    ifstream archivo(nombreArchivo.c_str());
    if (!archivo.is_open()) {
        cerr << "No se pudo abrir " << nombreArchivo << endl;
        return NULL;
    }

    string linea;
    getline(archivo, linea);   

    Nodo* cabeza = NULL;
    Nodo* cola = NULL;
    int id = 1;

    while (getline(archivo, linea)) {
        string campos[6];
        if (!separarLinea(linea, campos)) {
            continue;          
        }

        Nodo* nuevo = new Nodo;
        nuevo->dato.id = id;
        nuevo->dato.fecha = campos[0];
        nuevo->dato.jugador1 = campos[1];
        nuevo->dato.jugador2 = campos[2];
        nuevo->dato.resultado = campos[3];
        nuevo->dato.tiempo_segundos = atof(campos[4].c_str());
        nuevo->dato.limite_segundos = atoi(campos[5].c_str());
        nuevo->siguiente = NULL;
        id++;

        if (cabeza == NULL) {
            cabeza = nuevo;
        } else {
            cola->siguiente = nuevo;
        }
        cola = nuevo;
    }

    archivo.close();
    return cabeza;
}

void liberarLista(Nodo* cabeza) {
    while (cabeza != NULL) {
        Nodo* temporal = cabeza;
        cabeza = cabeza->siguiente;
        delete temporal;
    }
}

int main(int argc, char* argv[]) {
    string archivo = "historial.csv";
    if (argc > 1) {
        archivo = argv[1];
    }

    Nodo* historial = cargarHistorial(archivo);

    if (historial != NULL) {
        mostrarRanking(historial);
    }

    liberarLista(historial);
    return 0;
}
