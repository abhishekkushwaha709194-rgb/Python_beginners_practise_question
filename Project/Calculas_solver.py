import streamlit as st
import sympy as sp

x = sp.symbols('x')

st.title("Calculus Solver")

operation = st.selectbox("Choose operation", ["Derivative", "Integral"])


if operation == "Derivative":
    expr_input = st.text_input("Enter expression")

    if st.button("Solve"):
        try:
            expr = sp.sympify(expr_input)
            result = sp.diff(expr, x)
            st.success(f"Derivative: {result}")
        except Exception as e:
            st.error(f"Error: {e}")

elif operation == "Integral":
    expr_input = st.text_input("Enter expression")
    lower = st.text_input("Lower limit (optional)")
    upper = st.text_input("Upper limit (optional)")

    if st.button("Solve"):
        try:
            expr = sp.sympify(expr_input)

            if lower and upper:
                result = sp.integrate(expr, (x, float(lower), float(upper)))
            else:
                result = sp.integrate(expr, x)

            st.success(f"Integral: {result}")

        except Exception as e:
            st.error(f"Error: {e}")