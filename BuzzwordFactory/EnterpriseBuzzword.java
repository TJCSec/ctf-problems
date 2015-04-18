public class EnterpriseBuzzword {
    private String buzz;
    public EnterpriseBuzzword(String buzzz) {
        buzz = buzzz;
    }
    public String serialize() {
        return "EnterpriseBuzzword:" + buzz;
    }
    public static EnterpriseBuzzword deserialize(String arg) {
        return new EnterpriseBuzzword(arg);
    }
    public String toString() {
        return buzz;
    }
}
