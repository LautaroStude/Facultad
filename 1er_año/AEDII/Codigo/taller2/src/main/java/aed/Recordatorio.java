package aed;

public class Recordatorio {
    private String mensaje;
    private Fecha fecha;
    private Horario horario;

    public Recordatorio(String mensaje, Fecha fecha, Horario horario) {
        this.mensaje = mensaje;
        this.fecha = new Fecha(fecha.dia(), fecha.mes());
        this.horario = horario;
    }

    public Horario horario() {
        return this.horario;
    }

    public Fecha fecha() {
        return new Fecha(this.fecha.dia(), this.fecha.mes());
    }

    public String mensaje() {
        return this.mensaje;
    }

    @Override
    public String toString() {
        return mensaje + " @ " + fecha + " " + horario;
    }

    @Override
        public boolean equals(Object otro) {
            if (otro == null || otro.getClass() != this.getClass()) {
                return false;
            }
            Recordatorio otroRecordatorio = (Recordatorio) otro;

            boolean mensajesIguales = true;
            if (this.mensaje.length() != otroRecordatorio.mensaje.length()) {
                mensajesIguales = false;
            } else {
                for (int i = 0; i < this.mensaje.length() && mensajesIguales; i++) {
                    if (this.mensaje.charAt(i) != otroRecordatorio.mensaje.charAt(i)) {
                        mensajesIguales = false;
                    }
                }
            }

            return mensajesIguales && otroRecordatorio.horario.equals(this.horario) && otroRecordatorio.fecha.equals(this.fecha);
        }
    }