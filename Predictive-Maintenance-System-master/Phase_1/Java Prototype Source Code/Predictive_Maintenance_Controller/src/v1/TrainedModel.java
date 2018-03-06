package v1;

public class TrainedModel {
	
	private String modelPath;
	
	public TrainedModel(){
		
		//Set the modelPath to dynamic path
		modelPath = FilepathHandler.trainedModelPath;
		
		//Class to pass new data from the PrincipalComponentAnalyzer to for predictions
		//Uses MatlabExecutor to call the Trained Model Executable
		MatlabExecutor matlab = new MatlabExecutor(this.modelPath);
		
		//Possibly add additional functionality to 
		//add data to trained model
		//generate new trained model
		
	}

}
