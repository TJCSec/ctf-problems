import java.util.*;
import java.io.*;

public class EnterpriseBuzzwordFactoryClient {
    private static EnterpriseLocalizationUtility localizer;
    private static EnterpriseOptionMenuSystem menu;
    private static LinkedList<Object> buzzwords;
    static {
        localizer = new EnterpriseLocalizationUtility();
        menu = new EnterpriseOptionMenuSystem();
        buzzwords = new LinkedList<>();
    }
    public static void main(String[] args) throws InterruptedException {
        System.out.println(localizer.getString(EnterpriseConstants.WELCOME));
        Thread.sleep(500);
        System.out.println(localizer.getString(EnterpriseConstants.OPTIONS));
        Thread.sleep(500);
        while(true) {
            menu.displayOptions();
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int choice = -1;
            try {
                choice = Integer.parseInt(br.readLine());
            } catch (IOException i) {
                System.exit(1);
            }
            menu.invokeOption(buzzwords, choice);
        }
    }
}
