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
        String resultado = fecha.toString() + "\n" + "=====" + "\n"; 
        for (int i=0;i < recordatorios.longitud(); i++) {
            Recordatorio recodatorioAgenda = recordatorios.obtener(i);
            if (recodatorioAgenda.fecha().equals(fechaActual()) ){
                resultado += recodatorioAgenda.toString();
                resultado += "\n";
            }
        }
        return resultado;
    }

    public void incrementarDia() {
        this.fecha.incrementarDia();
    }

    public Fecha fechaActual() {
        
        return new Fecha(fecha);
    }

}
