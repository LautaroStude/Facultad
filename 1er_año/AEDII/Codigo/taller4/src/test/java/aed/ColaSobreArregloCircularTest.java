package aed;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ColaSobreArregloCircularTest {
    @Test
    public void testEncolar() {
        Cola queue = new ColaSobreArregloCircular(3);
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        assertThrows(RuntimeException.class, () -> queue.enqueue(4));
    }

    @Test
    public void testDesencolar() {
        Cola queue = new ColaSobreArregloCircular(3);
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
        Cola queue = new ColaSobreArregloCircular(3);
        assertTrue(queue.isEmpty());
        queue.enqueue(1);
        assertFalse(queue.isEmpty());
        queue.dequeue();
        assertTrue(queue.isEmpty());
    }

    @Test
    public void testColaLlena() {
        Cola queue = new ColaSobreArregloCircular(3);
        assertFalse(queue.isFull());
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        assertTrue(queue.isFull());
        queue.dequeue();
        assertFalse(queue.isFull());
    }
}
