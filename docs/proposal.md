# 1. Title and Author

### **Project Title**

**Global AI and Data Science Job Market Analysis and Salary Prediction**

Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang

**Author Name:**
Raja Vamshi Goud Amaragoni

**GitHub Repository Link:**
https://github.com/Vamshi267/UMBC-DATA606-Capstone

**LinkedIn Profile Link:**
https://www.linkedin.com/in/rajavamshi-goud-amaragoni-93a105345

**PowerPoint Presentation Link:**
[To be added after presentation is created]

**YouTube Video Link:**
[To be added after project demo video is recorded]

---

# 2. Background

### What is it about?

This project is about analyzing the global job market for Artificial Intelligence, Data Science, and related technology roles, and building a machine learning system to predict salaries based on job-related factors.

The project has two main goals:

1. To understand current job market trends in AI and Data Science by analyzing the demand for different skills and technologies.
2. To build a predictive model that can estimate the expected salary of a job based on features such as job title, experience level, location, and company size.

---

### Why does it matter?

The fields of AI, Data Science, and Machine Learning are growing very fast across the world. Many students and professionals want to enter these fields, but it is often difficult to understand:

* Which skills are most important to learn
* What salary they can expect
* How experience affects pay
* Which job roles are in high demand

Information about jobs and salaries is usually scattered across many websites. This project matters because it brings real job market data together and provides data-driven answers to these important questions.

The project can help:

* Students choose the right skills to learn
* Job seekers understand realistic salary expectations
* Employers understand market trends
* Anyone interested in AI/Data Science careers

---

### Research Questions

1. What factors most influence salaries in AI and Data Science jobs?
2. How do experience level, job title, and location affect salary?
3. Which technical skills are most in demand globally?
4. What are the most popular skill categories in the AI job market?
5. Can machine learning models accurately predict salary based on job-related features?

---

# 3. Data

To answer the research questions, two real-world datasets are used in this project. Each dataset is used for a specific purpose.

---

## Dataset A – Salary Prediction Dataset

### Data Source

The first dataset used in this project is **jobs_dataset.csv**, a structured dataset containing global AI and Data Science job information with salary details.

### Purpose of This Dataset

This dataset is used for:

* Salary prediction using machine learning
* Analyzing factors that affect compensation
* Understanding salary differences across roles and locations

---

### Data Size

* File size: Approximately **5 MB**
* Format: CSV file

---

### Data Shape

* Number of rows: **50,000**
* Number of columns: **14**

---

### Time Period

* The data contains job postings from recent years (primarily from 2021–2024).
* The column **posted_year** provides the time information for each job record.

---

### What Does Each Row Represent?

Each row in this dataset represents:

 **One AI/Data Science related job posting with salary information**

---

### Data Dictionary

| Column Name          | Data Type | Definition                           | Potential Values                               |
| -------------------- | --------- | ------------------------------------ | ---------------------------------------------- |
| job_title            | string    | Title of the job position            | Data Scientist, ML Engineer, AI Engineer, etc. |
| country              | string    | Country where the job is located     | USA, India, UK, etc.                           |
| city                 | string    | City of job location                 | New York, London, etc.                         |
| experience_level     | string    | Level of experience required         | Entry, Mid, Senior                             |
| min_experience_years | integer   | Minimum years of experience required | 0–15                                           |
| remote_type          | string    | Type of work                         | Remote, Hybrid, Onsite                         |
| company_size         | string    | Size of the company                  | Small, Medium, Large                           |
| salary_min_usd       | numeric   | Minimum salary in USD                | Numeric value                                  |
| salary_max_usd       | numeric   | Maximum salary in USD                | Numeric value                                  |
| posted_year          | integer   | Year the job was posted              | 2021, 2022, 2023                               |

---

### Target Variable for Machine Learning

This dataset does not have a single salary column, but it contains:

* salary_min_usd
* salary_max_usd

To create a proper label for machine learning, the following target variable will be calculated:

**salary_avg_usd = (salary_min_usd + salary_max_usd) / 2**

This calculated column will be the **target/label variable** for salary prediction.

---

### Features / Predictors for ML Models

The following columns may be selected as input features for the machine learning models:

* job_title
* country
* experience_level
* min_experience_years
* remote_type
* company_size
* posted_year

These features will be used to predict the target variable **salary_avg_usd**.

---

# 4. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was conducted to understand the characteristics of the dataset and examine relationships between the selected features and the target variable **salary_avg_usd**. The analysis focused on the variables chosen for modeling, and unnecessary columns were removed to simplify the dataset.

## Data Preparation

A new target variable, **salary_avg_usd**, was created by calculating the average of the minimum and maximum salary values provided in the dataset. This variable represents the estimated salary for each job posting and was used as the prediction target for the machine learning models.

Only the relevant variables used for modeling were retained, including job title, country, experience level, minimum experience years, remote work type, company size, posted year, and the target variable.

## Data Cleansing

The dataset was examined for common data quality issues. No missing values or duplicate rows were found in the selected variables. Therefore, no additional data cleaning steps were required.

## Summary Statistics

Summary statistics were generated to examine the distribution and variability of the numerical variables, particularly salary and experience. These statistics provided an initial understanding of salary ranges and variation across job postings.

## Visual Analysis

Visualizations were created using **Plotly Express** to explore relationships between salary and the selected features. The analysis included:

* distribution of the target variable (salary)
* comparison of salaries across experience levels
* comparison of salaries by work arrangement (remote, hybrid, onsite)
* relationship between years of experience and salary
* frequency of job titles within the dataset

These visualizations helped identify patterns and potential relationships between job characteristics and salary.

## Dataset Structure

The dataset follows a tidy structure in which each row represents a single job posting and each column represents a specific attribute of that job. This structure makes the dataset suitable for statistical analysis and machine learning modeling.

## Outcome of EDA

The exploratory analysis confirmed that the dataset is clean and well structured. The relationships observed between salary and job characteristics indicate that the selected features are relevant for predicting salary. The prepared dataset was then used for training and evaluating machine learning models.

---

# Summary

In this project:

* **Dataset A (jobs_dataset.csv)** is used for machine learning and salary prediction and is used for understanding job market trends and skill demand.

Together, these datasets provide a strong foundation for answering the research questions and completing the objectives of the capstone project.
