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

    %Create a matrix of the PCA scores and class of data for each row
    classificationMatrix = cat(2, score(:,1), score(:,2));

    %Set the output path csv dynamically
    currentDir = pwd;
    splitDir = strsplit(currentDir, 'Predictive_Maintenance_System');
    rootDir = splitDir(1);
    finalPath = strcat(rootDir, 'Predictive_Maintenance_System\Files\Current_File\dataPCA.csv');
    pathToLoad = char(finalPath);
    
    %Save the classification matrix as a CSV file in Classification_Tables
    csvwrite(pathToLoad, classificationMatrix)

end