import java.nio.file.*;
import java.io.*;

public class EnterpriseFlagPrinter {
    public static EnterpriseFlagPrinter deserialize(String arg) throws IOException {
        if(arg != "i can read the source code") {
            System.out.println(new String(Files.readAllBytes(Paths.get("flag.txt"))));
        }
        return new EnterpriseFlagPrinter();
    }
}
