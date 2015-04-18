import java.util.*;
import java.io.*;

public class EnterpriseOptionMenuSystem {
    public EnterpriseOptionMenuSystem() {}

    public void displayOptions() {
        System.out.println("1. Show all buzzwords");
        System.out.println("2. Create a buzzword");
        System.out.println("3. Add a buzzword");
    }

    public void invokeOption(LinkedList<Object> buzzwords, int option) {
        if(option == 1) {
            System.out.println(buzzwords);
        }
        if(option == 2) {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String buzz = null;
            try {
                System.out.print("Your buzzword: ");
                buzz = br.readLine();
            } catch (IOException i) {
                System.exit(1);
            }
            EnterpriseBuzzword b = new EnterpriseBuzzword(buzz);
            System.out.println("Here's your buzzword: ");
            System.out.println(b.serialize());
        }
        if(option == 3) {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String buzz = null;
            try {
                System.out.print("Your serialized buzzword: ");
                buzz = br.readLine();
            } catch (IOException i) {
                System.exit(1);
            }
            try {
                buzzwords.add(EnterpriseDeserializer.deserialize(buzz));
                System.out.println("Buzzword added!");
            } catch(Exception e) {
                System.out.println("Buzzword not added :(");
            }
        }
    }
}
