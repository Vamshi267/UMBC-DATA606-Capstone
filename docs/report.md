# **1. Title and Author**

## **Project Title**

**Global AI & Data Science Salary Prediction Using Machine Learning**

**Prepared for UMBC Data Science Master Degree Capstone Project(Data 606) by Dr. Chaojie (Jay) Wang**

**Author Name:** Raja Vamshi Goud Amaragoni

**GitHub Repository:** https://github.com/Vamshi267/UMBC-DATA606-Capstone/tree/master

**LinkedIn Profile:** https://www.linkedin.com/in/rajavamshi-goud-amaragoni-93a105345

**PowerPoint Presentation:** https://github.com/Vamshi267/UMBC-DATA606-Capstone/blob/master/docs/Presentation.pptx

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

Linear Regression was used as the baseline model for this project. It assumes that the relationship between the input features and the target variable follows a linear pattern. The model estimates coefficients for each predictor and uses them to calculate the expected salary value. Linear Regression is widely used because it is simple, fast to train, easy to interpret, and provides a strong benchmark for comparison with more advanced algorithms.

### **Random Forest Regressor**

Random Forest Regressor is an ensemble learning method that combines the predictions of multiple decision trees. Each tree is trained on a random subset of the data and features, and the final prediction is obtained by averaging all trees. This approach reduces overfitting, improves generalization, and captures non-linear relationships between variables. It is especially useful when feature interactions are complex and not purely linear.

### **Gradient Boosting Regressor**

Gradient Boosting Regressor is a sequential ensemble model that builds weak learners one after another, where each new model focuses on correcting the errors made by the previous model. Instead of averaging independent trees, it gradually improves performance through iterative learning. This algorithm is highly effective for structured tabular datasets and often provides strong predictive accuracy when properly tuned.

---

## **Training Process**

The dataset was prepared and divided into two subsets to evaluate the model fairly on unseen data.

* **Train-Test Split:** 80% / 20%  
* **Training Data:** 40,000 records used to train the models  
* **Testing Data:** 10,000 records used to evaluate final performance  
* **Encoding:** One-hot encoding was applied to categorical variables such as job title, country, experience level, remote type, and company size.

This process ensures that the models learn patterns from historical data while being tested on separate records to measure generalization performance.

---

## **Libraries Used**

The following Python libraries were used during model development and deployment:

* **pandas** – Data loading, cleaning, transformation, and analysis  
* **numpy** – Numerical computations and array operations  
* **plotly** – Interactive visualizations for exploratory analysis  
* **scikit-learn** – Machine learning models, preprocessing, evaluation, and hyperparameter tuning  
* **joblib** – Saving and loading trained models for deployment  

---

## **Evaluation Metrics**

To compare model performance objectively, three regression metrics were used.

### **MAE (Mean Absolute Error)**

MAE measures the average absolute difference between the actual salary and the predicted salary. It shows how far predictions are from true values on average and is easy to interpret because it uses the same unit as the target variable (USD). Lower MAE indicates better prediction accuracy.

<img width="1378" height="449" alt="Mean Absolute Error" src="https://github.com/user-attachments/assets/e04a6e49-3523-4235-a922-e773b243305d" />

### **RMSE (Root Mean Squared Error)**

RMSE calculates the square root of the average squared prediction errors. Because errors are squared before averaging, larger mistakes receive more penalty than smaller ones. This makes RMSE useful when large prediction errors are especially undesirable.

<img width="1366" height="463" alt="RMSE" src="https://github.com/user-attachments/assets/e4b37797-34ed-49c8-8531-b35c3ed87820" />

### **R² Score (Coefficient of Determination)**

R² Score measures how well the model explains the variation in the target variable. Its value typically ranges from 0 to 1, where values closer to 1 indicate stronger explanatory power and better overall fit.

<img width="1374" height="496" alt="R2 score" src="https://github.com/user-attachments/assets/572259a4-10fa-46fa-8322-4fd8ae3a8f45" />

---

## **Model Performance**

| Model             | MAE  | RMSE | R²     |
|------------------|------|------|--------|
| Linear Regression | 3522 | 4222 | 0.9869 |
| Random Forest     | 3786 | 4592 | 0.9846 |
| Gradient Boosting | 3522 | 4222 | 0.9869 |

### **Performance Interpretation**

The results show that all three models performed strongly, indicating that the selected features were highly informative for salary prediction. Linear Regression and Gradient Boosting achieved the best results with the lowest error values and highest R² score. Random Forest also performed well but showed slightly higher prediction errors.

---

## **Model Selection**

Gradient Boosting Regressor was selected as the final model because it offered strong predictive performance and robust learning behavior.

**Reasons for selection:**

* Captures complex feature interactions effectively  
* Handles non-linear relationships better than simple linear models  
* Provides stable and consistent results  
* Performs well on structured tabular datasets  
* Suitable for further optimization through hyperparameter tuning  

Although Linear Regression produced nearly identical results, Gradient Boosting was preferred because of its ability to model more complex patterns when scaling to richer datasets.

---

## **Hyperparameter Tuning**

To further optimize the selected model, hyperparameter tuning was performed using **GridSearchCV**, which systematically tests multiple parameter combinations and selects the best configuration based on cross-validation performance.

### **Best Parameters Found**

* `n_estimators = 200`  
* `learning_rate = 0.05`  
* `max_depth = 3`

### **Interpretation**

The tuned model showed only minimal improvement over the default version. This indicates that the original model configuration was already performing near its optimal level for the available dataset.

---

## **Feature Importance**

Feature importance analysis was performed to identify which predictors had the strongest influence on salary estimation.

### **Most Important Predictors**

* Senior experience level  
* Years of experience  
* Mid-level experience  

### **Insight**

The results confirm that professional experience is the most influential factor in salary determination. As seniority and experience increase, predicted salary also tends to increase significantly.

---

## **Residual Analysis**

Residual analysis examines the prediction errors of the model, where:

**Residual = Actual Salary − Predicted Salary**

It is used to evaluate whether the model errors are random and unbiased.

<img width="1348" height="450" alt="Residual Analysis" src="https://github.com/user-attachments/assets/f8c363e2-541a-47a7-8ca2-b26aa7d15353" />

### **Interpretation**

A well-performing model should produce residuals that are randomly distributed around zero without clear patterns. This suggests that the model is not consistently overestimating or underestimating salaries. In this project, residual analysis indicated a balanced fit and reliable prediction behavior.

---

# **6. Application of the Trained Models**

To make the model practical and user-friendly, a web application was developed using **Streamlit**. This allows users to interact with the trained model without writing code.

## **Application Functionality**

The application accepts user inputs related to job characteristics and instantly returns a predicted annual salary.

Users can provide:

* Job title  
* Country  
* Experience level  
* Years of experience  
* Work type  
* Company size  

After submitting the inputs, the trained model processes the data and generates a salary estimate in real time.

## **Workflow**

1. User enters job details through the interface  
2. Inputs are preprocessed to match training format  
3. Trained model generates salary prediction  
4. Result is displayed with benchmark comparison  

---

## **User Interface**

<img width="1812" height="945" alt="Screenshot (158)" src="https://github.com/user-attachments/assets/fffd31df-bd08-4e86-935a-325a4d00583b" />

<img width="1895" height="996" alt="Screenshot (159)" src="https://github.com/user-attachments/assets/6b08fd01-4573-4a90-973e-c2cd835ec80d" />

### **Benefits of the Application**

* Easy to use for non-technical users  
* Real-time salary estimation  
* Demonstrates practical deployment of machine learning  
* Can be extended for business or recruitment use cases  

---

## **Tools Used**

* **Streamlit** – Front-end web application framework  
* **Joblib** – Loading saved trained model files  

---

# **7. Conclusion**

This project successfully developed and evaluated machine learning models for predicting salaries in AI and Data Science roles using a large real-world dataset.

Among the tested models, Gradient Boosting achieved the best overall performance with high predictive accuracy and stable results. The findings also showed that experience level and years of experience are the most important variables influencing salary.

The project demonstrates how machine learning can transform raw job market data into practical insights and useful decision-support tools.

## **Applications**

* Salary benchmarking for job seekers  
* Compensation planning for companies  
* Job market analysis and workforce insights  
* Support for hiring and recruitment decisions  

## **Limitations**

* Limited set of input features  
* No external economic or labor market data included  
* No fairness or bias assessment performed  
* Results depend on the quality of available dataset  

## **Lessons Learned**

* Data quality has a major impact on model performance  
* Feature engineering significantly improves predictive accuracy  
* Simple models can sometimes compete with complex models  
* Deployment is essential for real-world usability  

## **Future Work**

* Add more features such as skills, education, certifications, and industry demand  
* Use advanced algorithms such as XGBoost or LightGBM  
* Apply stronger cross-validation strategies  
* Improve explainability and fairness analysis  
* Deploy as a production-ready cloud application  

---

# **8. References**

* Matbouli, Y.T., & Alghamdi, S.M. (2022). Statistical machine learning regression models for salary prediction. *Information, 13*(10), 495. [https://doi.org/10.3390/info13100495](https://doi.org/10.3390/info13100495)

* Gheriyani, N.S., & Dbeea, J.I. (2024). Salary prediction: Case study. *African Journal of Advanced Pure and Applied Sciences*. [https://doi.org/10.65418/ajapas.vi.766](https://doi.org/10.65418/ajapas.vi.766)

* Raj, P., et al. (2025). Forecasting salary using machine learning. *Atlantis Press*.

* Ayua, S.I. (2024). Salary prediction model using regression techniques.

* Alsheyab, A.R., et al. (2025). Job market salary prediction using ML. *arXiv*.

---
