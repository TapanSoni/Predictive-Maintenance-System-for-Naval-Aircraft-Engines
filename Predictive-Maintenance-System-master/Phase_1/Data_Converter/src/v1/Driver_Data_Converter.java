package v1;

public class Driver_Data_Converter {

	public static void main(String[] args) {
		
		String dataFile = "C:\\Users\\connorlof\\Documents\\School\\Fall 2017\\Software Eng\\UCI CBM Dataset\\UCI CBM Dataset\\data.txt";
		
		//Generate CSV file from data file
		CsvGenerator csvGenerator = new CsvGenerator(dataFile);
		
		//Split output CSV file into separate ship speed CSV files
		int numSpeeds = 9;		//TODO generate number of speeds dynamically
		ShipSpeedDataSplitter shipSpeedSplitter = new ShipSpeedDataSplitter(csvGenerator.getOutCsvPath(), numSpeeds);
		
		

	}

}
