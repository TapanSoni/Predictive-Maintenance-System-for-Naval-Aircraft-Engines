package v1;

import java.io.File;

public class PreprocessController {
	
	private String filePath;
	
	public PreprocessController(String path, int columnToSplit){
		
		System.out.println("Starting preprocessing on data...");
		
		this.filePath = path;

		//Split by measurement interval (discrete column) if applicable
		//In original data set it is the lever position
		//If no measurement interval in the data set it will return the same data set
		//Pass 0 if there is no measurement column
		DataSplitter splitter = new DataSplitter(filePath, columnToSplit);
		
		System.out.println("Preprocessing on data complete...");

	}

	
	//Getters
	public String getFilePath() {
		return filePath;
	}
	
}
