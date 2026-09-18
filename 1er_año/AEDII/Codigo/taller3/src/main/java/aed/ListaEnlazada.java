package aed;

public class ListaEnlazada<T> {
    private Nodo primero;
    private Nodo ultimo;
    private int tamaño;

    private class Nodo {
        T valor;
        Nodo siguiente;
        Nodo anterior;

        Nodo(T v) {this.valor = v;
                    this.siguiente = null;
                    this.anterior = null;
        }       
    }

    public ListaEnlazada() {
        this.primero = null;
        this.ultimo = null;
        this.tamaño = 0;
    }

    public int longitud() {
        return this.tamaño; 
    }

    public void agregarAdelante(T elem) {
        Nodo nuevo = new Nodo(elem);
        //si lo inicio vacio tiene que ser el primero y a la vez el ultimo el que agregue
        if (this.primero == null) {
            this.primero = nuevo;
            this.ultimo = nuevo;
        } else {
            nuevo.siguiente = this.primero;
            this.primero.anterior = nuevo;
            this.primero = nuevo;
        }
        this.tamaño = this.tamaño + 1;
    }

    public void agregarAtras(T elem) {
        Nodo nuevo = new Nodo(elem);
        if (this.ultimo == null) {
            this.primero = nuevo;
            this.ultimo = nuevo;
        } else {
            nuevo.anterior = this.ultimo;
            this.ultimo.siguiente = nuevo;
            this.ultimo = nuevo;
        }
        this.tamaño = this.tamaño + 1;
    }

    public T obtener(int i) {
        //mi actual en realidad es el primer nodo de la lista, voy actualizando
        Nodo actual = this.primero;
        for (int j = 0; j < i; j++) {
            actual = actual.siguiente;
        }
        return actual.valor;
    }

    public void eliminar(int i) {
        Nodo actual = this.primero;
        //freno en el j = i
        for (int j = 0; j < i; j++) {
            actual = actual.siguiente;
        }
        if (actual.anterior != null) {
            //si tengo a alguien atras le tengo que decir que deje de apuntar a mi actual, que apunte al siguiente, si no tengo a nadie soy el primero
            actual.anterior.siguiente = actual.siguiente;
        } else {
            this.primero = actual.siguiente;
        }

        if (actual.siguiente != null) {
            //lo mismo pero con siguiente hago
            actual.siguiente.anterior = actual.anterior;
        } else {
            this.ultimo = actual.anterior;
        }
        this.tamaño = this.tamaño - 1;
    }

    public void modificarPosicion(int indice, T elem) {
        Nodo actual = this.primero;
        for (int j = 0; j < indice; j++) {
            actual = actual.siguiente;
            }
        actual.valor = elem;
    }

    public ListaEnlazada(ListaEnlazada<T> lista) {
        this.primero = null;
        this.ultimo = null;
        this.tamaño = 0;
        
        Nodo actual = lista.primero;
        while (actual != null) {
            this.agregarAtras(actual.valor);
            actual = actual.siguiente;
        }
    }
    
    @Override
    public String toString() {
        String resultado = "[";
        Nodo actual = this.primero;
        
        while (actual != null) {
            resultado += actual.valor;
            
            if (actual.siguiente != null) {
                resultado += ", ";
            }
            actual = actual.siguiente;
        }
        
        resultado += "]";
        return resultado;
    }

    public class ListaIterador{
        private Nodo actual = primero;

        public boolean haySiguiente() {
            //el dedito empezaria antes del primer nodo seria algo como "| (1er nodo) (2do nodo) ..." donde | es el dedo, entonces me queda que el siguiente es mi primer nodo
	        return this.actual != null;
        }
        
        public boolean hayAnterior() {
            //veo si es el ultimo elemento, tambien veo que no este vacia la lista
	        if (this.actual == null) {
                return ultimo != null;
            }
            return this.actual.anterior != null;
        }

        public T siguiente() {
	        T valorActual = this.actual.valor;
            this.actual = this.actual.siguiente;
            return valorActual;
        }
        
        public T anterior() {
	        if (this.actual == null) {
                this.actual = ultimo; 
            } else {
                this.actual = this.actual.anterior;
            }
            return this.actual.valor;
        }
    }

    public ListaIterador iterador() {
	    return new ListaIterador();
    }

}
