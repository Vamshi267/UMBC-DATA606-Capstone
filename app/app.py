
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="AI Job Salary Predictor",
    page_icon="💼",
    layout="wide"
)

# -----------------------------
# Load model artifacts
# -----------------------------
model = joblib.load("salary_prediction_model.pkl")
model_columns = joblib.load("model_columns.pkl")

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
    <style>
    .main {
        background: linear-gradient(180deg, #f8fbff 0%, #eef4ff 100%);
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    .hero-box {
        background: linear-gradient(135deg, #1f4cff, #6a5cff);
        padding: 28px;
        border-radius: 18px;
        color: white;
        box-shadow: 0 10px 25px rgba(0,0,0,0.12);
        margin-bottom: 1.5rem;
    }
    .hero-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }
    .hero-subtitle {
        font-size: 1rem;
        opacity: 0.95;
    }
    .card {
        background: white;
        padding: 18px;
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.06);
        border: 1px solid #edf1f7;
        margin-bottom: 1rem;
    }
    .small-label {
        font-size: 0.9rem;
        color: #6b7280;
        margin-bottom: 0.2rem;
    }
    .big-value {
        font-size: 1.15rem;
        font-weight: 700;
        color: #111827;
    }
    .salary-box {
        background: linear-gradient(135deg, #0f9d58, #34c38f);
        padding: 24px;
        border-radius: 16px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.12);
        margin: 1rem 0;
    }
    .salary-text {
        font-size: 1rem;
        opacity: 0.95;
    }
    .salary-value {
        font-size: 2.2rem;
        font-weight: 800;
        margin-top: 0.4rem;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="hero-box">
    <div class="hero-title">AI & Data Science Salary Prediction</div>
    <div class="hero-subtitle">
        Predict annual salary based on role, location, experience, work type, and company size.
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("Enter Job Details")

job_title = st.sidebar.selectbox(
    "Job Title",
    ["Data Scientist", "Data Analyst", "ML Engineer", "MLOps Engineer", "Applied Scientist"]
)

country = st.sidebar.selectbox(
    "Country",
    ["USA", "India", "UK", "Germany", "Canada"]
)

experience_level = st.sidebar.selectbox(
    "Experience Level",
    ["Entry", "Mid", "Senior"]
)

min_experience_years = st.sidebar.slider("Minimum Experience Years", 0, 20, 2)

remote_type = st.sidebar.selectbox(
    "Work Type",
    ["Remote", "Hybrid", "Onsite"]
)

company_size = st.sidebar.selectbox(
    "Company Size",
    ["Small", "Medium", "Large"]
)

predict_clicked = st.sidebar.button("Predict Salary", use_container_width=True)

# Fixed internally, not shown in UI
posted_year = 2024

# -----------------------------
# Prepare input
# -----------------------------
input_data = pd.DataFrame([{
    "job_title": job_title,
    "country": country,
    "experience_level": experience_level,
    "min_experience_years": min_experience_years,
    "remote_type": remote_type,
    "company_size": company_size,
    "posted_year": posted_year
}])

input_encoded = pd.get_dummies(input_data)

for col in model_columns:
    if col not in input_encoded.columns:
        input_encoded[col] = 0

input_encoded = input_encoded[model_columns]

# -----------------------------
# Main Output Area
# -----------------------------
st.markdown("### Prediction Result")

c1, c2 = st.columns(2)
with c1:
    st.markdown(f"""
    <div class="card">
        <div class="small-label">Job Role</div>
        <div class="big-value">{job_title}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
        <div class="small-label">Country</div>
        <div class="big-value">{country}</div>
    </div>
    """, unsafe_allow_html=True)

c3, c4 = st.columns(2)
with c3:
    st.markdown(f"""
    <div class="card">
        <div class="small-label">Experience</div>
        <div class="big-value">{experience_level} ({min_experience_years} yrs)</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="card">
        <div class="small-label">Work Setup</div>
        <div class="big-value">{remote_type} / {company_size}</div>
    </div>
    """, unsafe_allow_html=True)

if predict_clicked:
    prediction = model.predict(input_encoded)[0]

    st.markdown(f"""
    <div class="salary-box">
        <div class="salary-text">Predicted Annual Salary</div>
        <div class="salary-value">${prediction:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Salary Benchmarks")

    comparison_df = pd.DataFrame({
        "Category": ["Entry Benchmark", "Mid Benchmark", "Senior Benchmark", "Your Prediction"],
        "Salary": [70000, 110000, 160000, prediction]
    })

    st.bar_chart(comparison_df.set_index("Category"))

    st.markdown("""
    <div class="card">
        <div class="small-label">Model Status</div>
        <div class="big-value">Prediction generated successfully using the trained salary model.</div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="card">
        <div class="small-label">Status</div>
        <div class="big-value">Select inputs from the sidebar and click “Predict Salary”.</div>
    </div>
    """, unsafe_allow_html=True)
