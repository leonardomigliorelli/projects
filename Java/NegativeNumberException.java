public class NegativeNumberException extends Exception {
    public NegativeNumberException(String testo, double x) {
        super(testo + " negativo/a [value: " + x + "]");
    }

    public NegativeNumberException(String testo, int x) {
        super(testo + " negativo/a [value: " + x + "]");
    }

    public NegativeNumberException(String testo) {
        super(testo + " negativo/a");
    }
}
