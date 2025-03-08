
import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
file_path = "university_student_dashboard_data.csv"
df = pd.read_csv(file_path)

# Set page config for a better layout
st.set_page_config(page_title="University Dashboard", layout="wide")


# KPI Metrics with colorful cards
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.markdown("<div class='metric-card'> <b>Total Applications</b><br>{}</div>".format(df_filtered['Applications'].sum()), unsafe_allow_html=True)
col2.markdown("<div class='metric-card'> <b>Total Admitted</b><br>{}</div>".format(df_filtered['Admitted'].sum()), unsafe_allow_html=True)
col3.markdown("<div class='metric-card'> <b>Total Enrolled</b><br>{}</div>".format(df_filtered['Enrolled'].sum()), unsafe_allow_html=True)

# Retention Rate Trends
st.subheader("Retention Rate Trends")
grouped_year = df_filtered.groupby("Year")["Retention Rate (%)"].mean().reset_index()
fig_retention = px.area(grouped_year, x="Year", y="Retention Rate (%)", 
                         title="Retention Rate Over Time", markers=True, 
                         color_discrete_sequence=["#FF5733"], template="plotly_dark")
st.plotly_chart(fig_retention, use_container_width=True)

# Satisfaction Trends
st.subheader("Student Satisfaction Trends")
fig_satisfaction = px.line(df_filtered, x="Year", y="Student Satisfaction (%)", color="Term", 
                           title="Student Satisfaction Over Time", markers=True, 
                           color_discrete_map={"Spring": "#FFA07A", "Fall": "#20B2AA"}, template="plotly_dark")
st.plotly_chart(fig_satisfaction, use_container_width=True)

# Enrollment Breakdown by Department
st.subheader("Enrollment Breakdown by Department")
department_data = df_filtered.melt(id_vars=["Year", "Term"], value_vars=selected_department, var_name="Department", value_name="Enrollment")
fig_enrollment = px.bar(department_data, x="Year", y="Enrollment", color="Department", 
                         barmode="group", title="Enrollment by Department", 
                         color_discrete_sequence=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"], template="plotly_dark")
st.plotly_chart(fig_enrollment, use_container_width=True)

# Spring vs Fall Comparison
st.subheader("Spring vs Fall Enrollment Comparison")
fig_term_comparison = px.bar(df_filtered, x="Year", y="Enrolled", color="Term", 
                             barmode="group", title="Enrollment Trends: Spring vs Fall", 
                             color_discrete_map={"Spring": "#17BECF", "Fall": "#9467BD"}, template="plotly_dark")
st.plotly_chart(fig_term_comparison, use_container_width=True)

# Compare Trends Between Departments, Retention Rates, and Satisfaction Levels
st.subheader("Comparison of Trends Across Departments")
fig_dept_comparison = px.line(df_filtered, x="Year", y=["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"], 
                              title="Enrollment Trends by Department", markers=True, template="plotly_dark")
st.plotly_chart(fig_dept_comparison, use_container_width=True)

fig_retention_comparison = px.line(df_filtered, x="Year", y="Retention Rate (%)", color="Term", 
                                   title="Retention Rate Comparison by Term", markers=True, template="plotly_dark")
st.plotly_chart(fig_retention_comparison, use_container_width=True)

fig_satisfaction_comparison = px.line(df_filtered, x="Year", y="Student Satisfaction (%)", color="Term", 
                                      title="Student Satisfaction Levels by Term", markers=True, template="plotly_dark")
st.plotly_chart(fig_satisfaction_comparison, use_container_width=True)

# Insights Section with Highlighted Box
st.subheader("Key Insights")
st.markdown("""
    <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
    <ul>
    <li> <b>Retention and satisfaction have steadily increased over the years.</b></li>
    <li> <b>Engineering sees the highest enrollment, followed by Business.</b></li>
    <li> <b>Fall enrollments are generally higher than Spring enrollments.</b></li>
    <li> <b>Trends in retention and satisfaction show consistent improvement across terms.</b></li>
    </ul>
    </div>
""", unsafe_allow_html=True)
