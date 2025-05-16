# 📊 JAMB Performance Analysis Web App

This is a Streamlit-based web application that provides insightful analysis on students' performance in the Joint Admissions and Matriculation Board (JAMB) examination. It helps visualize trends and factors that influence success rates across various demographics.

---

## 🚀 Live App

🔗 [Click here to view the live app](https://francisbright1-jamb-performance-analysis-jamb-app-bv9irx.streamlit.app/)

---

## 📂 Project Structure

├── Jamb_app.py # Main Streamlit application

├── jamb_exam_results.csv # Dataset used for analysis

├── requirements.txt # Python dependencies

└── README.md # Project documentation


---

## 📈 Key Features

- Score band categorization and distribution
- Success rate analysis based on:
  - Extra tutorials
  - Parental involvement
  - Access to learning materials
  - School type
  - Socioeconomic status (Pie chart)
  - Parent education level (Bar chart with value labels)
- Cross analysis:
  - School location vs. Gender
  - Extra tutorials vs. School location
- Interactive data table preview
- Clean and engaging data visualizations using Plotly

---

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- Python 3.12+

---

## 📊 Dataset Info

The dataset includes fictional but realistic records of JAMB exam results, including:
- JAMB Score
- Gender
- School location
- Parent involvement
- Extra tutorial attendance
- Socioeconomic status
- Access to learning materials

---

## 📦 Installation

To run the project locally:

```bash
git clone https://github.com/FrancisBright1/Jamb-Performance-Analysis.git
cd Jamb-Performance-Analysis
pip install -r requirements.txt
streamlit run Jamb_app.py

