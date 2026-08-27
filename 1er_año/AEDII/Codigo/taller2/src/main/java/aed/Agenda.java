package aed;

public class Agenda {
    private Fecha fecha;
    private ArregloRedimensionableDeRecordatorios recordatorios;
    public Agenda(Fecha fechaActual) {
        this.fecha = new Fecha(fechaActual);
        this.recordatorios = new ArregloRedimensionableDeRecordatorios();
    }

    public void agregarRecordatorio(Recordatorio recordatorio) {
        recordatorios.agregarAtras(recordatorio);
    }

    @Override
    public String toString() {
            String resultado = this.fecha.toString() + "\n=====\n";
            
            for (int i = 0; i < this.recordatorios.longitud(); i++) {
                Recordatorio r = this.recordatorios.obtener(i);
                if (r.fecha().equals(this.fecha)) {
                    resultado = resultado + r + "\n";
                }
            }
            return resultado;
        }

    public void incrementarDia() {
        this.fecha.incrementarDia();
    }

    public Fecha fechaActual() {
        return new Fecha(this.fecha);
    }

}
