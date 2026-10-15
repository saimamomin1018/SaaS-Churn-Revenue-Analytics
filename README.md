# 📊 SaaS Subscription, Customer Churn & Revenue Analytics

### 🚀 End-to-End Data Analytics Project Using Excel, Python, SQL, PostgreSQL & Power BI

Welcome to my **SaaS Subscription, Customer Churn & Revenue Analytics** project! 👋

This project focuses on analyzing subscription data to understand customer churn, recurring revenue, product feature usage, and customer support performance. It demonstrates how multiple data analytics tools can be used to clean, analyze, validate, and visualize data to support business decision-making.

---

## 📌 1. Project Overview

Software as a Service (SaaS) companies provide software to customers through subscription-based plans. Understanding subscription performance, customer retention, recurring revenue, and customer support is important for sustainable business growth.

The goal of this project is to explore SaaS business data, identify descriptive patterns, answer business questions, and present insights through interactive Power BI dashboards.

**Project type:** End-to-end data analytics  
**Domain:** SaaS, Subscription Analytics & Customer Success  
**Approach:** Descriptive analytics and business intelligence

---

## 🎯 2. Project Objectives

- 📈 Analyze subscription and recurring revenue patterns.
- 👥 Understand customer accounts and subscription records.
- 🔄 Examine customer and subscription churn.
- 💰 Analyze Monthly Recurring Revenue (MRR) and Annual Recurring Revenue (ARR).
- 🧩 Explore product feature usage and error patterns.
- 🎧 Analyze support tickets, response times, resolution times, satisfaction, and escalations.
- 📊 Build interactive Power BI reports for business users.
- ✅ Validate key metrics across the analysis tools.

---

## 🛠️ 3. Tools & Technologies

| Tool | Purpose |
|---|---|
| 📗 Microsoft Excel | Spreadsheet analysis, summaries, and data presentation |
| 🐍 Python | Data inspection, cleaning, validation, and exploratory data analysis |
| 🧮 Pandas & NumPy | Data manipulation and numerical analysis |
| 📊 Matplotlib & Seaborn | Data visualization |
| 🐘 PostgreSQL | Relational database storage |
| 💻 SQL | Data querying and business analysis |
| 📈 Power BI | Data modeling, DAX measures, interactive reports, and dashboards |
| 🧑‍💻 VS Code | Python development and project organization |
| 🌐 GitHub | Version control and project portfolio |

---

## 🗂️ 4. Dataset Description

The project uses the RavenStack SaaS Subscription & Churn Analytics dataset, organized into five CSV datasets.

| Dataset | Description |
|---|---|
| 🏢 Accounts | Account information, industry, country, plan tier, seats, and account-level churn indicators |
| 📝 Subscriptions | Subscription records, dates, plan tiers, MRR, ARR, billing frequency, and subscription events |
| 🧩 Feature Usage | Feature activity, usage counts, usage duration, and error counts |
| 🎧 Support Tickets | Ticket priority, response time, resolution time, satisfaction, and escalation indicators |
| 🔄 Churn Events | Recorded churn dates, reason codes, refund amounts, and related event information |

**Important data-grain note:** An account represents a customer organization, while a subscription represents a subscription record. One account may have multiple subscription records. Therefore, account counts and subscription counts are not interchangeable.

---

## 🔄 5. Project Workflow

The project follows a multi-tool analytics workflow with a common cleaned-data source.

1. 🏁 **Project Setup:** Organize the project folders and development environment.
2. 🔍 **Dataset Understanding:** Inspect the source files, columns, data types, and data quality.
3. 🧹 **Python Data Cleaning:** Clean and validate the raw CSV files.
4. 📗 **Excel Analysis:** Independently use the cleaned CSV files for spreadsheet analysis.
5. 🐘 **PostgreSQL & SQL:** Load the cleaned CSV files into PostgreSQL tables and perform SQL-based analysis.
6. 🐍 **Python EDA:** Independently reuse the cleaned CSV files for exploratory and descriptive analysis.
7. 📊 **Power BI:** Load the cleaned CSV files, prepare the data model, create DAX measures, and build reports.
8. ✅ **Final Validation:** Review key metrics, report visuals, and interactive slicers.

The cleaned CSV files are reused independently across Excel, PostgreSQL/SQL, Python, and Power BI.

---

## 📊 6. Power BI Dashboard Pages

The Power BI report contains five analytical pages:

### 📌 Page 1 — Executive Overview
Provides a high-level view of subscription performance, revenue, and churn through KPI cards and summary visuals.

![Executive Overview](./01-executive-overview.png)

### 👥 Page 2 — Customer Success & Churn
Explores customer churn patterns, recorded churn reasons, and relevant customer success indicators.

![Customer Success & Churn](./02-customer-success-churn.png)

### 💰 Page 3 — Revenue & Subscription Analysis
Examines MRR, ARR, plan-tier contributions, billing frequency, and subscription patterns.

![Revenue & Subscription Analysis](./03-revenue-subscription-analysis.png)

### 🧩 Page 4 — Feature Usage Analysis
Explores feature activity, usage volume, usage duration, and recorded errors.

![Feature Usage Analysis](./04-feature-usage-analysis.png)

### 🎧 Page 5 — Support & Customer Success
Reviews support ticket patterns, satisfaction scores, response and resolution times, and escalations.

![Support & Customer Success](./05-support-customer-success.png)

Interactive slicers allow users to explore the available data by relevant categories and dates.

---

## 💡 7. Business Questions

This project investigates questions such as:

- 📉 What customer and subscription churn patterns appear in the data?
- 💵 How is recurring revenue distributed across subscription plans?
- 🔄 Which churn reasons are recorded most frequently?
- 🧩 How do feature usage and error patterns differ across records?
- 🎧 What patterns appear in support response times, resolution times, satisfaction, and escalations?
- 📊 How can interactive reports help business stakeholders explore these patterns?

The analysis is descriptive. Observed relationships do not, by themselves, establish causation.

---

## ✅ 8. Data Validation & Quality Checks

Validation is an important part of the analytics workflow.

- 🔍 Inspect source data and column types.
- 🧹 Review cleaning operations and data-quality issues.
- 🔗 Check relationships and data grain.
- 🧮 Compare selected metrics across tools where definitions and filters match.
- 📊 Review dashboard visuals and KPI calculations.
- 🎛️ Test report slicers and interactions.

Final KPI values and conclusions should be interpreted using the actual project files and validated outputs.

---

## 📁 9. Repository Structure

The repository is organized into folders for data, analysis, reporting, and documentation. The exact folder names reflect the files included in the uploaded project.

Typical components include:

- 📂 Data — raw and cleaned CSV datasets
- 📂 Excel — spreadsheet analysis
- 📂 Python — data cleaning and exploratory analysis scripts
- 📂 PostgreSQL — database setup 
- 📂 SQL — analysis queries and kpi
- 📂 Power BI — report and dashboard files

---

## 🎓 10. Key Learning Outcomes

Through this project, I practiced:

- 🧹 Data cleaning and data-quality validation
- 🐍 Python-based data analysis
- 🧮 SQL querying and relational database concepts
- 📗 Spreadsheet-based analysis
- 📊 Power BI data modeling and DAX
- 📈 Business KPI interpretation and visualization
- 📝 Technical documentation and project presentation
- 🔍 Cross-tool validation and analytical reasoning

---

## ⚠️ 11. Project Scope

This project focuses on **descriptive analytics and business intelligence**. It does not implement a machine-learning churn prediction model.

Business recommendations should be based on validated analytical findings and interpreted within the limitations of the available data.

---

## 👩‍💻 12. About This Project

This project was developed as an academic and portfolio project to demonstrate practical data analytics skills across Excel, Python, SQL, PostgreSQL, and Power BI.

Thank you for visiting my repository! ⭐

If you find this project useful, feel free to explore the files and dashboards.
