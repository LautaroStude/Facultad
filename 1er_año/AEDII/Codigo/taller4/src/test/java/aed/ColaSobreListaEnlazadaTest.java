package aed;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ColaSobreListaEnlazadaTest {
    @Test
    public void testEncolar() {
        Cola queue = new ColaSobreListaEnlazada();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        assertTrue(queue.front()==1 && queue.rear()==3);
    }

    @Test
    public void testDesencolar() {
        Cola queue = new ColaSobreListaEnlazada();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        assertEquals(1, queue.dequeue());
        assertEquals(2, queue.dequeue());
        assertEquals(3, queue.dequeue());
        assertThrows(RuntimeException.class, () -> queue.dequeue());
    }

    @Test
    public void testColaVacia() {
        Cola queue = new ColaSobreListaEnlazada();
        assertTrue(queue.isEmpty());
        queue.enqueue(1);
        assertFalse(queue.isEmpty());
        queue.dequeue();
        assertTrue(queue.isEmpty());
    }

    @Test
    public void testColaLlena() {
        Cola queue = new ColaSobreListaEnlazada();
        assertFalse(queue.isFull());
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        assertFalse(queue.isFull());
        queue.enqueue(4);
        assertFalse(queue.isFull());
    }
}
