package v1;

import java.awt.BorderLayout;
import java.awt.Dimension;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class GuiProgressController {
	
	//Class controls the flow of the program and displays the status to the user
	public GuiProgressController(String currentFile){
		
		//Unfinished GUI for displaying the proress
		JFrame frame = new JFrame("Progress");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(300, 200);
		
		JPanel statusPanel = new JPanel();
		JLabel statusLabel = new JLabel();
		statusLabel.setText("Preprocessing data...");
		statusPanel.setLayout(new BorderLayout(2, 5));
		statusPanel.add(statusLabel, BorderLayout.CENTER);
		frame.add(statusPanel);
		
		//Not showing
		frame.setVisible(false);
		
		//Preprocess data
		PreprocessController preprocessController = new PreprocessController(currentFile, 1);

		//Perform PCA on data
		statusLabel.setText("Performing Principal Component Analysis on data..."+1);
		frame.revalidate();
		PrincipalComponentAnalyzer pca = new PrincipalComponentAnalyzer();
		
		//Pass full PCA data set into the Trained Model
		statusLabel.setText("Passing data to training model to predict maintenance levels...");
		frame.revalidate();
		TrainedModel model = new TrainedModel();
		
		statusLabel.setText("Generating and opening output...");
		frame.revalidate();
		try {
			Thread.currentThread().sleep(3000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
		}
		frame.dispose();

	}

}
