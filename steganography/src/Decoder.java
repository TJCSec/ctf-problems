import java.util.*;
import java.io.*;
import java.awt.Color;
import java.awt.image.BufferedImage; 
import javax.imageio.ImageIO;

public class Decoder
{
	public static String decode(BufferedImage img)
	{
		//malformity check
		if(img.getHeight()*img.getWidth()%8!=0)
			return null;
		int[] bits = new int[64];
		for(int i=0;i<8;i++)
			for(int j=0;j<8;j++)
				bits[8*i+j] = (new Color(img.getRGB(i,j)).getBlue()&1);
		char[] bytes=new char[8];
		for (int c=0;c<8;c++){
			bytes[c]=0;
			for(int i=0;i<8;i++){
				bytes[c]<<=1;
				bytes[c]+=(char)bits[c*8+i];
			}
		}
		String ret="";
		for(char a : bytes)
			ret+=a;
		return ret;
	}
}
