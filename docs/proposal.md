# 1. Title and Author

## Project Title

**Global AI and Data Science Job Market Analysis and Salary Prediction**

Prepared for the **UMBC Master’s Program in Data Science**
Capstone Project under the supervision of **Dr. Chaojie (Jay) Wang**

Author: **Raja Vamshi Goud Amaragoni**

GitHub Repository:
[https://github.com/Vamshi267/UMBC-DATA606-Capstone](https://github.com/Vamshi267/UMBC-DATA606-Capstone)

LinkedIn Profile:
[https://www.linkedin.com/in/rajavamshi-goud-amaragoni-93a105345](https://www.linkedin.com/in/rajavamshi-goud-amaragoni-93a105345)

PowerPoint Presentation:
[To be added after presentation is created]

Project Demonstration Video:
https://youtu.be/CNcNwNXGFRY

---

# 2. Background

## Project Overview

This project analyzes the **global job market for Artificial Intelligence (AI), Machine Learning, and Data Science roles** and develops a **machine learning model to predict salaries based on job-related characteristics**.

The rapid growth of AI and data-driven technologies has significantly increased demand for skilled professionals in areas such as data science, machine learning engineering, and AI development. However, understanding salary trends and the factors influencing compensation in these fields can be difficult due to the large and scattered nature of job market information.

This project aims to address this challenge by analyzing a large dataset of AI and data science job postings and identifying patterns related to salaries, experience levels, job roles, and work arrangements.

The project has two primary objectives:

1. **Job Market Analysis** – Explore the demand for AI and data science roles and identify trends in required skills, experience levels, and job characteristics.
2. **Salary Prediction** – Build machine learning models capable of predicting expected salary based on job-related features such as job title, experience level, location, and company size.

---

## Motivation

The fields of **Artificial Intelligence, Data Science, and Machine Learning** are expanding rapidly worldwide. Students, job seekers, and professionals often want to understand:

* Which technical skills are most valuable in the job market
* What salary ranges can be expected for different roles
* How experience level affects salary
* Which job roles are most in demand globally

However, this information is often scattered across many job platforms and websites, making it difficult to analyze systematically.

This project consolidates job market data into a single dataset and uses data analysis and machine learning techniques to provide **data-driven insights into the AI and data science job market**.

The findings from this project may help:

* Students identify important skills to learn
* Job seekers understand realistic salary expectations
* Employers understand compensation trends
* Researchers study global technology job market trends

---

## Research Questions

This project aims to answer the following research questions:

1. What factors most strongly influence salaries in AI and data science jobs?
2. How do experience level, job title, and location affect salary?
3. Which technical roles appear most frequently in the AI and data science job market?
4. What job characteristics are associated with higher salaries?
5. Can machine learning models accurately predict salary based on job-related features?

---

# 3. Data

To address the research questions, this project uses a **real-world dataset containing global job postings for AI and Data Science roles**.

---

## Dataset Source

The primary dataset used in this project is **jobs_dataset.csv**, which contains structured information about AI and data science job postings, including salary ranges and job characteristics.

---

## Purpose of the Dataset

This dataset is used for two main purposes:

1. **Exploratory Analysis of the Job Market**

   * Understanding salary distributions
   * Identifying relationships between job features and compensation
   * Exploring demand for different job roles and experience levels

2. **Machine Learning Salary Prediction**

   * Building models to estimate salary based on job characteristics

---

## Dataset Size

* File format: CSV
* File size: approximately **5 MB**
* Number of rows: approximately **50,000 job postings**
* Number of columns: **14 variables**

---

## Time Period

The dataset includes job postings primarily from **2021 to 2024**.

The column **posted_year** indicates the year in which each job posting was listed.

---

## Data Representation

Each row in the dataset represents **a single AI or data science job posting**.

Each column represents a specific attribute describing the job, such as job title, location, experience requirements, and salary range.

---

## Data Dictionary

| Column Name          | Data Type | Description                          | Example Values              |
| -------------------- | --------- | ------------------------------------ | --------------------------- |
| job_title            | string    | Job title of the position            | Data Scientist, ML Engineer |
| country              | string    | Country where the job is located     | USA, India, UK              |
| city                 | string    | City of the job location             | New York, London            |
| experience_level     | string    | Required experience level            | Entry, Mid, Senior          |
| min_experience_years | integer   | Minimum years of experience required | 0–15                        |
| remote_type          | string    | Work arrangement                     | Remote, Hybrid, Onsite      |
| company_size         | string    | Size of the company                  | Small, Medium, Large        |
| salary_min_usd       | numeric   | Minimum salary offered               | Numeric                     |
| salary_max_usd       | numeric   | Maximum salary offered               | Numeric                     |
| posted_year          | integer   | Year the job was posted              | 2021–2024                   |

---

## Target Variable for Machine Learning

The dataset provides a salary range rather than a single salary value. Specifically, it includes:

* **salary_min_usd**
* **salary_max_usd**

To create a suitable target variable for machine learning, an estimated salary value was calculated as the average of these two values:

```
salary_avg_usd = (salary_min_usd + salary_max_usd) / 2
```

This new variable, **salary_avg_usd**, serves as the target variable for the salary prediction models.

---

## Features Used for Modeling

The following features were selected as potential predictors for the machine learning models:

* job_title
* country
* experience_level
* min_experience_years
* remote_type
* company_size
* posted_year

These variables capture key aspects of job characteristics that may influence salary levels.

---

# 4. Exploratory Data Analysis (EDA)

Exploratory Data Analysis (EDA) was conducted to understand the structure and characteristics of the dataset and to examine the relationships between selected job attributes and the target variable **salary_avg_usd**. The primary goal of this analysis was to explore patterns in the data, identify potential relationships between variables, and confirm that the dataset was suitable for machine learning modeling.

The analysis focused only on the variables selected for modeling. Columns that were not relevant to the prediction task were removed in order to simplify the dataset and improve computational efficiency.

---

## Data Cleansing

The dataset was examined for common data quality issues, including missing values and duplicate records.

The following checks were performed:

* Detection of missing values across all selected variables
* Verification of duplicate rows
* Inspection of data types for consistency

The analysis indicated that there were **no missing values or duplicate rows in the selected features**. As a result, no additional data cleaning steps such as imputation or record removal were required.

Ensuring that the dataset is clean and consistent is an important step before performing statistical analysis or training machine learning models.

---

## Summary Statistics

Summary statistics were calculated to examine the distribution and variability of the numerical variables in the dataset, particularly salary and years of experience.

These statistics include:

* mean salary
* median salary
* minimum and maximum values
* standard deviation

The summary statistics provided an initial understanding of the salary range and the variation across job postings. This step also helped identify whether extreme values or unusual distributions were present in the dataset.

---

## Visual Analysis

Several visualizations were created using **Plotly Express** to explore relationships between the target variable and the selected features. Visual analysis helps identify patterns, trends, and potential correlations in the data.

The following visualizations were produced:

### Salary Distribution

A histogram of **salary_avg_usd** was created to examine the distribution of salaries in the dataset. This visualization helps identify the general salary range and the presence of any skewness or outliers.

<img width="1351" height="438" alt="Screenshot (122)" src="https://github.com/user-attachments/assets/e27f1ca7-8c03-4634-b16f-957b6bba1a96" />

---

### Salary by Experience Level

A comparison of salaries across different **experience levels** was performed using box plots. This visualization helps illustrate how salary changes with increasing experience.

<img width="1348" height="428" alt="Screenshot (125)" src="https://github.com/user-attachments/assets/7cc84041-ae39-4016-9be7-cdcd3b6bbc00" />

---

### Salary by Work Arrangement

A visualization was created to compare salaries across different work arrangements such as **remote, hybrid, and onsite positions**. This helps evaluate whether remote work influences salary levels.

---

### Relationship Between Experience and Salary

A scatter plot was used to analyze the relationship between **minimum experience years** and **salary_avg_usd**. This visualization helps identify whether salary tends to increase with additional experience.

---

### Frequency of Job Titles

A bar chart was created to examine the frequency distribution of job titles in the dataset. This helps identify the most common roles included in the data.

<img width="1351" height="426" alt="Screenshot (124)" src="https://github.com/user-attachments/assets/8c52af9c-5d56-4455-8c15-359fd93079a1" />

---

## Dataset Structure

The dataset follows a **tidy data structure**, where:

* each row represents a single job posting
* each column represents a specific attribute of that job

This structured format makes the dataset suitable for statistical analysis, visualization, and machine learning modeling.

---

## Outcome of the Exploratory Data Analysis

The exploratory analysis confirmed that the dataset is clean, well structured, and suitable for predictive modeling. The relationships observed between salary and job-related attributes such as experience level, job role, and work arrangement suggest that these features are informative predictors of salary.

The insights obtained during EDA guided the selection of relevant features for the machine learning models. The prepared dataset was then used for training and evaluating multiple predictive models to estimate salary based on job characteristics.

---

# Summary

In this project:

* **Dataset (jobs_dataset.csv)** is used for machine learning and salary prediction and is used for understanding job market trends and skill demand.

This dataset provide a strong foundation for answering the research questions and completing the objectives of the capstone project.
