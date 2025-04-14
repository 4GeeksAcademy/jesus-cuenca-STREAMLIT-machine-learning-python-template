from pickle import load
import streamlit as st

model = load(open("/Users/jesus/Desktop/4geeks/4geeks -  streamlit/jesus-cuenca-STREAMLIT-machine-learning-python-template/models/best_model.pkl", "rb"))

st.title("Random forest")

embarazos = st.number_input(
    "Indica un valor", value=None, placeholder="Indica un número..."
)
st.write("El número actual es: ", embarazos)

glucosa = st.number_input(
    "Indica un valor", value=None, placeholder="Indica un número..."
)
st.write("El número actual es: ", glucosa)

Presión_sanguínea = st.number_input(
    "Indica un valor", value=None, placeholder="Indica un número..."
)
st.write("El número actual es: ", Presión_sanguínea)

Grosor_piel = st.number_input(
    "Indica un valor", value=None, placeholder="Indica un número..."
)
st.write("El número actual es: ", Grosor_piel)

Insulina = st.number_input(
    "Indica un valor", value=None, placeholder="Indica un número..."
)
st.write("El número actual es: ", Insulina)

BMI = st.number_input(
    "Indica un valor", value=None, placeholder="Indica un número..."
)
st.write("El número actual es: ", BMI)

Diabetes = st.number_input(
    "Indica un valor", value=None, placeholder="Indica un número..."
)
st.write("El número actual es: ", Diabetes)

Edad = st.number_input(
    "Indica un valor", value=None, placeholder="Indica un número..."
)
st.write("El número actual es: ", Edad)