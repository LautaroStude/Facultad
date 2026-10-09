package aed;
import java.util.ArrayList;

public class SistemaPedidos {
    private ListaEnlazada<Pedido> pedidosPorLlegada;
    private ArrayList<Handle<Pedido>> pedidosPorId;

    public SistemaPedidos(){
         this.pedidosPorLlegada = new ListaEnlazada<>();
         this.pedidosPorId = new ArrayList<>();
    }

    public void agregarPedido(Pedido pedido){
        //tiene complejidad O(n) porque se recorre la lista de pedidosPorId para encontrar la posición donde insertar el nuevo pedido.
        Handle<Pedido> nuevohandle = pedidosPorLlegada.agregarAtras(pedido);
        int i = 0;
        while (i < pedidosPorId.size() && pedidosPorId.get(i).compareTo(nuevohandle) > 0){ //el compareTo devuelve un int asi que si es mayor a 0 veo que el nuevo pedido es mayor al que estoy comparando y sigo buscando hasta que sea menor
            i++;
        }
        //preguntar si add y remove tienen complejidad 0(n) o 0(1)
        pedidosPorId.add(i, nuevohandle);
    }

    private void agregarOrdenado(Handle<Pedido> p){
        throw new UnsupportedOperationException("No implementado aún");
    }

    public Pedido proximoPedidoPorId(){
        // la complejidad es O(1) nunca recorro una lista
        Handle<Pedido> handleIdmaschico = pedidosPorId.remove(pedidosPorId.size()-1);
        Pedido pedidoIdmaschico = handleIdmaschico.valor();
        handleIdmaschico.eliminar();
        return pedidoIdmaschico;
    }

    public Pedido proximoPedidoPorLlegada(){
        // la complejidad es O(n) porque al recorrer una lista a lo sumo recorro toda la lista que tiene n elementos
        Pedido primerPedido = pedidosPorLlegada.obtenerPrimero();
        int i = 0;
        boolean encontre = false;
        while (i < pedidosPorId.size() && !encontre){
            Handle<Pedido> handleActual = pedidosPorId.get(i);
            if (handleActual.valor().id() == primerPedido.id()){
                pedidosPorId.remove(i);
                handleActual.eliminar();
                encontre = true;
            }
            i++;
        }
        return primerPedido;
    }

    public Pedido pedidoMenorId(){
        //con el get queda O(1)
        return pedidosPorId.get(pedidosPorId.size()-1).valor();
    }

    public String obtenerPedidosEnOrdenDeLlegada(){
        //la complejidad es O(n) porque toString recorre la lista asi que tiene 0(n) de complejidad
        return pedidosPorLlegada.toString();
    }
    

    public String obtenerPedidosOrdenadosPorId(){
        // aca recorro asi que tambien es O(n) en realidad theta(n) porque siempre recorro toda la lista de pedidosPorId
        String res = "[";
        for (int i = pedidosPorId.size() - 1; i >= 0; i--){
            res += pedidosPorId.get(i).valor().toString();
            if (i > 0){
                res += ", ";
            }
        }
        res += "]";
        return res;
    }
}
