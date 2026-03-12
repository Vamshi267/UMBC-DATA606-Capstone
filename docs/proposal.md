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

## Dataset

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

Your section is already good, but for grading purposes it should be **more structured, clearer, and slightly more detailed**. Professors usually expect:

* clear subsections
* explanation of process
* description of visualizations
* interpretation of results

I rewrote your section while **keeping your ideas but improving clarity, structure, and academic tone**.

---

# 4. Exploratory Data Analysis (EDA)

Exploratory Data Analysis (EDA) was conducted to understand the structure and characteristics of the dataset and to examine the relationships between selected job attributes and the target variable **salary_avg_usd**. The primary goal of this analysis was to explore patterns in the data, identify potential relationships between variables, and confirm that the dataset was suitable for machine learning modeling.

The analysis focused only on the variables selected for modeling. Columns that were not relevant to the prediction task were removed in order to simplify the dataset and improve computational efficiency.

---

## Data Preparation

A new target variable, **salary_avg_usd**, was created to represent the estimated salary associated with each job posting. This variable was calculated by taking the average of the minimum salary and maximum salary values provided in the dataset.

The following formula was used:

```
salary_avg_usd = (salary_min_usd + salary_max_usd) / 2
```

This derived variable was used as the prediction target for the machine learning models.

After creating the target variable, only the relevant features required for modeling were retained. These include:

* job_title
* company_location (country)
* experience_level
* minimum_experience_years
* remote_ratio / work arrangement
* company_size
* posted_year
* salary_avg_usd (target variable)

Reducing the dataset to these variables helped simplify the analysis and ensured that only meaningful features were included in the modeling process.

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

* **Dataset A (jobs_dataset.csv)** is used for machine learning and salary prediction and is used for understanding job market trends and skill demand.

Together, these datasets provide a strong foundation for answering the research questions and completing the objectives of the capstone project.
