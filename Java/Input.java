import java.util.Scanner;

abstract public class Input {
    /**
     * questa  classe ci permette di usare il Input.get* come in java--
     */

    static byte getByte(String x) {
        Scanner s = new Scanner(System.in);
        System.out.println(x);

        return s.nextByte();
    }

    static short getShort(String x) {
        Scanner s = new Scanner(System.in);
        System.out.println(x);

        return s.nextShort();
    }

    static int getInt(String x) {
        Scanner s = new Scanner(System.in);
        System.out.println(x);

        return s.nextInt();
    }

    static long getLong(String x) {
        Scanner s = new Scanner(System.in);
        System.out.println(x);

        return s.nextLong();
    }

    static String getString(String x) {
        Scanner s = new Scanner(System.in);
        System.out.println(x);

        return s.nextLine();
    }

    static float getFloat(String x) {
        Scanner s = new Scanner(System.in);
        System.out.println(x);

        return s.nextFloat();
    }

    static double getDouble(String x) {
        Scanner s = new Scanner(System.in);
        System.out.println(x);

        return s.nextDouble();
    }

    static double round(double x) {
        return (int) (x * 100) / 100.0;
    }
}
