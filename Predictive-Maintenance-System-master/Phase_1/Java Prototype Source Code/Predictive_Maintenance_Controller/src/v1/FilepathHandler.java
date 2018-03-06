package v1;

public class FilepathHandler {
	
	private String rootDir;
	
	//File path for the Split File Directory, used with DataSplitter class
	public static String splitFileDir;
	
	//File paths for performing PCA paths, used with PrincipalComponentAnalyzer class
	public static String inputPcaDir;
	public static String outputPcaDir;
	public static String currentFileDir;
	
	//File path for prediction classes
	public static String predictionDir;
	
	//MATLAB exe file paths
	public static String pcaFunctionTestingPath;
	public static String trainedModelPath;
	public static String outputGenPath;
	
	//Output html path
	public static String predictDir;
	public static String outputHtmlPath;
	
	//Settings file path
	public static String settingsPath;
	
	//Example testing folder
	public static String testPath;
	
	public FilepathHandler(){

		//Set the working directory of current computer
		setRootDir();
		
		//Set the file paths used in the program
		splitFileDir = rootDir + "Predictive_Maintenance_System\\Files\\Split_By_Discrete\\";
		
		inputPcaDir = rootDir + "Predictive_Maintenance_System\\Files\\Split_By_Discrete\\";
		outputPcaDir = rootDir + "Predictive_Maintenance_System\\Files\\Classification_Tables\\";
		currentFileDir = rootDir + "Predictive_Maintenance_System\\Files\\Current_File\\";
		
		predictionDir = rootDir + "Predictive_Maintenance_System\\Files\\Predicted_Data\\";
		
		pcaFunctionTestingPath = rootDir + "Predictive_Maintenance_System\\Matlab\\PCA_Function_Testing.exe";
		
		trainedModelPath = rootDir + "Predictive_Maintenance_System\\Matlab\\Trained_Model.exe";
		
		outputGenPath = rootDir + "Predictive_Maintenance_System\\Matlab\\Output_Graph.exe";
		
		outputHtmlPath = rootDir + "Predictive_Maintenance_System\\Output\\pages\\index.html";
		
		settingsPath = rootDir + "Predictive_Maintenance_System\\Files\\settings.txt";
		
		testPath = rootDir + "Predictive_Maintenance_System\\Files\\Example Testing Data\\";
		
	}

	//Method gets the current directory and splits by the project root folder
	//Sets the root directory
	private void setRootDir(){
		
		//Get the complete root directory file path
		String fullRootDir = System.getProperty("user.dir");
		
		//Split the full directory by the project root folder
		String[] dirParts = fullRootDir.split("Predictive_Maintenance_System");
		
		//Set rootDir to be the 0th element of the array
		this.rootDir = dirParts[0];
		
	}
	
}
