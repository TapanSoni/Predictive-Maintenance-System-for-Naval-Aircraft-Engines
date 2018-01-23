package v1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class CsvGenerator {
	
	private String inputFilePath;		//File path of data to be converted into a CSV
	private String outCsvPath = "C:\\Users\\connorlof\\java\\Data_Converter\\Files\\completeDataCsv.csv";	//File path to save CSV to
	
	private ArrayList<String> dataList = new ArrayList();
	
	public CsvGenerator(String inputFile){
		
		this.inputFilePath = inputFile;
		
		//TODO in later sprint, detect input file type
		//For now using original white space delimited file type
		
		//Read the data in
		readDataFile();
		
		//Test the size has the proper number of rows as original file
		//System.out.println(dataList.size());
		
		//Convert List of rows to a CSV file
		createCsvFile();
		
	}
	
	//Method reads a data file by each line and converts to comma delimited. Stores in ArrayList
	private void readDataFile(){
		
		try(BufferedReader br = new BufferedReader(new FileReader(this.inputFilePath))) {
	    	
	        String line = "";
	        while ((line = br.readLine()) != null) {
	        	
	        	//Replace any commas in the data
	        	line = line.replace(",", "");
	        	
	        	//Replace any whitespace with a comma to make comma delimted line
	        	line = line.replaceAll("\\s{1,}", ",");
	        	
	        	//Remove the first comma add (in front of line)
	        	line = line.replaceFirst(",", "");
	        	
	        	//Print line for testing
	        	//System.out.println(line);
	        	
	        	//Add line to the List
	        	dataList.add(line);
	        }
	    } catch (IOException e) {
	    	System.err.println("Error reading in data file.");
	        e.printStackTrace();
	    }
		
	}
	
	//Write the list of rows to a CSV file
	private void createCsvFile(){

		try {
			
			FileWriter writer = new FileWriter(this.outCsvPath);
			
			for(int i = 0; i < dataList.size(); i++) {
				writer.write(dataList.get(i) + "\n");
			}

		    writer.close();
		    
		} catch (IOException e) {
			System.err.println("Error reading list to a csv file.");
			e.printStackTrace();
		}
		
	}

	//Getters
	public String getOutCsvPath() {
		return outCsvPath;
	}


	
	
}
