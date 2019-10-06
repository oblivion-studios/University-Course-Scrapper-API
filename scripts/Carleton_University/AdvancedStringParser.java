import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;
import junit.framework.Test;

public class AdvancedStringParser {
	private static String semesterCode = "201920";
	private static String[] static_course = {"AFRI", "ASLA", "ANTH", "ALDS", "ARCC", "ARCH", "ARTH", "BIOC", "BIOL", "BUSI", "CDNS", "CHEM", "CHST", "CIVE", "CLCV", "CGSC", "CCDP", "COMS", "COMP", "CRCJ", "DIGH", "ERTH", "ECON", "ELEC", "ECOR", "ENGL", "ESLA", "ENVE", "ENSC", "ENST", "EURR", "FILM", "FOOD", "FREN",
            "GEOG", "GEOM", "GPOL", "GINS", "HLTH", "HIST", "HUMR", "HUMS", "BIT", "IPAF", "ITAL", "JAPA", "KORE", "LANG", "LAWS", "LING", "MATH", "MAAE", "MUSI", "NET", "NEUR", "PHIL", "PLT", "PHYS", "PSCI", "PSYC", "PAPM", "RELI", "SOWK", "SOCI", "SPAN", "STAT", "SYSC", "TSES", "WGST"};
	private static String[] static_status_options = {"Registration Closed", "Open", "Full, No Waitlist"};

	public static void removeNewLines(String File) {
		Scanner file;
		PrintWriter writer;
		try {
			file = new Scanner(new File(File + ".txt"));
			writer = new PrintWriter(File + "temp" + ".txt");
			while (file.hasNext()) {
				String line = file.nextLine();
				if (!line.isEmpty()) {
					if (line.startsWith(static_status_options[0]) || line.startsWith(static_status_options[1]) || line.startsWith(static_status_options[2])){
						writer.write("|-\n" + line.trim());
						writer.write("\n");
					} else {
						writer.write(line.trim());
						writer.write("\n");
					}
				}
			}
			file.close();
			writer.close();
		} catch (FileNotFoundException ex) {
			Logger.getLogger(Test.class.getName()).log(Level.SEVERE, null, ex);
		}
	}

	public static void main(String[] args) {
		System.out.println("---------------------------------------------------------");
		System.out.println("---------------------------------------------------------");
		System.out.println("|\t\tOblivion Studios (DevTOS)\t\t|");
		System.out.println("|\t\tversion 1.0.0 (API)\t\t\t|");
		System.out.println("|\t\tINTERNAL USE ONLY\t\t\t|");
		System.out.println("---------------------------------------------------------");
		System.out.println("---------------------------------------------------------");
		System.out.println("|" + "\t\tCourse Name\t" + "...." + "\tProgress\t" + "|");
		System.out.println("---------------------------------------------------------");
		System.out.println("---------------------------------------------------------");
		for (int i = 0; i<static_course.length; i++) {
			try {
				removeNewLines("Courses/" + static_course[i]);
				System.out.println("Parsing Course --> [" + static_course[i] + "]\t....\t" + "No Issues Found");
			} catch (Exception e) {
				System.out.println("Parsing Course --> [" + static_course[i] + "]\t....\t" + "Error Occured: " + e.getMessage().toString());
			}	
		}
		System.out.println("---------------------------------------------------------");
		System.out.println("---------------------------------------------------------");
		System.out.println("\nDONE PARSING! --> [" + semesterCode+ "]" + "\t....\t" + "100% Complete!\n");
		System.out.println("---------------------------------------------------------");
		System.out.println("---------------------------------------------------------");
		System.out.println("|" + "\t\tCourse Name\t" + "...." + "\tProgress\t" + "|");
		System.out.println("---------------------------------------------------------");
		System.out.println("---------------------------------------------------------");
	}
}