import java.io.*;
import java.util.*;
import java.awt.Color;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
public class PrintPixels
{
	public static void main(String args[]) throws Exception
	{
		String filename = null;
		if(args.length==0)
		{
			System.out.print("Image: ");
			filename = new Scanner(System.in).nextLine();
		}
		else
			filename = args[0];
		PrintWriter pw = new PrintWriter("out.txt");
		pw.println(ppm(ImageIO.read(new File(filename))));
		pw.close();
		System.out.println("Saved to out.txt");
	}
	public static String ppm(BufferedImage img)
	{
		String ret="";
		for(int i=0;i<img.getHeight();i++)
			for(int j=0;j<img.getWidth();j++)
			{
				Color c = new Color(img.getRGB(i,j));
				ret+="["+i+", "+j+"] :: ("+c.getRed()+" "+c.getGreen()+" "+c.getBlue()+")\n";
			}
		return ret;
	}
}

