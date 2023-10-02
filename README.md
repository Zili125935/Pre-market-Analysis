# Pre-market FDA Analysis
## Visualize FDA Pre-market Clearance Time for Regulatory
### If this is the first time you use this script, please go to the [bottom of this page](https://github.com/Zili125935/pre_market_analysis#environment-setup) to do the environment set up first
### 1. Daily Use
* Step 1:\
copy the FDA clearance file, usually the file name is 'pmn96cur.txt' under folder 'pre_market_analysis'\
If you have renamed your FDA Clearance file, please make sure to use the modified name\
**Please remember this script only accept .txt file, if you would like to use excel as your source file, please contact the author**

* Step 2:\
Open 'Command Prompt', copy paste & enter
```
cd Downloads\FDA Clearance Plot\pre_market_analysis
git pull
python pre_mkt_FDA.py
```
* Note - \
Please note if the folder name is changed, you have to change the command as well.\
For example, if the folder 'FDA Clearance Plot' has be changed to 'FDA Plot', the first command will be\
```cd Downloads\FDA Plot\pre_market_analysis```\
Please remember the file route we are using now is under 'Downloads'. If you would like change direction to other folders, for example to OneDrive, please contact Zili Huang.

## Environment Setup
#### Prerequisite - install Python and Git

Open 'Command Prompt' and follow the instruction\
![command](https://github.com/Zili125935/semi_auto_process/assets/107199759/0686dfed-c293-4395-8ca9-ffecd353f1cc)


* Step 1:\
 Open Command prompt and choose the location you want to save the auto process.\
 For example, if you want save the file in the 'FDA Clearance Plot' under 'Downloads', you can type 
```
cd Downloads\FDA Clearance Plot
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
python pre_mkt_FDA.py
