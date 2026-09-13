import streamlit as st
import sympy as sp

x = sp.symbols('x')

def solve(expr_input, choice):
    expr = sp.sympify(expr_input)

    if choice == "Derivative":
        return sp.diff(expr, x)
    elif choice == "Integral":
        return sp.integrate(expr, x)
    else:
        return "Invalid choice"

st.title("Calculus Solver")

expr_input = st.text_input("Enter expression:")
operation = st.selectbox("Choose operation", ["Derivative", "Integral"])

if st.button("Solve"):
    try:
        result = solve(expr_input, operation)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")