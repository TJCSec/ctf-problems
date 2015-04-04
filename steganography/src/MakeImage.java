import java.util.*;
import java.io.*;
import java.awt.Color;
import java.awt.image.BufferedImage; 
import javax.imageio.ImageIO;

public class MakeImage
{
	public static void main(String args[]) throws Exception
	{
		BufferedImage img = make(new Scanner(new File("../key")).nextLine());
		ImageIO.write(img,"png",new File("image.png"));
	}
	public static BufferedImage make(String s)
	{
		char[] bytes = s.toCharArray();
		int[] bits=new int[64];
		for (int c=0;c<(bytes.length);c++){
			for (int d=7;d>=0;d--){
				bits[(c*8)+d]=(bytes[c]&1);
				bytes[c]>>>=1;
			}
		}
		BufferedImage ret = new BufferedImage(8,8,BufferedImage.TYPE_INT_RGB);
		for(int i=0;i<8;i++)
			for(int j=0;j<8;j++)
				ret.setRGB(i,j,new Color((int)(Math.random()*256/2)*2,(int)(Math.random()*256/2)*2,((int)(Math.random()*256/2)*2)%256+bits[8*i+j]).getRGB());
		return ret;
	}
}
