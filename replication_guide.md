🚀 Quick Replication Guide

To recreate this environment on your local machine, follow these steps:
Step 1: Generate the Synthetic Data

Ensure you have Python installed, then run the provided script to generate the CSV files mimicking the ERP, CRM, and EPM exports.

Bash: python data_generation_script.py

This will create three files: Oracle_EBS_Actuals.csv, Hyperion_Budget.csv, and Salesforce_Projects.csv.
Step 2: Open the Power BI Template

    Open the Nearshore_Profitability_Report.pbit file.

    Power BI will prompt you for the File Path of the three CSVs generated in Step 1.

    Once the paths are entered, the model will automatically populate the visuals, DAX measures, and relationships.

Step 3: Verify the BI Flow

    Go to the Model View to confirm the Star Schema is active.

    Verify that the Dim_Date and Dim_Account tables have correctly bridged the daily EBS data with the monthly Hyperion targets.