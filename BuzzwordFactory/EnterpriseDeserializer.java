import java.lang.reflect.*;

public class EnterpriseDeserializer {
    public static Object deserialize(String s) throws Exception {
        String[] ss = s.split(":");
        String klass = ss[0];
        String arg = ss[1];
        Class<?> klassClass = Class.forName(klass);
        Method m = klassClass.getMethod("deserialize", String.class);
        return m.invoke(null, arg);
    }
}
