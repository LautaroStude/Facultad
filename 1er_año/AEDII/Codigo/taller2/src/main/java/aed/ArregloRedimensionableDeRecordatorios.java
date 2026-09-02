package aed;

class ArregloRedimensionableDeRecordatorios {
    private Recordatorio[] recordatorios;
    private int cantidad;

    public ArregloRedimensionableDeRecordatorios() {
        this.recordatorios = new Recordatorio[1];
        this.cantidad = 0;
    }

    public int longitud() {
        return this.cantidad;
    }

    public void agregarAtras(Recordatorio i) {
        if (this.cantidad == this.recordatorios.length) {
            int nuevaCantidad = this.recordatorios.length + 1; 
            Recordatorio[] nuevoRecordatorios = new Recordatorio[nuevaCantidad];
            
            for (int j = 0; j < cantidad; j++) {
                nuevoRecordatorios[j] = recordatorios[j];
            }
            this.recordatorios = nuevoRecordatorios;
        }
        this.recordatorios[this.cantidad] = i;
        cantidad++;
    }


    public Recordatorio obtener(int i) {
        return this.recordatorios[i];
    }

    public void quitarAtras() {
        if (this.cantidad > 0) {
            Recordatorio[] newRecordatorio = new Recordatorio[this.cantidad - 1];
            for (int i = 0; i < cantidad - 1; i++) {
                newRecordatorio[i] = this.recordatorios[i];
            }
            this.recordatorios = newRecordatorio;
        }
        cantidad--;
    }

    public void modificarPosicion(int indice, Recordatorio valor) {
        if (indice < cantidad) {
            recordatorios[indice] = valor;
        }
    }

    public ArregloRedimensionableDeRecordatorios(ArregloRedimensionableDeRecordatorios vector) {
        this.cantidad = vector.cantidad;
        this.recordatorios = new Recordatorio[vector.recordatorios.length];
        for (int i = 0; i < this.cantidad; i++){
            this.recordatorios[i] = vector.recordatorios[i];
        }
    }

    public ArregloRedimensionableDeRecordatorios copiar() {

        return new ArregloRedimensionableDeRecordatorios(this);
    }
}
