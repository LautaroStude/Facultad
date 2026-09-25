package aed;

public class ColaSobreListaEnlazada implements Cola {
    private Node primero;
    private Node ultimo;
    public ColaSobreListaEnlazada() {
        this.primero = null;
        this.ultimo = null;
    }

    public void enqueue(int elem) {
        // creo nuevo nodo pero primero veo en como esta mi lista, me puede pasar que este vacia o que no
        Node nuevo = new Node(elem);
        if (isEmpty()) {
            primero = nuevo;
            ultimo = nuevo;
        } else {
            ultimo.next = nuevo;
            ultimo = nuevo;
        }
    }

    public int dequeue() {
        //obtengo el primero y despues lo elimino en caso que la lista este vacia primero y ultimo son null
        int elemento = primero.data;
        primero = primero.next;
        if (primero == null) {
            ultimo = null;
        }
        return elemento;
    }

    public int front() {
        return primero.data;
    }

    public int rear() {
        return ultimo.data;
    }

    public boolean isEmpty() {
        return primero == null;
    }

    public boolean isFull() {
        return false;
    }
}
