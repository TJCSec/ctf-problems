import java.util.Scanner;

public class JavaBytecode2 {

	private static final char[] arr = { 'r', 'e', 'a', 'd', 'c', 'l', 'a', 's',
			's', 'y' };

	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		System.out.print("Enter passcode: ");
		String b = a.nextLine();
		if (c(b)) {
			System.out.println("Success!");
		} else {
			System.out.println("Failed");
		}
	}

	private static boolean c(String b) {
		for (int i = 0; i < b.length(); ++i) {
			if (i < arr.length && arr[i] == b.charAt(i)) {
				continue;
			}
			return false;
		}
		return true;
	}
}
