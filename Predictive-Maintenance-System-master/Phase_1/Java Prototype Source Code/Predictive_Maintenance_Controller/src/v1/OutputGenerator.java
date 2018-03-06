package v1;

import java.awt.Desktop;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.stream.Stream;

public class OutputGenerator {
	
	private String graphExe;
	private String outputPath;
	
	private ArrayList<String> combinedData;
	private ArrayList<String> predictionData = new ArrayList();
	private ArrayList<String> pcaData = new ArrayList();
	
	public OutputGenerator(){
		
		//Set the graphExe to dynamic path
		graphExe = FilepathHandler.outputGenPath;
		outputPath = FilepathHandler.outputHtmlPath;
		
		
		
		System.out.println("Generating Output");
		
		//Class to format and open web browser compatible output
		//Will replace parts of Bootstrap template with generated code
		
		//Combine PCA and Prediction CSV files
		combineData();
		
		findPercentages(predictionData);
		
		//Generate Graph for output
		generateGraph();
		
	}
	
	//Method opens the output webpage in the default web browser
	public void displayOutput(){
		
		File htmlFile = new File(this.outputPath);
		
		try {
			Desktop.getDesktop().browse(htmlFile.toURI());
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
	private void combineData(){
		
		combinedData = new ArrayList();
		
		String pcaDataPath = FilepathHandler.outputPcaDir + "Full_Table\\dataPcaFull.csv";
		
		String predictionPath = FilepathHandler.predictionDir + "predictedClasses.csv";

		
		//Read CSVs into ArrayLists
		//PCA Data
		try(BufferedReader brPca = new BufferedReader(new FileReader(pcaDataPath))) {

			
	        String line = "";
	        while ((line = brPca.readLine()) != null) {
	        	
	        	//Add line to the List
	        	pcaData.add(line);
	        }
	        
	        brPca.close();
	        
	    } catch (IOException e) {
	    	System.err.println("Error reading in data file.");
	        e.printStackTrace();
	    }
		
		//Prediction Data
		try(BufferedReader brPred = new BufferedReader(new FileReader(predictionPath))) {

			
	        String line = "";
	        while ((line = brPred.readLine()) != null) {
	        	
	        	//Add line to the List
	        	predictionData.add(line);
	        }
	        
	        brPred.close();
	    } catch (IOException e) {
	    	System.err.println("Error reading in data file.");
	        e.printStackTrace();
	    }
		
		//Check the both data sets are the same length
		if(pcaData.size() == predictionData.size()){
			
			for(int i = 0; i < pcaData.size(); i++){
				
				combinedData.add(pcaData.get(i) + ", " + predictionData.get(i));
				
			}
			
		}else{
			System.out.println("Error - PCA and Prediction data sets are not the same length. Exiting...");
			return;
		}
		
	}
	
	private void generateGraph(){
		
		//Create CSV from data
		try {
			
			FileWriter writer = new FileWriter(FilepathHandler.predictionDir + "predictedFull.csv");
			
			for(int i = 0; i < combinedData.size(); i++) {
				writer.write(combinedData.get(i) + "\n");
			}

		    writer.close();
		    
		    System.out.println("Successfully created CSV predictedFull");
		    
		} catch (IOException e) {
			
			System.out.println("Error creating CSV predictedFull");
			
			e.printStackTrace();
			
		}
		
		MatlabExecutor matlab = new MatlabExecutor(this.graphExe);
		
	}
	
	public void findPercentages(ArrayList<String> list){	
		
		int numberOfZeros = 0, numberOfOnes = 0, numberOfTwos = 0;
		String zerosPercent, onesPercent, twosPercent;
		
 		for (int i=0; i<list.size(); i++){
 		    if (list.get(i).equals("0")){
 		        numberOfZeros++;
 		    }
 		    else if (list.get(i).equals("1")){
 		        numberOfOnes++;
 		    }
 		   else if (list.get(i).equals("2")){
 		        numberOfTwos++;
 		    }		 		   
 		}
 		
 		System.out.println(numberOfZeros + ", " + numberOfOnes + ", " + numberOfTwos);
 		System.out.println(list.size());
 		
 		String[] splitPercent;
 		
 		//Calculate the percent
 		zerosPercent = Double.toString(((double) numberOfZeros/list.size()) * 100);
 		splitPercent = zerosPercent.split("\\.");
 		try{
 			zerosPercent = splitPercent[0] + "." + splitPercent[1].substring(0, 2);
 		}catch(StringIndexOutOfBoundsException e){
 			zerosPercent = zerosPercent;
 		}
 		
 		
 		onesPercent = Double.toString(((double) numberOfOnes/list.size()) * 100);
 		splitPercent = onesPercent.split("\\.");
 		try{
 			onesPercent = splitPercent[0] + "." + splitPercent[1].substring(0, 2);
 		}catch(StringIndexOutOfBoundsException e){
 			onesPercent = onesPercent;
 		}
 		
 		twosPercent = Double.toString(((double) numberOfTwos/list.size()) * 100);
 		splitPercent = twosPercent.split("\\.");
 		try{
 			twosPercent = splitPercent[0] + "." + splitPercent[1].substring(0, 2);
 		}catch(StringIndexOutOfBoundsException e){
 			twosPercent = twosPercent;
 		}
 		
 		//Replace the values in the html output
 		//Get the html page as a String
 		String htmlText = readLineByLineHtml(outputPath);

 		
 		//Replace Good Percent in web output
 		String oldPercent = findVaribleBetweenTwoPatterns(htmlText, "<span id=\"goodData\">", "</div><div>Data Considered Good</div>");
 		htmlText = htmlText.replace("<span id=\"goodData\">" + oldPercent + "</div><div>Data Considered Good</div>", "<span id=\"goodData\">" + zerosPercent + "%</div><div>Data Considered Good</div>");
 		
 		//Replace Warning Percent in web output
 		oldPercent = findVaribleBetweenTwoPatterns(htmlText, "<span id=\"warnData\">", "</div><div>Data Considered Warning</div>");
 		htmlText = htmlText.replace("<span id=\"warnData\">" + oldPercent + "</div><div>Data Considered Warning</div>", "<span id=\"warnData\">" + onesPercent + "%</div><div>Data Considered Warning</div>");
 		
 		//Replace Alarm Percent in web output
 		oldPercent = findVaribleBetweenTwoPatterns(htmlText, "<span id=\"alarmData\">", "</div><div>Data Considered Alarm</div>");
 		htmlText = htmlText.replace("<span id=\"alarmData\">" + oldPercent + "</div><div>Data Considered Alarm</div>", "<span id=\"alarmData\">" + twosPercent + "%</div><div>Data Considered Alarm</div>");
 		
 		//Overwrite web output with percents
 		try(  PrintWriter out = new PrintWriter( outputPath )  ){
 		    out.println( htmlText );
 		    
 		    out.close();
 		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

 		System.out.println(zerosPercent);
 		System.out.println(onesPercent);
 		System.out.println(twosPercent);
		
	}
	
	//Method find the variable between two String patterns
	public String findVaribleBetweenTwoPatterns(String page, String pattern1, String pattern2){

        String foundString = "";
        int pattern1Length = pattern1.length();
        
        foundString = (page.substring(page.indexOf(pattern1) + pattern1Length, page.indexOf(pattern2))).trim();
        
        foundString = foundString.replace("_", "");
        
        return foundString;
    }
	
	//Method reads the HTML content into a String
	private static String readLineByLineHtml(String filePath){
	    StringBuilder contentBuilder = new StringBuilder();
	    try (Stream<String> stream = Files.lines( Paths.get(filePath), StandardCharsets.UTF_8))
	    {
	        stream.forEach(s -> contentBuilder.append(s).append("\n"));
	    }
	    catch (IOException e)
	    {
	        e.printStackTrace();
	    }
	    return contentBuilder.toString();
	}

}
