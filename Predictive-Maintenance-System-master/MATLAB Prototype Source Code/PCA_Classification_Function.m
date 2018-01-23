%Code to dynmically set the file path for files used
currentDir = pwd;
splitDir = strsplit(currentDir, 'Predictive_Maintenance_System');
rootDir = splitDir(1);
finalPath = strcat(rootDir, 'Predictive_Maintenance_System\Files\Current_File\data.csv');
pathToLoad = char(finalPath);

%Read in ship speed from an edited csv file and assign it to a currentDataTable
currentDataTable = readtable(pathToLoad,'ReadVariableNames',false);

%Call function to perform PCA and classify data
pcaClassifier(currentDataTable)

%Function to calculate the pca for the called dataSet, as well as graph the
%pca in a cumulative/indiviudal comparison plot for the # of principal
%components, and the percent of the data explained by that number 
%of principal components.
function z = pcaClassifier(data)

    %Parse table to array
    dataAsArray = table2array(data);
    
    %gets the size of the table where m = # of rows and n = # of columns
    %n will be used later for determining the # of individual principal
    %components, **m is not needed**.
    [m,n] = size(dataAsArray);
    
    %Normalize columns of matrix
    mn = mean(dataAsArray);
    sd = std(dataAsArray);
    sd(sd==0) = 1;

    dataNorm = bsxfun(@minus,dataAsArray,mn);
    dataNorm = bsxfun(@rdivide,dataNorm,sd);
    
    %Replace original data with normalized data
    dataAsArray = dataNorm;

    %Perform Principal Component Analysis on normalized data
    %Allows variance of data to be seen in only a few dimensions
    coeff = pca(dataAsArray);
    [coeff,score,latent] = pca(dataAsArray);

   
    %Calculate the IQR for the first two Principal Component Scores
    %This is used to determine outliers and create groups of data
    column1IQR = iqr(score(:,1));
    column2IQR = iqr(score(:,2));
    
    %Possible IQR values to use for determining groups of data
    %Currently using weak to achieve results for each group
    %Plan to allow the user to choose values based on settings file
    %Normal IQR in Stats: 1.5/3.0
    
    %STRICT?(Default?): 1.5/2.0
    %MEDIUM?: 1.25/1.75
    %WEAK?: 1.0/1.5
    
    %Variable to hold IQR multiplier
    %TODO read value from settings file to set this dynmically
    %Currently using weak values
    warningIqrMultiplier = 1.0;
    alarmIqrMultiplier = 1.5;
    
    %Determine the outlier coefficients for the first principal comp
    warningOutlierColumn1 = warningIqrMultiplier * column1IQR;
    alarmOutlierColumn1 = alarmIqrMultiplier * column1IQR;
    
    %Determine the outlier coefficients for the second principal comp
    warningOutlierColumn2 = warningIqrMultiplier * column2IQR;
    alarmOutlierColumn2 = alarmIqrMultiplier * column2IQR;

    %Group data points into Alarm and Warning groups
    %Generating a boolean array corresponding to each data point
    idxAlarm = score(:,1) > alarmOutlierColumn1 | score(:,1) < -alarmOutlierColumn1  | score(:,2) > alarmOutlierColumn2 | score(:,2) < -alarmOutlierColumn2;
    idxWarn = score(:,1) > warningOutlierColumn1  | score(:,2) > warningOutlierColumn2 | score(:,2) < -warningOutlierColumn2 & ~idxAlarm;

    %Create an array of the same length that initializes to all 0's
    classOfData = zeros(length(idxAlarm),1);
  
    %Loop through the Alarm array and set the class of data to group value
    %0 means the data point is in a good range
    %1 means the data point is in the warning range
    %2 means the data point is in the alarm range
    for i = 1:length(idxAlarm)
        
        if idxAlarm(i) == 1
            
            classOfData(i,1) = 2;
            
        elseif idxWarn(i) == 1
            
            classOfData(i,1) = 1;
            
        end
        
    end

    %Create a matrix of the PCA scores and class of data for each row
    classificationMatrix = cat(2, score(:,1), score(:,2), classOfData);
    
    %Set the output path csv dynamically
    currentDir = pwd;
    splitDir = strsplit(currentDir, 'Predictive_Maintenance_System');
    rootDir = splitDir(1);
    finalPath = strcat(rootDir, 'Predictive_Maintenance_System\Files\dataTraining.csv');
    pathToLoad = char(finalPath);

    %Save the classification matrix as a CSV file in Classification_Tables
    csvwrite(pathToLoad, classificationMatrix)

end