/**
 * fecha
 */
public class Fecha {

    public Año año;
    public int mes;
    public int dia;

    /**
     * Año
     */
    public static class Año {
    
        public int añoNumero;
        public boolean esBisiesto;

        public static Año copy(Año año) {
            Año añoNuevo = new Año();
            añoNuevo.añoNumero = año.añoNumero;
            añoNuevo.esBisiesto = año.esBisiesto;
            return añoNuevo;
        }
    }
    public static Fecha copy(Fecha fecha) {
        Fecha nuevaFecha  = new Fecha();
        nuevaFecha.año = Año.copy(fecha.año); //clase organizadora
        nuevaFecha.mes = fecha.mes;
        nuevaFecha.dia = fecha.dia;
        return nuevaFecha;
    }

    public static int sigloPorOmision;
}
