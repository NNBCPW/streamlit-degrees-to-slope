import streamlit as st
import math

# App title
st.title("Degrees to Slope Percentage Calculator")

# Input section
st.header("Enter Degrees")
degrees = st.number_input("Degrees", value=0.0, step=0.01)

# Calculation
slope_percentage = math.tan(math.radians(degrees)) * 100

# Display result with custom styling
st.subheader("Slope Percentage")
st.markdown(
    f"""
    <div style='background-color: black; color: red; padding: 10px; border-radius: 5px;'>
        <h3>{slope_percentage:.2f}%</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Instructions
st.header("How to Calculate This on a Calculator")
st.markdown("""
1. **Ensure your calculator is in degree mode.**
   - Switch from radian mode if necessary.
2. **Enter the angle in degrees.**
   - Example: For 6 degrees, type `6`.
3. **Press the `TAN` button.**
   - This gives the tangent of the angle.
4. **Multiply the result by 100 to get the percentage.
""")
# Footer directly added at the end
st.markdown(
    """
    <div style="width: 100%; background-color: black; color: white; text-align: center; padding: 10px; margin-top: 20px;">
        Created by: NN <br>
        <a href="mailto:Nicholas.nabholz@bexar.org?subject=Feedback%20on%20BCPW%20Elevation%20Calc&body=Hello,%0A%0AI%20would%20like%20to%20provide%20feedback%20on%20the%20app.%0A%0A" 
           style="color: white; text-decoration: none;">
            For support, please email me. Thanks!
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)
