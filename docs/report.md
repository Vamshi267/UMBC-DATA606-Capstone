# **1. Title and Author**

## **Project Title**

**Global AI & Data Science Salary Prediction Using Machine Learning**

**Prepared for UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang**

**Author Name:** Raja Vamshi Goud Amaragoni

**GitHub Repository:** https://github.com/Vamshi267/UMBC-DATA606-Capstone/tree/master

**LinkedIn Profile:** https://www.linkedin.com/in/rajavamshi-goud-amaragoni-93a105345

**PowerPoint Presentation:** *To be added*

**YouTube Video:** *To be added*

---

# **2. Background**

The demand for professionals in Artificial Intelligence (AI) and Data Science has grown significantly over the past decade. As organizations across industries adopt data-driven strategies, the need for skilled professionals has increased, leading to a wide variation in salaries across roles, locations, and experience levels.

Salary estimation in this domain is a complex problem because compensation is influenced by multiple interacting factors such as job role, years of experience, geographic location, company size, industry, and work type (remote, hybrid, or onsite). Traditional methods of estimating salaries rely on manual judgment or limited historical data, which often results in inconsistent and subjective outcomes.

A machine learning-based approach provides a systematic and scalable way to analyze large volumes of job data and identify patterns that influence salary. By leveraging historical job postings, predictive models can estimate expected salaries for new job configurations with a high degree of accuracy.

This project aims to build a salary prediction model using machine learning techniques to provide reliable salary estimates for AI and Data Science roles.

## **Why it matters**

* Provides **objective salary benchmarking** for job seekers and employers
* Helps organizations design **competitive compensation strategies**
* Supports **data-driven decision-making** in recruitment
* Enables analysis of **global job market trends**
* Reduces reliance on subjective estimation methods

## **Research Questions**

* Can machine learning models accurately predict salaries for AI and Data Science jobs?
* Which regression model performs best on this dataset?
* What are the most influential features affecting salary?
* Does hyperparameter tuning significantly improve model performance?

---

# **3. Data**

## **Data Source**

The dataset used in this project was obtained from **Kaggle**. It contains structured job-related data for AI and Data Science roles across multiple countries.

## **Data Size**

* Approximate file size: **~5 MB**
* In-memory size observed during processing: ~5.3 MB

## **Data Shape**

* **50,000 rows** (job records)
* **14 columns** (features)

## **Time Period**

* The dataset includes job postings from approximately **2021 to 2024**, as indicated by the `posted_year` column.

## **Unit of Observation**

Each row represents a **single job posting** with associated attributes such as job role, experience level, salary range, and location.

---

## **Data Dictionary**

| Column Name          | Data Type | Definition                | Potential Values                     |
| -------------------- | --------- | ------------------------- | ------------------------------------ |
| job_id               | object    | Unique identifier for job | Alphanumeric                         |
| job_title            | object    | Job role title            | Data Scientist, ML Engineer, Analyst |
| company_type         | object    | Type of company           | Startup, Enterprise                  |
| industry             | object    | Industry category         | Tech, Finance, Healthcare            |
| country              | object    | Job location country      | USA, India, UK, etc.                 |
| city                 | object    | Job location city         | Various                              |
| remote_type          | object    | Work type                 | Remote, Hybrid, Onsite               |
| experience_level     | object    | Experience category       | Entry, Mid, Senior                   |
| min_experience_years | int       | Required experience       | Numeric                              |
| salary_min_usd       | int       | Minimum salary            | Numeric                              |
| salary_max_usd       | int       | Maximum salary            | Numeric                              |
| employment_type      | object    | Job type                  | Full-time, Contract                  |
| posted_year          | int       | Year of posting           | 2020–2024                            |
| company_size         | object    | Company size              | Small, Medium, Large                 |

---

## **Target Variable**

A new target variable was created:

**salary_avg_usd = (salary_min_usd + salary_max_usd) / 2**

This transformation converts the salary range into a single continuous value suitable for regression modeling.

---

## **Selected Features**

The following variables were selected as predictors:

* job_title
* country
* experience_level
* min_experience_years
* remote_type
* company_size
* posted_year

These features were chosen because they are directly related to salary determination.

---

# **4. Exploratory Data Analysis (EDA)**

Exploratory Data Analysis (EDA) was conducted using Jupyter Notebook to understand the dataset, identify patterns, and prepare the data for modeling.

## **Initial Data Exploration**

* Inspected dataset structure and column types
* Generated summary statistics for numerical variables
* Analyzed distributions of categorical variables

## **Data Quality Assessment**

* **Missing values:** None detected
* **Duplicate rows:** None detected
* Dataset is clean and requires minimal preprocessing

## **Feature Engineering**

* Created target variable `salary_avg_usd`
* Removed unnecessary columns
* Focused on relevant predictors

## **Data Transformation**

* Converted categorical variables using **one-hot encoding**
* Ensured all features are numeric for model compatibility


* ## Visual Analysis

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

## **Key Insights**

* Experience level is strongly correlated with salary
* Years of experience significantly influence salary
* Location and remote work type also contribute to variation
* Salary distribution is wide but follows identifiable patterns

## **Data Structure**

The dataset is **tidy**:

* Each row represents one job
* Each column represents a feature
* Target variable is clearly defined

---

# **5. Model Training**

## **Models Implemented**

### **Linear Regression**

A baseline model that assumes a linear relationship between features and salary. It is simple, interpretable, and computationally efficient.

### **Random Forest Regressor**

An ensemble model that builds multiple decision trees and combines their predictions. It captures non-linear relationships and reduces overfitting.

### **Gradient Boosting Regressor**

A sequential ensemble model that improves predictions by correcting previous errors. It is highly effective for structured datasets.

---

## **Training Process**

* Train-test split: **80% / 20%**
* Training data: 40,000 records
* Testing data: 10,000 records
* One-hot encoding applied to categorical variables

---

## **Libraries Used**

* pandas
* numpy
* plotly
* scikit-learn
* joblib

---

## **Evaluation Metrics**

### **MAE**

Measures average prediction error in USD.
<img width="1378" height="449" alt="Mean Absolute Error" src="https://github.com/user-attachments/assets/e04a6e49-3523-4235-a922-e773b243305d" />


### **RMSE**

Penalizes larger errors more heavily.
<img width="1366" height="463" alt="RMSE" src="https://github.com/user-attachments/assets/e4b37797-34ed-49c8-8531-b35c3ed87820" />


### **R² Score**

Measures how well the model explains variance.
<img width="1374" height="496" alt="R2 score" src="https://github.com/user-attachments/assets/572259a4-10fa-46fa-8322-4fd8ae3a8f45" />


---

## **Model Performance**

| Model             | MAE  | RMSE | R²     |
| ----------------- | ---- | ---- | ------ |
| Linear Regression | 3522 | 4222 | 0.9869 |
| Random Forest     | 3786 | 4592 | 0.9846 |
| Gradient Boosting | 3522 | 4222 | 0.9869 |

---

## **Model Selection**

Gradient Boosting was selected because:

* Captures complex feature interactions
* Handles non-linear relationships
* Provides stable and high accuracy
* Suitable for structured tabular data

---

## **Hyperparameter Tuning**

Performed using **GridSearchCV**

Best parameters:

* n_estimators = 200
* learning_rate = 0.05
* max_depth = 3

Performance improvement was minimal, indicating the model was already near optimal.

---

## **Feature Importance**

Most important predictors:

* Senior experience level
* Years of experience
* Mid-level experience

---

---

## **Residual Analysis**

Residual analysis is the process of examining the errors (residuals) of a model, where a residual is the difference between the actual value and the predicted values.
<img width="1348" height="450" alt="Residual Analysis" src="https://github.com/user-attachments/assets/f8c363e2-541a-47a7-8ca2-b26aa7d15353" />

---

# **6. Application of the Trained Models**

A **Streamlit web application** was developed to make the model interactive.

## **Application Functionality**

* Users input job details
* Model predicts salary in real-time
* Simple and user-friendly interface

## **Workflow**

1. User inputs features
2. Data is preprocessed
3. Model generates prediction
4. Result is displayed

---

## **User Interface**

<img width="1812" height="945" alt="Screenshot (158)" src="https://github.com/user-attachments/assets/fffd31df-bd08-4e86-935a-325a4d00583b" />

<img width="1895" height="996" alt="Screenshot (159)" src="https://github.com/user-attachments/assets/6b08fd01-4573-4a90-973e-c2cd835ec80d" />

---

## **Tools Used**

* Streamlit
* Joblib

---

# **7. Conclusion**

This project successfully developed a machine learning model to predict salaries for AI and Data Science roles.

Gradient Boosting achieved the best performance with high accuracy and stability. The analysis showed that experience level and years of experience are the most significant factors influencing salary.

## **Applications**

* Salary benchmarking
* Job market insights
* Hiring decisions

## **Limitations**

* Limited feature set
* No external data integration
* No bias analysis

## **Lessons Learned**

* Data quality is critical
* Feature engineering improves performance
* Complex models do not always outperform simple ones

## **Future Work**

* Add more features (skills, education)
* Use advanced models
* Improve generalization
* Deploy production system

---

# **8. References**

* Matbouli, Y.T., & Alghamdi, S.M. (2022). Statistical machine learning regression models for salary prediction. *Information, 13*(10), 495. [https://doi.org/10.3390/info13100495](https://doi.org/10.3390/info13100495)

* Gheriyani, N.S., & Dbeea, J.I. (2024). Salary prediction: Case study. *African Journal of Advanced Pure and Applied Sciences*. [https://doi.org/10.65418/ajapas.vi.766](https://doi.org/10.65418/ajapas.vi.766)

* Raj, P., et al. (2025). Forecasting salary using machine learning. *Atlantis Press*.

* Ayua, S.I. (2024). Salary prediction model using regression techniques.

* Alsheyab, A.R., et al. (2025). Job market salary prediction using ML. *arXiv*.

---
