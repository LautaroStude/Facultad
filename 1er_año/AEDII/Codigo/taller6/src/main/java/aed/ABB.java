package aed;

import java.util.*;

// Todos los tipos de datos "Comparables" tienen el método compareTo()
// elem1.compareTo(elem2) devuelve un entero. Si es mayor a 0, entonces elem1 > elem2
public class ABB<T extends Comparable<T>> {
    private Nodo raiz;
    private int cardinal;

    private class Nodo {
        T valor;
        Nodo izq;
        Nodo der;
        Nodo padre;

        Nodo(T v) {
            valor = v;
            izq = null;
            der = null;
            padre = null;
        }
    }

    public ABB() {
        raiz = null;
        cardinal = 0;;
    }

    public int cardinal() {
        return cardinal;
    }

    public T minimo(){
        T res = null;
        if (raiz != null) {
            Nodo actual = raiz;
            while (actual.izq != null) {
                actual = actual.izq;
            }
            res = actual.valor;
        }
        return res;
    }

    public T maximo(){
        T res = null;
        if (raiz != null) {
            Nodo actual = raiz;
            while (actual.der != null) {
                actual = actual.der;
            }
            res = actual.valor;
        }
        return res;
    }

    public void insertar(T elem){
        if (raiz == null) {
            raiz = new Nodo(elem);
            cardinal++;
        } else {
            Nodo actual = raiz;
            Nodo padre = null;
            boolean insertado = false;

            while (actual != null && !insertado) {
                padre = actual;
                int comparacion = elem.compareTo(actual.valor);
                
                if (comparacion == 0) {
                    insertado = true; // el elemento ya existe corto la iteración
                } else if (comparacion < 0) {
                    actual = actual.izq;
                } else {
                    actual = actual.der;
                }
            }
            // si salgo del while porque llegue a una hoja lo inserto
            if (!insertado) {
                Nodo nuevo = new Nodo(elem);
                nuevo.padre = padre;
                
                if (elem.compareTo(padre.valor) < 0) {
                    padre.izq = nuevo;
                } else {
                    padre.der = nuevo;
                }
                
                cardinal++;
            }
        }
    }

    public boolean pertenece(T elem){
        boolean encontrado = false;
        Nodo actual = raiz;
        
        while (actual != null && !encontrado) {
            int comparacion = elem.compareTo(actual.valor);
            if (comparacion == 0) {
                encontrado = true;
            } else if (comparacion < 0) {
                actual = actual.izq;
            } else {
                actual = actual.der;
            }
        }
        
        return encontrado;
    }

    public void eliminar(T elem){
        throw new UnsupportedOperationException("No implementada aun");
    }

    public String toString(){
        String resultado = "{";
        ABB_Iterador it = iterador();
        
        while (it.haySiguiente()) {
            resultado += it.siguiente().toString();
            if (it.haySiguiente()) {
                resultado += ", ";
            }
        }    
        resultado += "}";
        return resultado;
    }

    public class ABB_Iterador implements Iterador<T> {
        private Nodo _actual;

        public ABB_Iterador() {
            _actual = raiz;
            if (_actual != null) {
                while (_actual.izq != null) {
                    _actual = _actual.izq;
                }
            }
        }

        public boolean haySiguiente() {            
            return _actual != null;
        }
    
        public T siguiente() {
            T valorActual = _actual.valor;
            
            if (_actual.der != null) {
                _actual = _actual.der;
                while (_actual.izq != null) {
                    _actual = _actual.izq;
                }
            } else {
                Nodo p = _actual.padre;
                while (p != null && _actual == p.der) {
                    _actual = p;
                    p = p.padre;
                }
                _actual = p;
            }
            
            return valorActual;
        }
    }

    public ABB_Iterador iterador() {
        return new ABB_Iterador();
    }

}
