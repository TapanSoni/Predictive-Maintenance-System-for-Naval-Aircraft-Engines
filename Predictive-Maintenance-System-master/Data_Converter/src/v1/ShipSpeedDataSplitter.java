package v1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class ShipSpeedDataSplitter {
	
	private String outputFolderPath = "C:\\Users\\connorlof\\java\\Data_Converter\\Files\\Speed CSVs\\";
	private String inputCsvPath;
	private int numberOfShipSpeeds;
	
	private ArrayList<String> rowList = new ArrayList();
	
	public ShipSpeedDataSplitter(String inputCsv, int numberOfSpeeds){
		
		this.inputCsvPath = inputCsv;
		this.numberOfShipSpeeds = numberOfSpeeds;
		
		//Read the data file into a List
		readDataFile();
		
		//Generate each separate ship speed csv
		for(int i = 1; i <= this.numberOfShipSpeeds; i++){
			
			generateShipSpeedCsv(i);
			
		}
		
	}
	
	private void readDataFile(){
		
		try(BufferedReader br = new BufferedReader(new FileReader(this.inputCsvPath))) {
	    	
	        String line = "";
	        while ((line = br.readLine()) != null) {
	        	
	        	//Add line to the List
	        	rowList.add(line);
	        }
	    } catch (IOException e) {
	    	System.err.println("Error reading in data file.");
	        e.printStackTrace();
	    }
		
	}
	
	private void generateShipSpeedCsv(int speedIndex){
		
		ArrayList<String> newRowList = new ArrayList();
		
		//Create list of data
		for (int i = speedIndex; i < this.rowList.size(); i = i + this.numberOfShipSpeeds) {
			
			newRowList.add(this.rowList.get(i));
			
	    }
		
		//Create output csv file
		try {
			
			FileWriter writer = new FileWriter(this.outputFolderPath + "dataSpeed" + speedIndex + ".csv");
			
			for(int i = 0; i < newRowList.size(); i++) {
				writer.write(newRowList.get(i) + "\n");
			}

		    writer.close();
		    
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}

}
