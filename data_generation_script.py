import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. mock ORACLE EBS DATA (Transactional Actuals)
# Granular, daily, specific account codes
ebs_rows = 1000
ebs_data = {
    'Transaction_ID': range(1001, 1001 + ebs_rows),
    'GL_Date': [datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(ebs_rows)],
    'Account_Code': np.random.choice(['5100-Payroll', '5200-Travel', '5300-Software', '5400-Hardware'], ebs_rows),
    'Entity': np.random.choice(['US_HQ', 'Costa_Rica_Nearshore'], ebs_rows, p=[0.4, 0.6]),
    'Project_ID': np.random.choice(['PRJ-001', 'PRJ-002', 'PRJ-003', 'PRJ-004'], ebs_rows),
    'Amount_USD': np.random.uniform(500, 5000, ebs_rows).round(2),
    'Vendor': np.random.choice(['GlobalTalent IT', 'Azure Cloud', 'Delta Air', 'Local Payroll Corp'], ebs_rows)
}
df_ebs = pd.DataFrame(ebs_data)

# 2. mock HYPERION DATA (Budget/EPM)
# Multidimensional, usually monthly, and often "wide" format
departments = ['Engineering', 'Sales', 'Operations']
categories = ['5100-Payroll', '5200-Travel', '5300-Software', '5400-Hardware']
hyperion_rows = []

for dept in departments:
    for cat in categories:
        hyperion_rows.append({
            'Department': dept,
            'Account_Code': cat,
            'Scenario': 'FY2025_Budget',
            'Jan': np.random.randint(20000, 30000),
            'Feb': np.random.randint(20000, 30000),
            'Mar': np.random.randint(20000, 30000),
            'Apr': np.random.randint(20000, 30000),
            'May': np.random.randint(20000, 30000),
            'Jun': np.random.randint(20000, 30000)
        })
df_hyperion = pd.DataFrame(hyperion_rows)

# 3. mock SALESFORCE DATA (CRM)
# Project-based info
sf_data = {
    'Project_ID': ['PRJ-001', 'PRJ-002', 'PRJ-003', 'PRJ-004'],
    'Client_Name': ['TechCorp', 'DataFin', 'HealthSys', 'EcoPower'],
    'Contract_Value': [500000, 750000, 300000, 1200000],
    'Project_Status': ['Active', 'Active', 'On Hold', 'Active'],
    'Nearshore_Lead': ['Carlos M.', 'Elena R.', 'Carlos M.', 'Sofia Q.']
}
df_sf = pd.DataFrame(sf_data)

# Save to CSV
df_ebs.to_csv('Oracle_EBS_Actuals.csv', index=False)
df_hyperion.to_csv('Hyperion_Budget.csv', index=False)
df_sf.to_csv('Salesforce_Projects.csv', index=False)

print("Files generated: Oracle_EBS_Actuals.csv, Hyperion_Budget.csv, Salesforce_Projects.csv")