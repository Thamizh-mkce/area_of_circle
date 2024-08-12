import streamlit as st
import math

# Function to calculate the area of a circle
def calculate_area(radius):
    return math.pi * radius ** 2

# Streamlit app layout
st.title("Area of a Circle Calculator")

# Input for radius
radius = st.number_input("Enter the radius of the circle", min_value=0.0, step=0.1)

# Calculate area when button is pressed
if st.button("Calculate Area"):
    if radius >= 0:
        area = calculate_area(radius)
        st.write(f"The area of the circle with radius {radius} is {area:.2f} square units.")
    else:
        st.error("Radius cannot be negative.")
