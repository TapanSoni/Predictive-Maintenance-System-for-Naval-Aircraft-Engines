package v1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class PrincipalComponentAnalyzer {

	//Variables to hold file paths
	private String currentFilePath = "";
	private String currentFileOutputPath = "";
	private String inputDirectory;
	private String currentFileDirectory;
	private String outputDirectory;

	//File path for the PCA_Function_Testing exe
	private final String pcaFunctionPath;
	
	
	public PrincipalComponentAnalyzer() {
		
		//Get directory paths
		inputDirectory = FilepathHandler.inputPcaDir;
		currentFileDirectory = FilepathHandler.currentFileDir;
		outputDirectory = FilepathHandler.outputPcaDir;
		pcaFunctionPath = FilepathHandler.pcaFunctionTestingPath;

		//Clear Classification directory
		File outDir = new File(this.outputDirectory);
		
		for(File file: outDir.listFiles()) {
			
			 if (!file.isDirectory()) {
					 file.delete();
			 }
		        
		}
		
		// Class loops through each data in Files/Split_By_Discrete
		File dir = new File(inputDirectory);
		File[] directoryListing = dir.listFiles();
		if (directoryListing != null) {
			
			int index = 1;

			for (File child : directoryListing) {

				// try to scan file, if reaches the end of try block add file to
				// "Success" folder
				try {

					// Set the current file name
					this.currentFilePath = child.getAbsolutePath();

					// Move file into currentFileDirectory
					//child.renameTo(new File(currentFileDirectory + "data" + index + ".csv"));
					child.renameTo(new File(currentFileDirectory + "data.csv"));

					// Perform PCA Function on the data
					MatlabExecutor matlab = new MatlabExecutor(this.pcaFunctionPath);
					
					//Move PCA output to classification directory
					File currentPcaFile = new File(currentFileDirectory + "dataPCA.csv");
					currentPcaFile.renameTo(new File(outputDirectory + "dataPCA" + index + ".csv"));
					
					//Clear current file directory
					File currentDir = new File(this.currentFileDirectory);
					
					for(File file: currentDir.listFiles()) {
						
						 if (!file.isDirectory()) {
								 file.delete();
						 }
					        
					}
					
					Thread.sleep(500);

				} catch (Exception e) {

					e.printStackTrace();

				}
				
				index++;

			}
		} else {

			// TODO
			System.out.println("Error finding or accessing directory.");
		}

		// Combines each separate output file from the PCA_Function into one
		// full CSV
		// Saved into Files\Classification_Tables\Full_Table
		combinePcaFiles();

	}

	//Method combines the separate PCA files to one complete data set
	private void combinePcaFiles() {
		
		ArrayList<String> rowList = new ArrayList();

		File outDir = new File(outputDirectory);
		File[] outDirectoryListing = outDir.listFiles();
		if (outDirectoryListing != null) {
			
			int index = 1;

			for (File child : outDirectoryListing) {

				// try to scan file, if reaches the end of try block add file to
				// "Success" folder
				try {

					// Set the current file name
					this.currentFilePath = child.getAbsolutePath();
					
					//Get the file extension
	                String extension = "";

	                int i = currentFilePath.lastIndexOf('.');
	                if (i > 0) {
	                    extension = currentFilePath.substring(i+1);
	                }
					
					if (extension.equalsIgnoreCase("csv")) {

						try (BufferedReader br = new BufferedReader(new FileReader(this.currentFilePath))) {

							String line = "";
							while ((line = br.readLine()) != null) {

								// Add line to the List
								rowList.add(line + ", " + index);
							}
							
							br.close();
							
						} catch (IOException e) {
							System.err.println("Error reading in data file.");
							e.printStackTrace();
						}

					}

				} catch (Exception e) {

					e.printStackTrace();

				}
				
				index++;

			}
		} else {

			// TODO
			System.out.println("Error finding or accessing directory.");
		}
		
		//Create full CSV of entire data set in row list
		try {
			
			FileWriter writer = new FileWriter(this.outputDirectory + "\\Full_Table\\dataPcaFull.csv");
			
			for(int i = 0; i < rowList.size(); i++) {
				writer.write(rowList.get(i) + "\n");
			}

		    writer.close();
		    
		    System.out.println("Successfully created CSV dataPcaFull");
		    
		} catch (IOException e) {
			
			System.out.println("Error creating CSV dataPcaFull");
			
			e.printStackTrace();
			
		}
		
		//Clear Classification directory
		File dir = new File(this.outputDirectory);
		
		for(File file: dir.listFiles()) {
			
			 if (!file.isDirectory()) {
					 file.delete();
			 }
		        
		}
		
	}

}
