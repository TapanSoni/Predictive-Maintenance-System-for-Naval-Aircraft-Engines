package v1;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.filechooser.FileFilter;
import javax.swing.filechooser.FileNameExtensionFilter;

public class GuiMain {

    private String currentFile;

    public GuiMain() {
        
        createAndShow();

    }

	//Instantiate the GUI and set it to visible
    private void createAndShow() {

        JFrame frame = new JFrame("Predictive Maintenance System - Team Elephants");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Set the file types that the user can browse for
        //Only allow CSV right now
        JFileChooser fileSelect = new JFileChooser();
        fileSelect.setCurrentDirectory(new File(FilepathHandler.testPath));
        FileFilter csv = new FileNameExtensionFilter("CSV Files", new String[] { "csv" });

        fileSelect.setFileFilter(csv);

        //Setting up buttons and textfield for filepath
        JButton browseButton = new JButton("Browse");
        JButton settingsButton = new JButton("Settings");
        JButton runButton = new JButton("Run");
        JTextField filePathText = new JTextField(" Click browse to select data file...");

        filePathText.setPreferredSize(new Dimension(500, 30));
        settingsButton.setPreferredSize(new Dimension(150, 30));
        runButton.setPreferredSize(new Dimension(150, 30));
        browseButton.setPreferredSize(new Dimension(150, 30));

		//Instantiating JPanels
        JPanel containerPanel = new JPanel();
        JPanel fileIOPanel = new JPanel();
        JPanel settingsRunPanel = new JPanel();

		//Seeting JPanel layouts and adding buttons and textboxes
        fileIOPanel.setLayout(new BorderLayout(2, 5));
        settingsRunPanel.setLayout(new BoxLayout(settingsRunPanel, BoxLayout.PAGE_AXIS));

        fileIOPanel.add(filePathText, BorderLayout.PAGE_START);
        fileIOPanel.add(runButton, BorderLayout.CENTER);

        fileIOPanel.add(browseButton, BorderLayout.LINE_START);
        fileIOPanel.add(settingsButton, BorderLayout.LINE_END);

		//Adding jpanels to parent panel and setting GUI dimensions
        containerPanel.add(fileIOPanel);
        containerPanel.add(settingsRunPanel);

        frame.setSize(620, 125);
        frame.add(containerPanel);
        frame.setVisible(true);

		//Allow Browse button to instantiate a JFileSelector
        browseButton.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {

                int result;

                String filePath = "";
				//Sets the currentFile string to the filepath of the selected file and prints it to the console
                result = fileSelect.showOpenDialog(null);
                if (result == JFileChooser.APPROVE_OPTION) {
                    filePath = fileSelect.getSelectedFile().getAbsolutePath();
                    filePathText.setText(filePath);
                    setCurrentFile(filePath);
                    System.out.println("The current filepath is " + getCurrentFile());
                }
            }
        });

		//Allows Settings button to instantiate a new GuiSettings 
        settingsButton.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {

                GuiSettings guiSettings = new GuiSettings();
            }
        });

		
		//Allow the run button to instantiate GuiProgressController 
        runButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                System.out.println("The Run button has been pressed.");
                
                //Create instance of GuiProgressController
                GuiProgressController guiController = new GuiProgressController(getCurrentFile());
                
                //Create the web based output
                OutputGenerator output = new OutputGenerator();
                output.displayOutput();

            }
        });

    }
    
	//Setters
	
    public void setCurrentFile(String s) {
        this.currentFile = s;
    }

	//Getters
	
    public String getCurrentFile() {
        return this.currentFile;
    }

}
