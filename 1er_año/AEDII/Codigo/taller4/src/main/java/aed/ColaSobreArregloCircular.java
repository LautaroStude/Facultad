package aed;

public class ColaSobreArregloCircular implements Cola {
    private int[] arreglo;
    private int head;
    private int tail;
    private int capacidad;
    private int cantidad;

    public ColaSobreArregloCircular(int i) {
        this.capacidad = i;
        this.arreglo = new int[capacidad];
        this.head = 0;
        this.tail = -1;
        this.cantidad = 0;
    }

    // Inserta en el final (tail)
    public void enqueue(int elem) {
        tail = (tail + 1) % capacidad;
        arreglo[tail] = elem;
        cantidad = cantidad + 1;
    }

    // Obtiene el elemento del frente (head)
    public int dequeue() {
        int elem = arreglo[head];
        head = (head + 1) % capacidad;
        cantidad = cantidad - 1;
        return elem;
    }

    // Obtiene el elemento del frente (head)
    public int front() {
        return arreglo[head];
    }

    // Obtiene el elemento del final (tail)
    public int rear() {
        return arreglo[tail];
    }

    public boolean isEmpty() {
        return cantidad == 0;
    }

    public boolean isFull() {
        return cantidad == capacidad;
    }
}
