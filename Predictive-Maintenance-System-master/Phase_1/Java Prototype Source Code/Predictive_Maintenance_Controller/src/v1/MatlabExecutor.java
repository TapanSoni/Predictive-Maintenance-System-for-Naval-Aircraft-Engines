package v1;

import java.io.IOException;
import java.util.concurrent.TimeUnit;

public class MatlabExecutor {
	
	public MatlabExecutor(String File_Path) {
		try {
			
			System.out.println("Starting Matlab Exe: \n" + File_Path);
			
			Process p = Runtime.getRuntime().exec(File_Path);
	        p.waitFor(30, TimeUnit.SECONDS);
				
			System.out.println("Finished Running Matlab Exe: \n" + File_Path);
			
		} catch (IOException | InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
