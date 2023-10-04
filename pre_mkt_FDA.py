import pandas as pd
import chardet
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import seaborn as sns
import os
import sys
from datetime import datetime

def main():
    task_time = datetime.now()
    cwd =os.getcwd()
    file_path = "pmn96cur.txt"
    # Detect the encoding of the file using chardet
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    file_encoding = result['encoding']
    # Read the .txt file into a pandas DataFrame with the detected encoding
    print('processing...')
    df = pd.read_csv(file_path, sep='|', encoding=file_encoding)


    #calculate duration
    df['DATERECEIVED'] = pd.to_datetime(df['DATERECEIVED'])
    df['DECISIONDATE'] = pd.to_datetime(df['DECISIONDATE'])
    df['Duration'] = df['DECISIONDATE'] - df['DATERECEIVED']
    df_duration = df.copy()
    df_duration['DATERECEIVED'] = pd.to_datetime(df['DATERECEIVED'])
    df_duration = df_duration[df_duration['DECISIONDATE'] > '2017-12-31']
    df_dental = df_duration[df_duration['CLASSADVISECOMM'] == 'DE']
    df_tra_dental = df_dental[df_dental['TYPE'] == 'Traditional']
    df_dzenhapnp = df_tra_dental[df_tra_dental['PRODUCTCODE'].isin(['DZE', 'NHA', 'PNP'])]
    df_stm = df_dzenhapnp[df_dzenhapnp['APPLICANT'].str.contains('Straumann', case=False)]
    df_comp = df_dzenhapnp[~df_dzenhapnp['APPLICANT'].str.contains('Straumann', case=False)]

    #Line plot
    df_tra_dental['DECISIONDATE'] = pd.to_datetime(df_tra_dental['DECISIONDATE'])
    df_dzenhapnp['DECISIONDATE']= pd.to_datetime(df_dzenhapnp['DECISIONDATE'])
    df_stm['DECISIONDATE'] = pd.to_datetime(df_stm['DECISIONDATE'])
    df_comp['DECISIONDATE'] = pd.to_datetime(df_comp['DECISIONDATE'])

    # Extract years
    df_tra_dental['Year'] = df_tra_dental['DECISIONDATE'].dt.year
    df_dzenhapnp['Year'] = df_dzenhapnp['DECISIONDATE'].dt.year
    df_stm['Year'] = df_stm['DECISIONDATE'].dt.year
    df_comp['Year'] = df_comp['DECISIONDATE'].dt.year

    # Calculate the average duration for each year
    Dental_All = df_tra_dental.groupby('Year')['Duration'].mean()
    Dental_DZE_NHA_PNP = df_dzenhapnp.groupby('Year')['Duration'].mean()
    Straumann_DZE_NHA_PNP = df_stm.groupby('Year')['Duration'].mean()
    Competition_DZE_NHA_PNP = df_comp.groupby('Year')['Duration'].mean()

    #Convert durations to days for y-axis formatting
    Dental_All= Dental_All.dt.days
    Dental_DZE_NHA_PNP = Dental_DZE_NHA_PNP.dt.days
    Straumann_DZE_NHA_PNP = Straumann_DZE_NHA_PNP.dt.days
    Competition_DZE_NHA_PNP = Competition_DZE_NHA_PNP.dt.days

    #seaborn style
    sns.set(style="whitegrid")

    # Create line charts
    plt.figure(figsize=(10, 6))

    sns.lineplot(data=Dental_All, marker="o", label='Dental All Traditional', color = '#195AFA')
    sns.lineplot(data=Dental_DZE_NHA_PNP, marker="o", label='Dental DZE-NHA-PNP', color = '#36393A')
    sns.lineplot(data=Straumann_DZE_NHA_PNP, marker="o", label='Straumann DZE-NHA-PNP', color = '#B98C3C')
    sns.lineplot(data=Competition_DZE_NHA_PNP, marker="o", label='Competition DZE-NHA-PNP', color = '#D52B1E')

    # Format y-axis ticks to display values as integers (e.g., 120 instead of 1.2)
    def format_y_ticks(value, _):
        return f"{int(value)}"
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_y_ticks))

    plt.xlabel("Clearence Year")
    plt.ylabel("Number of days")
    plt.title("Average Time to FDA Clearance")

    # Show the legend
    plt.legend(title='Types of Dental')

    # Show the plot
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the lineplot as a JPG image
    plt.savefig(f"Avg FDA Clearance line chart {task_time.strftime('%Y-%m-%d_%H%M%S')}.jpg", dpi=300)
    plt.show()


    #Barplot
    df_tra_dental['DECISIONDATE'] = pd.to_datetime(df_tra_dental['DECISIONDATE'])
    df_dzenhapnp['DECISIONDATE']= pd.to_datetime(df_dzenhapnp['DECISIONDATE'])
    df_stm['DECISIONDATE'] = pd.to_datetime(df_stm['DECISIONDATE'])
    df_comp['DECISIONDATE'] = pd.to_datetime(df_comp['DECISIONDATE'])

    # Extract years
    df_tra_dental['Year'] = df_tra_dental['DECISIONDATE'].dt.year
    df_dzenhapnp['Year'] = df_dzenhapnp['DECISIONDATE'].dt.year
    df_stm['Year'] = df_stm['DECISIONDATE'].dt.year
    df_comp['Year'] = df_comp['DECISIONDATE'].dt.year

    # Calculate the average duration for each year
    count_dental = df_tra_dental.groupby('Year').size().reset_index(name='Count')
    count_dental_dnp = df_dzenhapnp.groupby('Year').size().reset_index(name='Count')
    count_straumann = df_stm.groupby('Year').size().reset_index(name='Count')
    count_comp = df_comp.groupby('Year').size().reset_index(name='Count')

    # # Add a new column indicating the DataFrame source
    count_dental['DataFrame'] = 'Dental All Traditional'
    count_dental_dnp['DataFrame'] = 'Dental DZE-NHA-PNP'
    count_straumann ['DataFrame'] = 'Straumann_DZE-NHA-PNP'
    count_comp['DataFrame'] = 'Competition DZE-NHA-PNP'

    combined_counts = pd.concat([count_dental, count_dental_dnp, count_straumann, count_comp], ignore_index=True)

    # Set the style for Seaborn
    sns.set(style="whitegrid")

    # Create the bar chart using Seaborn
    plt.figure(figsize=(10, 6))

    #Change colors
    custom_colors = ["#195AFA", "#36393A", "#B98C3C", "#D52B1E"]

    # Plot the bar chart with hue for each DataFrame
    sns.barplot(data=combined_counts, x='Year', y='Count', hue='DataFrame', palette=custom_colors)

    # Set plot labels and title
    plt.xlabel("Clearence Year")
    plt.ylabel("# of Tradtional 510(k)s")
    plt.title("# of Traditional 510(k)s Cleared by FDA")

    # Show the legend
    plt.legend(title='Types of Dental')

    # Show the barplot
    plt.xticks(rotation=45)
    plt.tight_layout()
    #export as jpg
    filename = f"Trational Bar chart {task_time.strftime('%Y-%m-%d_%H%M%S')}.jpg"
    plt.savefig(filename, dpi=300)
    plt.show()

if __name__ == "__main__":
    sys.exit(main())