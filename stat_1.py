import streamlit as st
import numpy as np
import scipy.stats as stats

# Function to calculate statistics
def calculate_statistics(data):
    mean = np.mean(data)
    variance = np.var(data)
    std_dev = np.std(data)
    
    # Confidence interval (95%)
    confidence_level = 0.95
    n = len(data)
    sem = stats.sem(data)
    margin_of_error = sem * stats.t.ppf((1 + confidence_level) / 2., n-1)
    conf_interval = (mean - margin_of_error, mean + margin_of_error)
    
    return mean, variance, std_dev, conf_interval

# Streamlit UI
st.title("📊 Statistical Calculator")

st.write("Enter your data (comma separated):")
data_input = st.text_input("Data", placeholder="e.g., 1, 2, 3, 4, 5")

if st.button("Calculate Statistics"):
    try:
        data = list(map(float, data_input.split(',')))
        if len(data) < 2:
            st.error("Please enter at least two numbers.")
        else:
            mean, variance, std_dev, conf_interval = calculate_statistics(data)
            st.success("Calculation Successful!")

            st.write(f"**Mean:** {mean:.2f}")
            st.write(f"**Variance:** {variance:.2f}")
            st.write(f"**Standard Deviation:** {std_dev:.2f}")
            st.write(f"**Confidence Interval (95%):** ({conf_interval[0]:.2f}, {conf_interval[1]:.2f})")
    except ValueError:
        st.error("Please enter a valid list of numbers separated by commas.")
