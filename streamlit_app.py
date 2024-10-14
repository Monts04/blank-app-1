import streamlit as st
import random
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt

# Título de la aplicación con emoji
st.title("⚖️ Ética en la Era del Big Data - Exposición Interactiva 📊")

# Menú de navegación con emojis
seccion = st.sidebar.selectbox("Selecciona una sección", 
                               ("🏠 Inicio", 
                                "📉 Criminalización de la Pobreza", 
                                "⚙️ Sesgo Algorítmico", 
                                "⚖️ Justicia vs Eficiencia", 
                                "📰 Posverdad y Fake News", 
                                "📝 Conclusión"))

# Sección 1: Inicio
if seccion == "🏠 Inicio":
    st.header("📚 Introducción")
    st.write("""
    En esta presentación, exploraremos los temas del capítulo **"Víctimas civiles: La justicia en la era del Big Data"** del libro *Armas de Destrucción Matemática* de Cathy O'Neil. Analizaremos cómo los algoritmos impactan la justicia y cómo la eficiencia tecnológica puede comprometer los derechos humanos.
    
    Los temas incluyen:
    - 📉 Criminalización de la pobreza
    - ⚙️ Sesgo en los algoritmos
    - ⚖️ Conflicto entre justicia y eficiencia
    - 📰 El rol de la posverdad y las fake news
    """)

# Sección 2: Criminalización de la Pobreza
elif seccion == "📉 Criminalización de la Pobreza":
    st.header("📉 Criminalización de la Pobreza")
    st.write("""
    En esta sección, exploramos cómo los modelos predictivos, como PredPol, tienden a concentrarse en los barrios pobres, generando un bucle de retroalimentación. Más vigilancia genera más arrestos, justificando aún más vigilancia.
    """)
    
    st.info("Para entender mejor, ejecutemos un código que simula este bucle 👇")
    
    # Simulación de vigilancia
    barrio_vigilado = st.radio("👮‍♂️ ¿Quieres aumentar la vigilancia en un barrio pobre?", ('Sí', 'No'))
    arrestos = 0

    if barrio_vigilado == 'Sí':
        arrestos = random.randint(5, 15)
        st.write(f"🔴 Se han realizado **{arrestos} arrestos** en el barrio vigilado.")
        st.write("Esto justifica más presencia policial 🚨.")
        
        decision = st.radio("👮‍♀️ ¿Deseas aumentar la vigilancia de nuevo?", ('Sí', 'No'))
        if decision == 'Sí':
            arrestos += random.randint(5, 15)
            st.write(f"🔴 Ahora se han realizado **{arrestos} arrestos**. El bucle continúa...")
        else:
            st.write("🟢 Decidiste no aumentar la vigilancia, pero los arrestos iniciales ya refuerzan la percepción de criminalidad.")
    else:
        st.write("🟢 No aumentaste la vigilancia, el número de arrestos en la zona se mantiene bajo.")

# Sección 3: Sesgo Algorítmico
elif seccion == "⚙️ Sesgo Algorítmico":
    st.header("⚙️ Sesgo Algorítmico")
    st.write("""
    Aunque los algoritmos se presentan como neutrales, en realidad, los datos sobre los que se basan están llenos de sesgos históricos. Esto afecta desproporcionadamente a las minorías y a las personas en barrios pobres.
    
    Ajusta los niveles de vigilancia en los barrios para ver cómo cambia el número de arrestos. 🎯
    """)

    # Deslizadores para controlar el nivel de vigilancia en los barrios
    vigilancia_pobre = st.slider("📉 Nivel de vigilancia en el barrio pobre", 0, 100, 50)
    vigilancia_rico = st.slider("📈 Nivel de vigilancia en el barrio rico", 0, 100, 50)

    # Simular el número de arrestos en función del nivel de vigilancia
    arrestos_pobre = int(vigilancia_pobre * 1.5)  # Barrio pobre más sensible a la vigilancia
    arrestos_rico = int(vigilancia_rico * 0.8)    # Barrio rico menos afectado por vigilancia

    # Crear un DataFrame con los datos
    data = pd.DataFrame({
        'Barrio': ['Barrio Pobre', 'Barrio Rico'],
        'Arrestos': [arrestos_pobre, arrestos_rico]
    })

    # Crear gráfico con Altair
    chart = alt.Chart(data).mark_bar().encode(
        x='Barrio',
        y='Arrestos',
        color='Barrio'
    ).properties(
        title='Impacto de la Vigilancia en los Arrestos'
    )

    # Mostrar el gráfico
    st.altair_chart(chart, use_container_width=True)

    st.write(f"📊 **Arrestos en el barrio pobre:** {arrestos_pobre}")
    st.write(f"📊 **Arrestos en el barrio rico:** {arrestos_rico}")

    st.write("""
    Como puedes ver, al aumentar la vigilancia en el barrio pobre, el número de arrestos crece más rápidamente que en el barrio rico, lo que refuerza el sesgo algorítmico.
    """)

# Sección 4: Justicia vs Eficiencia
elif seccion == "⚖️ Justicia vs Eficiencia":
    st.header("⚖️ Justicia vs Eficiencia")
    st.write("""
    En la toma de decisiones judiciales, los algoritmos tienden a priorizar la eficiencia, lo que puede socavar la justicia. ¿Qué priorizarías en el uso de algoritmos: la eficiencia o la justicia?
    """)
    
    decision = st.radio("🤔 ¿Qué priorizarías?", ('⚙️ Eficiencia', '⚖️ Justicia'))

    if decision == '⚙️ Eficiencia':
        st.warning("Elegiste eficiencia. Los algoritmos seguirán siendo efectivos, pero a costa de los derechos humanos.")
    else:
        st.success("Elegiste justicia. Esto implica limitar el uso de ciertos datos para evitar sesgos y proteger los derechos humanos.")

# Sección 5: Posverdad y Fake News
elif seccion == "📰 Posverdad y Fake News":
    st.header("📰 Posverdad y Fake News")
    st.write("""
    En la era de la información, la manipulación de los datos y la difusión de noticias falsas (Fake News) afectan la percepción pública. Cathy O'Neil destaca cómo la confianza en modelos y algoritmos puede perpetuar una falsa sensación de seguridad y justicia, similar a cómo las fake news distorsionan la realidad.
    
    Ahora, intentemos identificar noticias reales de fake news, al igual que intentamos discernir entre datos verídicos y modelos sesgados. ¡Veamos cómo te va! 🔍
    """)

    # Fake news y noticias reales
    noticias = [
        {"titular": "Las vacunas causan autismo, según un estudio de Harvard.", "fake": True},
        {"titular": "El cambio climático es una farsa, revelan científicos anónimos.", "fake": True},
        {"titular": "Nuevas tecnologías reducen el tiempo de diagnóstico en hospitales.", "fake": False},
        {"titular": "Los teléfonos móviles provocan cáncer cerebral, según nueva investigación.", "fake": True},
        {"titular": "La inteligencia artificial revoluciona la educación en línea.", "fake": False}
    ]
    
    st.write("🤔 Intenta adivinar si los siguientes titulares son reales o fake news:")

    # Seleccionar 3 noticias aleatorias
    selected_news = random.sample(noticias, 3)

    correct_answers = 0
    for noticia in selected_news:
        st.write(f"📰 **Titular:** {noticia['titular']}")
        respuesta = st.radio("¿Es real o fake news?", ['Real', 'Fake News'], key=noticia['titular'])
        if (respuesta == 'Real' and not noticia['fake']) or (respuesta == 'Fake News' and noticia['fake']):
            st.success("¡Correcto! ✅")
            correct_answers += 1
        else:
            st.error("Incorrecto. ❌")
    
    st.write(f"Has acertado {correct_answers} de 3. ¡Sigue practicando para mejorar tu habilidad de discernir entre la verdad y la posverdad!")

# Sección 6: Conclusión
elif seccion == "📝 Conclusión":
    st.header("📝 Conclusión")
    st.write("""
    A lo largo de esta presentación, hemos visto cómo los algoritmos, lejos de ser neutrales, pueden reforzar desigualdades y perpetuar sesgos históricos. También discutimos cómo las fake news y la posverdad afectan nuestra percepción de la realidad.
    
    🌍 **Reflexión final:** La pregunta clave es cómo podemos usar la tecnología de manera responsable para proteger los derechos humanos y garantizar una justicia más equitativa.
    
    Debemos abordar la tecnología con una visión crítica, asegurándonos de que los algoritmos y los modelos no se conviertan en "armas de destrucción matemática". Solo así podremos avanzar hacia un futuro más justo y equitativo. ⚖️
    """)

    st.balloons()