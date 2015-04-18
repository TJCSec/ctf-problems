import java.util.*;

public class EnterpriseLocalizationUtility {
    private Map<Integer, String> stringsMap;
    public EnterpriseLocalizationUtility() {
        stringsMap = new HashMap<>();
        stringsMap.put(EnterpriseConstants.WELCOME, "Welcome to the Enterprise Buzzword Factory");
        stringsMap.put(EnterpriseConstants.OPTIONS, "Here are your options: ");
    }
    public String getString(int id) {
        return stringsMap.get(id);
    }
}
