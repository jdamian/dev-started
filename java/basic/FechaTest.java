/**
 * testFecha
 */
public class FechaTest {

    public static void main(String[] args) {
        Fecha fechaPago = new Fecha();
        fechaPago.mes=12;

        int[] x = new int[10];
        Fecha[] fechas = new Fecha[5];

        fechas[0]=new Fecha();
        fechas[0].mes=12;
        fechas[0].dia=3;
        fechas[0].año= new Fecha.Año();
        fechas[0].año.añoNumero=2019;
        fechas[0].año.esBisiesto=false;
    }
}