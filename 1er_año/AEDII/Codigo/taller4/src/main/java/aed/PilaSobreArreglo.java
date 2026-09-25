package aed;

public class PilaSobreArreglo implements Pila {
    private int[] arreglo;
    private int tope;
    private int capacidad;
    public PilaSobreArreglo(int capacity) {
        this.capacidad = capacity;
        this.arreglo = new int[capacity];
        this.tope = -1;
    }

    public void push(int elem) {
        tope = tope + 1;
        arreglo[tope] = elem;
    }

    public int pop() {
        int elemento = arreglo[tope];
        tope = tope - 1;
        return elemento;
    }

    public int top() {
        return arreglo[tope];
    }

    public boolean isEmpty() {
        return tope == -1;
    }

    public boolean isFull() {
        return tope == capacidad - 1;
    }
}
