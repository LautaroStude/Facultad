package aed;

class ArregloRedimensionableDeRecordatorios {
    private Recordatorio[] recordatorios;
    private int cantidad;
    public ArregloRedimensionableDeRecordatorios() {
        this.recordatorios = new Recordatorio[1];
        this.cantidad = 0;
    }

    public int longitud() {
        return cantidad;
    }

    public void agregarAtras(Recordatorio i) {
        if (cantidad == recordatorios.length){
            int nuevaCantidad = recordatorios.length * 2;
            Recordatorio[] nuevoRecordatorios = new Recordatorio[nuevaCantidad];
            for (int j = 0; j < cantidad; j++){
                nuevoRecordatorios[j] = recordatorios[j];
            }
            recordatorios = nuevoRecordatorios;
        }
        recordatorios[cantidad] = i;
        cantidad++;
    }

    public Recordatorio obtener(int i) {
        return this.recordatorios[i];
    }

    public void quitarAtras() {
        if (cantidad > 0){
            recordatorios[cantidad - 1] = null;
            cantidad--;
        }
    }

    public void modificarPosicion(int indice, Recordatorio valor) {
        if (indice < cantidad){
            recordatorios[indice] = valor;
        }
    }

    public ArregloRedimensionableDeRecordatorios(ArregloRedimensionableDeRecordatorios vector) {
        this.cantidad = vector.cantidad;
        this.recordatorios = new Recordatorio[vector.recordatorios.length];
        for (int j = 0; j < cantidad; j++) {
            this.recordatorios[j] = vector.recordatorios[j];
        }
    }

    public ArregloRedimensionableDeRecordatorios copiar() {
        return new ArregloRedimensionableDeRecordatorios(this);
    }
}
