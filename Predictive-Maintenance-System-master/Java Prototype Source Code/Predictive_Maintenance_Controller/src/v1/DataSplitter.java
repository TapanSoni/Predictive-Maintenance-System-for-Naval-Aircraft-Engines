package v1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.Arrays;

public class DataSplitter {
	
	//Variables to hold the file paths
	private String outputFolderPath;
	private String inputCsvPath;
	
	//Variable to hold the discrete column (0 if no column to split by)
	private int discreteColumn;
	
	//ArrayList to hold each row of data in input CSV
	private ArrayList<String> rowList = new ArrayList();
	
	//Array to hold values in the discrete column
	private String[] columnValues;
	
	//Array to hold unique values in discrete column
	private String[] uniqueValues;
	
	
	//Constructor takes a String for the input CSV path and an int for the column to split
	public DataSplitter(String inputCsv, int columnToSplit){
		
		//Get outputFolerPath
		this.outputFolderPath = FilepathHandler.splitFileDir;
		
		//Clear save directory 
		clearSaveDirectory();
		
		//Set the inputCsvPath to passed in String
		this.inputCsvPath = inputCsv;
		
		//Split the data if column to split is not equal to 0
		if(columnToSplit > 0){

			this.discreteColumn = columnToSplit - 1;
			
			//Read the data file into a List
			readDataFile();
			
			//Determine number of unique values in discrete column
			int numDiscrete = determineNumDiscrete();
			
			//Generate a separate CSV for each discrete value
			for(int i = 1; i <= numDiscrete; i++){
				
				generateSplitCsv(i);
				
			}
			
		}else{
			
			//Copy full data set to Split_By_Discrete Folder
			copyFullData();
			
		}

	}
	
	//Method reads the CSV file and saves each row into rowList
	private void readDataFile(){
		
		try(BufferedReader br = new BufferedReader(new FileReader(this.inputCsvPath))) {
	    	
	        String line = "";
	        while ((line = br.readLine()) != null) {
	        	
	        	//Add line to the List
	        	rowList.add(line);
	        }
	        
	        br.close();
	        
	    } catch (IOException e) {
	    	System.err.println("Error reading in data file.");
	        e.printStackTrace();
	    }
		
	}
	
	
	//Method determines the number of unique values in discrete column
	private int determineNumDiscrete(){
		
		//Loop through row list and save the value of of column into array
		columnValues = new String[rowList.size()];
		String[] currentRow;
		
		for(int i = 0; i < rowList.size(); i++){
			
			currentRow = rowList.get(i).split(",");
			
			columnValues[i] = currentRow[discreteColumn];
			
		}
		
		//Determine the unique values and save into array
		uniqueValues = Arrays.stream(columnValues).distinct().toArray(String[]::new);
		
		System.out.println("Unique Values: " + Arrays.toString(uniqueValues));
		
		return uniqueValues.length;
		
	}
	
	//Create a single split CSV file containing data for that discrete measurement value
	private void generateSplitCsv(int index){
		
		System.out.println("Creating for CSV dataMeasurement_" + index);
		
		ArrayList<String> newRowList = new ArrayList();
		
		//Create list of data
		for (int i = 0; i < this.rowList.size(); i++) {
			
			if(columnValues[i].equals(uniqueValues[index - 1])){
				
				newRowList.add(this.rowList.get(i));
				
			}

	    }
		
		//Create output csv file
		try {
			
			FileWriter writer = new FileWriter(this.outputFolderPath + "dataMeasurement_" + index + ".csv");
			
			for(int i = 0; i < newRowList.size(); i++) {
				writer.write(newRowList.get(i) + "\n");
			}

		    writer.close();
		    
		    System.out.println("Successfully created CSV dataMeasurement_" + index);
		    
		} catch (IOException e) {
			
			System.out.println("Error creating CSV dataMeasurement_" + index);
			
			e.printStackTrace();
			
		}

	}

	//Method copies the full data to output folder if there is no discrete value
	private void copyFullData(){
		
		//Create output csv file
		try {
			
			File inputFile = new File(inputCsvPath);
			File outputFile = new File(this.outputFolderPath + "dataMeasurement_1.csv");
			
			Files.copy(inputFile.toPath(), outputFile.toPath());
		    
		    System.out.println("Successfully created CSV dataMeasurement_1");
		    
		} catch (IOException e) {
			
			System.out.println("Error creating CSV dataMeasurement_1");
			
			e.printStackTrace();
			
		}
		
	}
	
	//Method clears the Split_By_Discrete directory to avoid duplicate files
	private void clearSaveDirectory(){
		
		File dir = new File(outputFolderPath);
		
		for(File file: dir.listFiles()) {
			
			 if (!file.isDirectory()) {
				 file.delete();
			 }
		        
		}
		   
		
	}
	
}
