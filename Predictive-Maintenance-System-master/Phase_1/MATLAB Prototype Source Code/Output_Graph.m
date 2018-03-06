%Code to generate a dynamic filepath to run the function on any computer
currentDir = pwd;
splitDir = strsplit(currentDir, 'Predictive_Maintenance_System');
rootDir = splitDir(1);
finalPath = strcat(rootDir, 'Predictive_Maintenance_System\Files\Predicted_Data\predictedFull.csv');
pathToLoad = char(finalPath);

%Read in the CSV of principal components and predicted classes
scatterPlotData = readtable (pathToLoad,'ReadVariableNames',false);
  
%Set the x-axis to be the first column (first PC score)
xAxis = table2array(scatterPlotData(:,1));

%Set the y-axis to be the second column (second PC score)
yAxis = table2array(scatterPlotData(:,2));

%Set the class array to be the fourth column (predicted class)
class = table2array(scatterPlotData(:,4));

%Create array to hold the color for each data point
mycolor = strings(length(xAxis),1);

%Variable for the data point size in the scatter plot
pointsize = 12;

%Loop through the class array and set the color array based on the value
% 0 is good - set to green
% 1 is warning - set to yellow
% 2 is alert - set to red
for i = 1:numel(class)
     
      if class(i,:)== 0
          mycolor(i,:) = 'g';
      end
      
      if class(i,:) == 1
          mycolor(i,:)= 'y';
      end
      
      if class(i,:) == 2
          mycolor(i,:)= 'r';
      end
   
 end  
 
%Create table with the xAxis, yAxis, and color
fullData = cat(2,xAxis,yAxis,mycolor);
  
%Create table that contains good data
%Determined by column 3 in fullData that has the value 'g'
goodCriteria = fullData(:,3) == 'g';
goodData = fullData(goodCriteria,:);

%Create table that contains warning data
%Determined by column 3 in fullData that has the value 'y'
warnCriteria = fullData(:,3) == 'y';
warnData = fullData(warnCriteria,:);
 
%Create table that contains alarm data
%Determined by column 3 in fullData that has the value 'r'
alarmCriteria = fullData(:,3) == 'r';
alarmData = fullData(alarmCriteria,:);
  
%Create a figure to hold that graph that is not visible
figure1 = figure('visible','off');

%Hold to plot multiple data sets before figure is generated
hold on

    %Plot each good, warning, and alarm data set into scatter plot with
    %specified color
    scatter(goodData(:,1), goodData(:,2), pointsize, [.36 .72 .36], 'filled')
    scatter(warnData(:,1), warnData(:,2), pointsize, [.94 .68 .31], 'filled')
    scatter(alarmData(:,1), alarmData(:,2), pointsize, [.85 .33 .31], 'filled')
    
    %Set the axis labels, legend, and title
    xlabel('First Principal Component')
    ylabel('Second Principal Component')
    legend('Good','Warning','Alarm')
    title('Classification of Each Data Point')

%Hold off to create figure/graph
hold off

%Set dynamic file path for saving graph as image
finalPath = strcat(rootDir, 'Predictive_Maintenance_System\Output\images\outputGraph.png');
pathToLoad = char(finalPath);

%Convert figure to image and save
saveas(figure1,pathToLoad) 