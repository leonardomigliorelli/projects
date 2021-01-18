import java.util.Scanner;

abstract public class Input {
    /**
     * questa  classe ha diversi tool per semplificare l'input e gestire dei valori
     */

    public static byte getByte(String x) {
        Scanner s = new Scanner(System.in);
        System.out.print(x);

        return s.nextByte();
    }

    public static short getShort(String x) {
        Scanner s = new Scanner(System.in);
        System.out.print(x);

        return s.nextShort();
    }

    public static int getInt(String x) {
        Scanner s = new Scanner(System.in);
        System.out.print(x);

        return s.nextInt();
    }

    public static long getLong(String x) {
        Scanner s = new Scanner(System.in);
        System.out.print(x);

        return s.nextLong();
    }

    public static String getString(String x) {
        Scanner s = new Scanner(System.in);
        System.out.print(x);

        return s.nextLine();
    }

    public static float getFloat(String x) {
        Scanner s = new Scanner(System.in);
        System.out.print(x);

        return s.nextFloat();
    }

    public static double getDouble(String x) {
        Scanner s = new Scanner(System.in);
        System.out.print(x);

        return s.nextDouble();
    }

    public static double round(double x, int precision) {
        double p = 1;

        for (int i = 0; i < precision; i++)
            p *= 10;

        return (int) (x * (int) p) / p;
    }
}
