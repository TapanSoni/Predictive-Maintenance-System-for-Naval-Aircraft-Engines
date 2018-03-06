dataSetSpeed = readtable('C:\Users\hydro\Documents\School\Fall 2017\Software Eng\github 11.3\Predictive-Maintenance-System-master\Data_Converter\Files\Speed CSVs\dataSpeed9.csv','ReadVariableNames',false);



dataA = dataSetSpeed  % some test data
p = .7      % proportion of rows to select for training
N = size(dataA,1)  % total number of rows 
tf = false(N,1)    % create logical index vector
tf(1:round(p*N)) = true     
tf = tf(randperm(N))   % randomise order
dataTraining = dataA(tf,:) 
dataTesting = dataA(~tf,:)

writetable(dataTraining,'C:\Users\hydro\Documents\School\Fall 2017\Software Eng\Test_Train_Datasets\dataTrainingSpeed9.csv')
writetable(dataTesting,'C:\Users\hydro\Documents\School\Fall 2017\Software Eng\Test_Train_Datasets\dataTestingSpeed9.csv')