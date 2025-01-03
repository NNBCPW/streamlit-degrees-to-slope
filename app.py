import streamlit as st
import math

def main():
    st.title("Degrees to Slope Percentage Calculator")

    # Input section
    st.header("Enter Degrees")
    degrees = st.number_input("Degrees", value=0.0, step=0.01)

    # Calculation
    if degrees > 0:
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
    4. **Multiply the result by 100 to get the percentage.**
    """)

    # Additional Calculation: Grade of a Road
    st.write("---")
    st.write("### How Do You Calculate the Grade of a Road?")
    st.write("Let's assume that the road has 39.37 feet of rise for every 656.17 feet of run.")

    # Inputs for rise and run
    rise = st.number_input("Enter the rise (in feet)", min_value=0.0, step=0.1)
    run = st.number_input("Enter the run (in feet)", min_value=0.0, step=0.1)

    if rise > 0 and run > 0:
        grade = rise / run
        slope_angle = math.degrees(math.atan(grade))
        slope_percentage = grade * 100

        st.write("### Results")
        st.write(f"Grade: {grade:.4f}")
        st.write(f"Slope (angle): {slope_angle:.2f}°")
        st.write(f"Slope (percentage): {slope_percentage:.2f}%")

    st.markdown("""
    **Note:** To calculate the grade of a road on a calculator:
    1. Divide the rise (in feet) by the run (in feet) to get the grade as a ratio.
       - Example: For 39.37 feet rise and 656.17 feet run: `grade = 39.37 / 656.17 = 0.06`.
    2. To find the angle of the slope, use the arctangent function: `angle = arctan(grade)`.
       - Example: `angle = arctan(0.06) = 3.43°`.
    3. To express the slope as a percentage, multiply the grade by 100: `slope (%) = grade × 100`.
       - Example: `slope (%) = 0.06 × 100 = 6%`.
    """)

    # Footer directly added at the end
    st.markdown(
        """
        <div style="width: 100%; background-color: black; color: white; text-align: center; padding: 10px; margin-top: 20px;">
            Created by: NN <br>
            <a href="mailto:Nicholas.nabholz@bexar.org?subject=Feedback%20on%20Degrees%20to%20Slope%20Percentage%20Calculator&body=Hello,%0A%0AI%20would%20like%20to%20provide%20feedback%20on%20the%20app.%0A%0A" 
               style="color: white; text-decoration: none;">
                For support, please click me. Thanks!
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()

