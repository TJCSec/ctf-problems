import java.io.*;
import java.util.*;
import javax.imageio.ImageIO;

public class Problem
{
	public static void main(String args[]) throws Exception
	{
		System.out.print("Password: ");
		try {
			Scanner in = new Scanner(System.in);
			String password = in.nextLine();
			boolean check = check(password);
			if(check)
			{
				String flag = new Scanner(new File("../flag")).nextLine();
				System.out.println("Correct!");
				System.out.println("Flag: "+flag);
			}
			else throw new Exception();
		}
		catch(Exception e)
		{
			System.out.println("Wrong");
		}
		finally { System.exit(0); }
	}
	public static boolean check(String s) throws Exception
	{
		String c = Decoder.decode(ImageIO.read(new File("image.png"))).trim();
		if(s.equals(c))
			return true;
		return false;
	}
}
