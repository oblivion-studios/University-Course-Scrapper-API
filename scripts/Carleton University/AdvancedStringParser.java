import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;
import junit.framework.Test;

public class AdvancedStringParser {
	private static String[] static_course = { "AERO", "AFRI", "ASLA", "ANTH", "ALDS", "ARAB", "ARCS", 
			"ARCC", "ARCN", "ARCH", "ARCU", "ARTH", "BIOC", "BIOL",
			"BUSI", "CDNS", "CHEM", "CHST", "CHIN", "CIVE", "CLCV",
			"COOP", "CGSC", "CCDP", "COMS", "COMP", "CRCJ", "DIGH",
			"DBST", "ESPW", "ERTH", "ECON", "ELEC", "ECOR", "ENGL",
			"ESLA", "ENVE", "ENSC", "ENST", "EURR", "FILM", "FYSM",
			"FOOD", "FREN", "FINS", "GEOG", "GEOM", "GERM", "GPOL", "GINS",
			"GREK", "HLTH", "HIST", "HUMR", "HUMS", "INDG", "IDES", "IRM",
			"BIT", "ITEC", "INSC", "IMD", "IPAF", "ISCI", "INAF", "ITAL",
			"JAPA", "JOUR", "KORE", "LANG", "LATN", "LACS", "LAWS", "LING",
			"MATH", "MECH", "MAAE", "MPAD", "MEMS", "MGDS", "MUSI", "NSCI",
			"NET", "NEUR", "PHIL", "PLT", "PHYS", "PSCI", "PORT", "PSYC",
			"PADM", "PAPM", "RELI", "RUSS", "SXST", "SOWK", "SOCI", "SPAN",
			"STAT", "SREE", "SYSC", "TSES", "WGST"};

	private static String[] static_status_options = {"Registration Closed", "Open", "Full, No Waitlist"};

	public static void removeNewLines(String File) {
		Scanner file;
		PrintWriter writer;
		int i = 0;
		try {
			file = new Scanner(new File(File + ".txt"));
			writer = new PrintWriter(File + "temp" + ".txt");
			while (file.hasNext()) {
				String line = file.nextLine();
				i++;
				if (!line.isEmpty() && !line.startsWith("�") || line.startsWith(" ")) {
					if (i == 12 && (line.startsWith(static_status_options[0]) || line.startsWith(static_status_options[1]) || line.startsWith(static_status_options[2]))){
						writer.write("|-\n" + line.trim());
						writer.write("\n");
						i = 0;
					} 
					i++;
					else if (i>12 && ((line.startsWith(static_status_options[0]) || line.startsWith(static_status_options[1]) || line.startsWith(static_status_options[2])))) {
						writer.write("|-\n" + line.trim());
						writer.write("\n");
						i = 0;
					} else {
						writer.write(line.trim());
						writer.write("\n");
						i++;
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
		// Remove New Lines in ALL files
		for (int i = 0; i<static_course.length; i++) {
			removeNewLines("Courses/" + static_course[i]);
			System.out.println("Parsing ... " + i/static_course.length + "% Completed")	
		}
		System.out.println("DONE PARSING!");
	}
}