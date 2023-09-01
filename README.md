# Pre-market FDA Analysis
## Visualize FDA Pre-market Clearance Time for Regulatory
### If this is the first time you use this script, please go to the [bottom of this page](https://github.com/Zili125935/pre_market_analysis#environment-setup) to do the environment set up first
### 1. Daily Use
* Step 1:\
Rename the input Excel file to 'EXPORT.xlsx'\
copy the input Excel file under the folder 'Sunshine Act','semi_auto_process'\
![input](https://github.com/Zili125935/semi_auto_process/assets/107199759/1c6ae8e4-580e-4e31-a672-3bdd88ec97e9)
**Please make sure rename the new input excel file as 'EXPORT.xlsx' everytime you use this script!**

* Step 2:\
Open 'Command Prompt', copy paste & enter
```
cd OneDrive - STG-Business\Desktop\Sunshine Act\semi_auto_process
git pull
python sunshine_run.py
```
* Note - \
Please note if the folder name is changed, you have to change the command as well.\
For example, if the folder 'Sunshine Act' has be changed to 'Sunshine', the first command will be\
```cd Desktop\Sunshine\semi_auto_process```

## Environment Setup
#### Prerequisite - install Python and Git

Open 'Command Prompt' and follow the instruction\
![command](https://github.com/Zili125935/semi_auto_process/assets/107199759/0686dfed-c293-4395-8ca9-ffecd353f1cc)


* Step 1:\
 Open Command prompt and choose the location you want to save the auto process.\
 For example, if you want save the file in the 'FDA Clearance Plot' under 'Desktop', you can type 
```
cd OneDrive - STG-Business\Desktop\FDA Clearance Plot
```
* Step 2:\
 clone the repo to your local, please copy and paste the following command in your command line
```
git clone https://github.com/Zili125935/pre_market_analysis.git
cd pre_market_analysis
pip install -r requirements.txt
```
*Remember to click 'enter'
* Step 3:\
copy the FDA clearance file, usually the file name is 'pmn96cur.txt' under folder 'pre_market_analysis'\
If you have renamed your FDA Clearance file, please make sure to use the modified name\
*Please remember this script only accept .txt file, if you would like to use excel as your source file, please contact the author.

* Step 4:\
Go back to Command, copy & paste the following command to run the script
```
python pre-mkt FDA.py
