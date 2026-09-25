package aed;

public interface Cola {
    // Métodos para colas
    void enqueue(int elem);
    int dequeue();
    int front();
    int rear();
    boolean isEmpty();
    boolean isFull();
}
