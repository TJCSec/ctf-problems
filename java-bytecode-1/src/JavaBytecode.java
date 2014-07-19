import java.util.Scanner;

public class JavaBytecode {

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

	private static void e(String b) {
		int i = 0;
		b += i;
	}

	private static boolean c(String b) {
		for (int i = 0; i < 10000000; ++i) {
			e(b);
		}
		for (int i = 0; i < b.length(); ++i) {
			char c = b.charAt(i);
			if (c < '0' || c > '9') {
				return false;
			}
		}
		int d = 0;
		for (int i = 0; i < b.length() - 1; i += 2) {
			d += b.charAt(i) - '0';
		}
		for (int i = 1; i < b.length() - 1; i += 2) {
			d += (b.charAt(i) - '0') * 3;
		}
		int e = 10 - d % 10;
		int f = 0;
		for (int i = 0; i < 5; ++i) {
			f += b.charAt(i) - '0';
		}
		int g = 1;
		for (int i = 1; i < 5; ++i) {
			g *= b.charAt(i) - '0';
		}
		int h = b.charAt(1) - '0';
		int l = b.charAt(2) - '0';
		int m = b.charAt(3) - '0';
		int n = b.charAt(4) - '0';
		if (!b.substring(5, 11).equals("914323"))
			return false;
		if (Math.abs(h + l - m) != 1 || Math.abs(h + l - n) != 1)
			return false;
		if (!b.contains("0"))
			return false;
		if (b.charAt(b.length() - 1) - '0' != e)
			return false;
		if (f != 21)
			return false;
		if (g != 480)
			return false;
		return e == 9;
	}

}
