Enterprise BI Integration: ERP, CRM, and EPM Performance Tracker
📌 Project Overview

This project demonstrates a simple Business Intelligence Flow by integrating data from three core enterprise systems to analyze the profitability and operational efficiency of a Nearshore IT Staffing model.

The dashboard bridges the gap between sales targets, actual expenditures, and financial planning to provide a unified "Source of Truth" for executive decision-making.

🏗️ The Data Architecture (BI Flow)

The model utilizes a Star Schema to consolidate three disparate data sources:

    Oracle EBS (ERP): Transactional "Actuals" (Payroll, Hardware, Travel expenses).

    Salesforce (CRM): Project metadata, Client names, and Contract values.

    Hyperion (EPM): Multidimensional budget targets and financial forecasts.

🚀 Key Features & Analytics

    Budget Variance Analysis: A Waterfall visualization that identifies exactly which expense categories (from EBS) are deviating from the financial plan (from Hyperion).

    Project Profitability Matrix: A scatterplot correlating Salesforce contract values against actual operational delivery costs to identify "High-Value" vs. "High-Cost" accounts.

    Nearshore Efficiency Ratio: Custom DAX measures calculating the ROI and cost-savings of the nearshore delivery center compared to US-HQ costs.

    Time-Intelligence: Unified calendar dimensions to align daily transactional data with monthly/quarterly financial buckets.

🛠️ Technical Stack

    Power BI: Data modeling, DAX, and Visualization.

    Power Query (M): Data transformation, unpivoting EPM cubes, and schema normalization.

    Python: Used for generating synthetic enterprise-grade datasets mimicking Oracle and Salesforce schemas.

    DAX: Advanced measures for Variance %, Running Totals, and Cross-filtered KPIs.

📈 Business Interpretation

By integrating these flows, the dashboard answers critical business questions:

    "Are we profitable?" (Contract Value vs. Actual Cost).

    "Where is the leak?" (Budget vs. Actual Variance by Category).

    "Is the Nearshore model working?" (Comparative cost analysis between entities).
    
