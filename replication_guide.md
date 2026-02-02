🚀 Quick Replication Guide

This guide provides step-by-step instructions to recreate the Enterprise BI Integration environment on your local machine. This project simulates a real-world "BI Flow" by connecting CRM, ERP, and EPM data sources.

## 1. Prerequisites
Before starting, ensure you have the following installed:
* **Python 3.x**
* **Power BI Desktop** (Latest version recommended)

## 2. Environment Setup
To ensure all Python dependencies are met for data generation, use the provided `requirements.txt` file.

1. Open your terminal or command prompt.
2. Navigate to the project root directory.
3. Run the following command:
   ```bash
   pip install -r requirements.txt

## 3. Data Generation

The dashboard relies on synthetic data that mimics enterprise structures from Oracle EBS, Salesforce, and Hyperion.

    1. Run the generation script: (Alternatively and easier click Get Data <- Python and past the data_generation.py script (make sure to have a proper venv for python on your Power BI configuration)

    Bash: python data_generation_script.py

    2. Verify that the following files have been created in your folder:

    Oracle_EBS_Actuals.csv (Transactional ERP data) | Power BI might not add a table for the csv, if so you can refer to the df_ tables generated

    Hyperion_Budget.csv (Multidimensional EPM data) | Power BI might not add a table for the csv, if so you can refer to the df_ tables generated

    Salesforce_Projects.csv (CRM Project metadata) | Power BI might not add a table for the csv, if so you can refer to the df_ tables generated

## 4. Loading the Power BI Template

This project is provided as a .pbit (Power BI Template) to maintain data privacy and a small file size.

    Open Nearshore_Profitability_Tracker.pbit in Power BI Desktop.

    Input Parameters: Upon opening, a dialogue box will appear asking for the file paths of the three CSV files generated in the previous step.

    Enter the full local path for each file (e.g., C:\Users\Name\Documents\Oracle_EBS_Actuals.csv).

    Click Load.

## 5. Architecture Notes

    Star Schema: The model automatically builds relationships between the Fact tables (EBS/Hyperion) and the Dimension tables (Date/Account/Salesforce) upon loading.

    Date Alignment: If the "Actual Spend vs. Budget" chart appears empty, ensure your Dim_Date table range includes the current fiscal year (2025).

    Python Scripting in PBI: Ensure your Power BI Options are set to point to your Python installation (Options and Settings > Options > Python scripting).

For any questions or issues feel free to reach me :)