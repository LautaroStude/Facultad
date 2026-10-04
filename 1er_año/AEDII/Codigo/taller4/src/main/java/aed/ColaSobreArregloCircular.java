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
        //si me pase de la capacidad vuelvo al primero
        if (cantidad == capacidad) {
            throw new RuntimeException();
        }
        tail = tail + 1;
        if (tail == capacidad) {
            tail = 0;
        }
        arreglo[tail] = elem;
        cantidad = cantidad + 1;
    }

    // Obtiene el elemento del frente (head)
    public int dequeue() {
        //hago lo mismo que el anterior veo si el puntero se pasa de la capacidad vuelvo al primero
        if (cantidad == 0) {
            throw new RuntimeException();
        }
        int elem = arreglo[head];
        head = head + 1;
        if (head == capacidad) {
            head = 0;
        }
        cantidad = cantidad - 1;
        return elem;
    }

    // Obtiene el elemento del frente (head)
    public int front() {
        if (cantidad == 0) {
            throw new RuntimeException();
        }
        return arreglo[head];
    }

    // Obtiene el elemento del final (tail)
    public int rear() {
        if (cantidad == 0) {
            throw new RuntimeException();
        }
        return arreglo[tail];
    }

    public boolean isEmpty() {
        return cantidad == 0;
    }

    public boolean isFull() {
        return cantidad == capacidad;
    }
}
