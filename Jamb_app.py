import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="JAMB Score EDA", layout="wide")
st.title("📊 2024 JAMB Exam Result Analysis")

# Load and clean dataset
df = pd.read_csv("jamb_exam_results.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Debug: Display column names
st.write("Cleaned column names:", df.columns.tolist())

# Score Band Categorization
def categorize_score(score):
    if 100 <= score <= 120:
        return "Very Poor"
    elif 121 <= score <= 200:
        return "Poor"
    elif 201 <= score <= 260:
        return "Fair"
    elif 261 <= score <= 300:
        return "Good"
    elif 301 <= score <= 350:
        return "Very Good"
    elif 351 <= score <= 400:
        return "Excellent"
    else:
        return "Invalid"

df["score_band"] = df["jamb_score"].apply(categorize_score)
df["is_successful"] = df["jamb_score"] >= 260

# Display raw data
st.subheader("Raw Data with Score Band")
st.dataframe(df.head())

# Score Band Distribution
st.subheader("Score Band Distribution")
fig1 = px.histogram(df, x="score_band", color="score_band", title="Distribution of Candidates by Score Band")
st.plotly_chart(fig1, use_container_width=True)

# Success Rate by Extra Tutorials Attendance
st.subheader("Success Rate: Extra Tutorials Attendance")
if "extra_tutorials" in df.columns:
    tutorial_group = df.groupby("extra_tutorials")["is_successful"].mean().reset_index()
    tutorial_group["is_successful"] *= 100
    fig2 = px.bar(tutorial_group, x="extra_tutorials", y="is_successful",
                  title="Success Rate by Extra Tutorials Attendance",
                  labels={"is_successful": "Success Rate (%)"})
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.warning("⚠️ Column 'extra_tutorials' not found in dataset.")

# Success Rate by Parental Involvement
st.subheader("Success Rate: Parental Involvement")
if "parent_involvement" in df.columns:
    parent_group = df.groupby("parent_involvement")["is_successful"].mean().reset_index()
    parent_group["is_successful"] *= 100
    fig3 = px.bar(parent_group, x="parent_involvement", y="is_successful",
                  title="Success Rate by Parental Involvement",
                  labels={"is_successful": "Success Rate (%)"})
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.warning("⚠️ Column 'parent_involved' not found in dataset.")

# Success Rate by Area (Rural vs Urban)
st.subheader("Success Rate: Rural vs Urban")
if "school_location" in df.columns:
    area_group = df.groupby("school_location")["is_successful"].mean().reset_index()
    area_group["is_successful"] *= 100
    fig4 = px.bar(area_group, x="school_location", y="is_successful",
                  title="Success Rate by Area",
                  labels={"is_successful": "Success Rate (%)"})
    st.plotly_chart(fig4, use_container_width=True)
else:
    st.warning("⚠️ Column 'area' not found in dataset.")

# Success rate by gender
st.subheader("Success Rate: Gender")

gender_group = df.groupby("gender")["is_successful"].mean().reset_index()
gender_group["is_successful"] = gender_group["is_successful"] * 100  # convert to %

# Sort and get most successful gender
most_successful_gender = gender_group.sort_values(by="is_successful", ascending=False).iloc[0]

st.write(f"🎯 The most successful gender is **{most_successful_gender['gender']}** with a success rate of **{most_successful_gender['is_successful']:.2f}%**.")

# Show bar chart
fig = px.bar(gender_group, x="gender", y="is_successful",
             title="Success Rate by Gender",
             labels={"is_successful": "Success Rate (%)"})
st.plotly_chart(fig, use_container_width=True)

# Success rate based on access to learning materials
st.subheader("Success Rate: Access to Learning Materials")

materials_group = df.groupby("access_to_learning_materials")["is_successful"].mean().reset_index()
materials_group["is_successful"] = materials_group["is_successful"] * 100  # convert to %

# Display chart
fig = px.bar(
    materials_group,
    x="access_to_learning_materials",
    y="is_successful",
    title="Success Rate by Access to Learning Materials",
    labels={"is_successful": "Success Rate (%)", "access_to_learning_materials": "Access to Learning Materials"}
)
st.plotly_chart(fig, use_container_width=True)

# Success rate based on school type
st.subheader("Success Rate: School Type")

school_group = df.groupby("school_type")["is_successful"].mean().reset_index()
school_group["is_successful"] = school_group["is_successful"] * 100  # convert to %

# Bar chart
fig = px.bar(
    school_group,
    x="school_type",
    y="is_successful",
    title="Success Rate by School Type",
    labels={"is_successful": "Success Rate (%)", "school_type": "School Type"}
)
st.plotly_chart(fig, use_container_width=True)


# Success rate by school type and gender
st.subheader("Success Rate: School Type + Gender")

school_gender_group = df.groupby(["school_type", "gender"])["is_successful"].mean().reset_index()
school_gender_group["is_successful"] = school_gender_group["is_successful"] * 100  # convert to %

# Bar chart
fig = px.bar(
    school_gender_group,
    x="school_type",
    y="is_successful",
    color="gender",
    barmode="group",
    title="Success Rate by School Type and Gender",
    labels={"is_successful": "Success Rate (%)", "school_type": "School Type"}
)
st.plotly_chart(fig, use_container_width=True)

# Success rate by extra tutorials and school location
st.subheader("Success Rate: Extra Tutorials + School Location")

tutorial_location_group = df.groupby(["extra_tutorials", "school_location"])["is_successful"].mean().reset_index()
tutorial_location_group["is_successful"] = tutorial_location_group["is_successful"] * 100  # convert to %

# Bar chart
fig = px.bar(
    tutorial_location_group,
    x="extra_tutorials",
    y="is_successful",
    color="school_location",
    barmode="group",
    title="Success Rate by Extra Tutorials and School Location",
    labels={"is_successful": "Success Rate (%)", "extra_tutorials": "Extra Tutorials"}
)
st.plotly_chart(fig, use_container_width=True)

top_combo = tutorial_location_group.sort_values(by="is_successful", ascending=False).iloc[0]
st.write(f"📍 Highest success rate is among students who took **{top_combo['extra_tutorials']}** tutorials in **{top_combo['school_location']}** areas — **{top_combo['is_successful']:.2f}%** success.")

# Success rate by socioeconomic status
st.subheader("Success Rate: Socioeconomic Status")

socio_group = df.groupby("socioeconomic_status")["is_successful"].mean().reset_index()
socio_group["is_successful"] = socio_group["is_successful"] * 100  # convert to %

# Pie chart
fig = px.pie(
    socio_group,
    names="socioeconomic_status",
    values="is_successful",
    title="Success Rate by Socioeconomic Status",
    hole=0.4
)
fig.update_traces(textinfo="label+percent", pull=[0.05]*len(socio_group))

st.plotly_chart(fig, use_container_width=True)

# Success rate by parent education level
st.subheader("Success Rate: Parent Education Level")

parent_edu_group = df.groupby("parent_education_level")["is_successful"].mean().reset_index()
parent_edu_group["is_successful"] = parent_edu_group["is_successful"] * 100  # convert to %

# Column chart with value labels
fig = px.bar(
    parent_edu_group,
    x="parent_education_level",
    y="is_successful",
    title="Success Rate by Parent Education Level",
    labels={"is_successful": "Success Rate (%)", "parent_education_level": "Parent Education Level"},
    color="parent_education_level",
    text="is_successful"  # Add text labels
)

fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')  # Format and position
fig.update_layout(
    xaxis_title="Parent Education Level",
    yaxis_title="Success Rate (%)",
    uniformtext_minsize=8,
    uniformtext_mode='hide'
)

st.plotly_chart(fig, use_container_width=True)


# Frequency of male and female candidates by school location
st.subheader("Candidate Distribution: School Location + Gender")

gender_location_count = df.groupby(["school_location", "gender"]).size().reset_index(name="count")

fig = px.bar(
    gender_location_count,
    x="school_location",
    y="count",
    color="gender",
    barmode="group",
    title="Number of Male and Female Candidates by School Location",
    labels={"count": "Number of Candidates", "school_location": "School Location"},
    text="count"  # Add value labels
)

fig.update_traces(textposition='outside')  # Position labels above bars
fig.update_layout(
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    yaxis=dict(title="Number of Candidates")
)

st.plotly_chart(fig, use_container_width=True)




# Summary Table
st.subheader("Summary Table")
expected_columns = ["jamb_score", "score_band", "extra_tutorials", "parent_involved", "area", "is_successful"]
present_columns = [col for col in expected_columns if col in df.columns]
st.dataframe(df[present_columns].head(20))
