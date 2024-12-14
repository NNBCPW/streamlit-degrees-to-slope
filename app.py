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
3. **Press the TAN button.**
   - This gives the tangent of the angle.
4. **Multiply the result by 100 to get the percentage.
""")

# Add scrolling ticker at the bottom
ticker_message = "This is a scrolling ticker. Add updates, announcements, or notes here!"

st.markdown(
    f"""
    <div style="position: fixed; bottom: 0; width: 100%; background-color: black; color: white; overflow: hidden; z-index: 9999;">
        <marquee style="padding: 10px; font-size: 18px;" behavior="scroll" direction="left">
            {App is in beta for ongoing testing}
        </marquee>
    </div>
    """,
    unsafe_allow_html=True,
)

# Add "Created by" text at the very bottom
st.markdown(
    """
    <div style="text-align: center; font-size: 12px; margin-top: 20px; color: gray;">
        Created by: NN
    </div>
    """,
    unsafe_allow_html=True,
)
