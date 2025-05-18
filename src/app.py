from pickle import load
import streamlit as st

# Cargar el modelo
model = load(open("/Users/jesus/Desktop/4geeks/4geeks -  streamlit/jesus-cuenca-STREAMLIT-machine-learning-python-template/models/best_model.pkl", "rb"))

st.title("Random forest")

embarazos = st.number_input(
    "Indica un número de embarazos", value=0, placeholder="Indica un número...", key="embarazos", step=1
)
st.write("El número actual es: ", embarazos)

glucosa = st.number_input(
    "Indica un valor glucosa", value=0.0, placeholder="Indica un número...", key="glucosa", step=1.0
)
st.write("El número actual es: ", glucosa)

Presión_sanguínea = st.number_input(
    "Indica un valor de presión sanguínea", value=0.0, placeholder="Indica un número...", key="presion_sanguinea", step=1.0
)
st.write("El número actual es: ", Presión_sanguínea)

Grosor_piel = st.number_input(
    "Indica un valor de grosor de piel", value=0.0, placeholder="Indica un número...", key="grosor_piel", step=1.0
)
st.write("El número actual es: ", Grosor_piel)

Insulina = st.number_input(
    "Indica un valor de insulina", value=0.0, placeholder="Indica un número...", key="insulina", step=1.0
)
st.write("El número actual es: ", Insulina)

BMI = st.number_input(
    "Indica un valor indice de masa corporal", value=0.0, placeholder="Indica un número...", key="bmi", step=0.1
)
st.write("El número actual es: ", BMI)

Diabetes = st.number_input(
    "Indica un valor de diabetes", value=0.0, placeholder="Indica un número...", key="diabetes", step=0.1
)
st.write("El número actual es: ", Diabetes)

Edad = st.number_input(
    "Indica una edad", value=0, placeholder="Indica un número...", key="edad", step=1
)
st.write("El número actual es: ", Edad)

# Botón para predecir
if st.button("Predecir"):
    if all([embarazos is not None, glucosa is not None, Presión_sanguínea is not None, Grosor_piel is not None, Insulina is not None, BMI is not None, Diabetes is not None, Edad is not None]):
        input_data = [[embarazos, glucosa, Presión_sanguínea, Grosor_piel, Insulina, BMI, Diabetes, Edad]]
        prediction = model.predict(input_data)
        st.write("Resultado de la predicción: ", "Positivo" if prediction[0] == 1 else "Negativo")
    else:
        st.write("Por favor, completa todos los campos.")
