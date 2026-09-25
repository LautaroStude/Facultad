package aed;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class PilaSobreArregloTest {
    @Test
    public void testApilar() {
        Pila stack = new PilaSobreArreglo(3);
        stack.push(1);
        stack.push(2);
        stack.push(3);
        assertThrows(RuntimeException.class, () -> stack.push(4));
    }

    @Test
    public void testDesapilar() {
        Pila stack = new PilaSobreArreglo(3);
        stack.push(1);
        stack.push(2);
        stack.push(3);
        assertEquals(3, stack.pop());
        assertEquals(2, stack.pop());
        assertEquals(1, stack.pop());
        assertThrows(RuntimeException.class, () -> stack.pop());
    }

    @Test
    public void testPilaVacia() {
        Pila stack = new PilaSobreArreglo(3);
        assertTrue(stack.isEmpty());
        stack.push(1);
        assertFalse(stack.isEmpty());
        stack.pop();
        assertTrue(stack.isEmpty());
    }

    @Test
    public void testPilaLlena() {
        Pila stack = new PilaSobreArreglo(3);
        assertFalse(stack.isFull());
        stack.push(1);
        stack.push(2);
        stack.push(3);
        assertTrue(stack.isFull());
        stack.pop();
        assertFalse(stack.isFull());
    }
}
