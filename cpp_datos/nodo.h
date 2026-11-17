#ifndef NODO_H
#define NODO_H

#include <string>

struct Resultado {
    int id;                    
    std::string fecha;
    std::string jugador1;
    std::string jugador2;
    std::string resultado;     
    double tiempo_segundos;
    int limite_segundos;
};

struct Nodo {
    Resultado dato;
    Nodo* siguiente;
};

#endif
