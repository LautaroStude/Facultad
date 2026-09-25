package aed;

public class PilaSobreListaEnlazada implements Pila {
    private Node primero;
    public PilaSobreListaEnlazada() {
        this.primero = null;
    }

    public void push(int elem) {
        Node nuevo = new Node(elem);
        nuevo.next = primero;
        primero = nuevo;
    }

    public int pop() {
        int elemento = primero.data;
        primero = primero.next;
        return elemento;
    }

    public int top() {
        return primero.data;
    }

    public boolean isEmpty() {
        return primero == null;
    }

    public boolean isFull() {
        return false;
    }
}
