import streamlit as st
import random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Introducción - Título
def slide_intro():
    st.title("📰 ComuCode: La Comunicación en Acción - El Virreinato de la Nueva Granada")
    st.header("🗣️ Introducción")
    st.write("""
    Bienvenidos a **ComuCode**, una experiencia interactiva que muestra cómo la **programación** puede ayudarnos a entender los **temas históricos** de la **comunicación** en el **Virreinato de la Nueva Granada** entre **1810 y 1816**.
    
    A través de este proyecto, exploraremos cómo los **periódicos monárquicos** y **realistas** influyeron en la **opinión pública** durante el conflicto independentista, ayudando a **defender el orden colonial** y contrarrestar las ideas **independentistas**.
    
    ¡Prepárate para interactuar con la historia y entender cómo la **programación** puede ilustrar conceptos tan fundamentales como la construcción de la **esfera pública**!
    """)

# 2. Interactividad: Opinión Pública en 1810
def slide_slider_opinion():
    st.header("📊 Simulación de la Opinión Pública en 1810")
    st.write("""
    Usaremos un **slider interactivo** para mostrar cómo la **opinión pública** cambiaba entre los defensores del **orden colonial** y los **independentistas** a lo largo de los años, según la influencia de los **periódicos monárquicos**.
    
    **Desliza para ver cómo cambiaba la percepción pública de los diferentes temas en los periódicos**.
    """)

    # Usamos el slider para manipular la "opinión pública" en base al año o la influencia
    year = st.slider("Selecciona un año (1810 - 1816)", 1810, 1816, 1810)
    
    # Suponiendo que los periódicos monárquicos aumentaban su influencia a medida que la guerra avanzaba
    opinion_colonial = np.clip(100 - (year - 1810) * 5, 0, 100)  # Entre 100 y 0
    opinion_independentista = 100 - opinion_colonial
    
    # Visualizamos la opinión pública usando gráficos de barras
    opinion_data = {
        'Orden Colonial': opinion_colonial,
        'Independencia': opinion_independentista
    }
    df = pd.DataFrame(list(opinion_data.items()), columns=["Opinión", "Porcentaje"])

    # Mostrar la gráfica de barras
    st.bar_chart(df.set_index("Opinión"))
    
    st.write(f"En el año {year}, la percepción pública era: ")
    st.write(f"**{opinion_colonial}%** a favor del orden colonial y **{opinion_independentista}%** a favor de la independencia.")

# 3. Gráfica Interactiva: Distribución de Temas en los Periódicos
def slide_grafica_temporal():
    st.header("📈 Evolución de los Temas en los Periódicos Monárquicos")
    st.write("""
    Ahora vamos a ver cómo la **distribución de los temas** en los **periódicos monárquicos** cambiaba a lo largo del tiempo, en relación con la **guerra**, **política** y **sociedad**.
    
    Desliza para ver cómo los temas ganaban o perdían relevancia durante los años de la **guerra** y el **conflicto**.
    """)

    # Slider para seleccionar el año
    year = st.slider("Selecciona el año para ver la distribución de temas", 1810, 1816, 1810)
    
    # Crear una distribución de temas dependiendo del año
    if year <= 1812:
        guerra = 40 + random.randint(0, 20)  # Aumento gradual en guerra
        politica = 30
        sociedad = 20
        economia = 10
    elif year <= 1814:
        guerra = 60
        politica = 25
        sociedad = 10
        economia = 5
    else:
        guerra = 80
        politica = 15
        sociedad = 3
        economia = 2
    
    # Graficamos la distribución de los temas en los periódicos
    temas = ['Guerra', 'Política', 'Sociedad', 'Economía']
    distribucion = [guerra, politica, sociedad, economia]
    
    plt.figure(figsize=(10, 6))
    plt.bar(temas, distribucion, color=['red', 'green', 'blue', 'orange'])
    plt.title(f'Distribución de Temas en los Periódicos en {year}')
    plt.xlabel('Secciones del Periódico')
    plt.ylabel('Porcentaje de Contenido')
    st.pyplot(plt)

# 4. Conclusión Final y Reflexión
def slide_conclusion():
    st.header("📝 Conclusión")
    st.write("""
    En esta presentación interactiva, hemos explorado cómo los **periódicos monárquicos** y **realistas** ayudaron a moldear la **opinión pública** en el **Virreinato de la Nueva Granada** durante los años críticos de la independencia (1810-1816).
    
    Al usar **herramientas de programación**, pudimos visualizar cómo la **comunicación masiva** influía en las decisiones políticas y sociales de la época. Además, al integrar **Big Data** y conceptos como **PredPol**, hemos hecho un paralelo entre el pasado y el impacto de los **algoritmos modernos** en la **esfera pública**.
    
    Reflexionamos sobre cómo los **medios conservadores** y **discursos contrarrevolucionarios** siguen teniendo una influencia notable en la **opinión pública** hoy en día, similar a los periódicos de la época.
    """)

# 2. Herramientas de Historia Social de la Comunicación: Fuentes y Metodologías
def slide_hsc_metodologia():
    st.header("📜 Herramientas Metodológicas en la Historia Social de la Comunicación")
    st.write("""
    La **Historia Social de la Comunicación** se enfoca en cómo los **intercambios simbólicos** (medios, discursos, prensa) **configuran** y **moldean la realidad social**. Usaremos este enfoque para analizar cómo los periódicos de la época ayudaban a **defender el orden colonial** y consolidar el poder realista en el **Virreinato de la Nueva Granada**.
    
    **Herramientas clave**:
    - **Fuentes**: Periódicos, literatura, fuentes orales, objetos.
    - **Criterios de Periodización**: Analizar cómo los **medios** influían en las **etapas críticas** del proceso de independencia.
    - **Divulgación**: Cómo se comunicaban y se entendían las ideas entre los diferentes sectores sociales.
    """)

    # Agregar herramientas de visualización
    st.write("Veamos cómo la **comunicación** de la época se basaba en **intercambios simbólicos** que reforzaban el poder realista.")

    # Gráfico de distribución de fuentes y tipos de medios en la época
    fuentes = ['Prensa Realista', 'Literatura', 'Fuentes Orales', 'Objetos Históricos']
    cantidad = [70, 15, 10, 5]

    plt.figure(figsize=(10, 6))
    plt.pie(cantidad, labels=fuentes, autopct='%1.1f%%', startangle=140, colors=['blue', 'green', 'orange', 'red'])
    plt.title('Distribución de Fuentes en la Historia Social de la Comunicación (Virreinato)')
    st.pyplot(plt)

# 3. Los Periódicos Monárquicos y la Defensa del Orden Colonial
def slide_periodicos_monarquicos():
    st.header("📜 Los Periódicos Monárquicos en la Contrarrevolución")
    st.write("""
    Los **periódicos monárquicos** fueron fundamentales en la **defensa del orden colonial**. A través de sus publicaciones, **moldeaban la opinión pública** para promover una narrativa que defendiera la **legitimidad del gobierno colonial** y presentara la **independencia** como una **amenaza** al orden social.
    
    Vamos a ver cómo los periódicos de la época distribuían el contenido relacionado con los **temores de la independencia**, **el miedo a la anarquía**, y la **justificación de la intervención de la corona**.
    """)

    # Crear una gráfica de barras con distribución de temas
    secciones = ['Guerra', 'Política', 'Sociedad', 'Economía']
    porcentaje = [35, 25, 20, 20]

    plt.figure(figsize=(10, 6))
    plt.bar(secciones, porcentaje, color=['red', 'green', 'blue', 'orange'])
    plt.title('Distribución de Temas en Periódicos Monárquicos (1810-1816)')
    plt.xlabel('Secciones del Periódico')
    plt.ylabel('Porcentaje de Contenido')
    st.pyplot(plt)

# 2. Sección de Criminalización de la Pobreza con Simulación de PredPol
def slide_criminalizacion():
    st.header("🔴 Criminalización de la Pobreza y PredPol")
    st.write("""
    En esta sección, exploramos cómo los modelos predictivos, como **PredPol**, tienden a concentrarse en los **barrios pobres**, generando un **bucle de retroalimentación**.
    
    **Más vigilancia genera más arrestos**, justificando aún más vigilancia en el futuro. Este fenómeno puede perpetuar la **criminalización** de ciertas comunidades, especialmente las más vulnerables.
    
    Para entender mejor este fenómeno, vamos a ejecutar una simulación del modelo de **PredPol**: más vigilancia genera más arrestos, y esos arrestos justifican más vigilancia.
    """)

    # Simulación de PredPol: Bucle de retroalimentación
    barrio_vigilado = st.radio("¿Quieres aumentar la vigilancia en un barrio pobre?", ('Sí', 'No'))
    arrestos = 0

    if barrio_vigilado == 'Sí':
        arrestos = random.randint(5, 15)  # Número de arrestos iniciales
        st.write(f"🔴 Se han realizado **{arrestos} arrestos** en el barrio vigilado.")
        st.write("Esto justifica más presencia policial 🚔.")
        
        # Simulación de retroalimentación con un nuevo aumento de arrestos
        decision = st.radio("¿Deseas aumentar la vigilancia de nuevo?", ('Sí', 'No'))
        if decision == 'Sí':
            arrestos += random.randint(5, 15)  # Aumento en los arrestos
            st.write(f"🚔 Ahora se han realizado **{arrestos} arrestos**. El bucle de retroalimentación continúa...")
        else:
            st.write("🔵 Decidiste no aumentar la vigilancia, pero los arrestos iniciales ya generaron datos que refuerzan la percepción de criminalidad.")
    else:
        st.write("🟢 No aumentaste la vigilancia, el número de arrestos en la zona se mantiene bajo.")

    # Visualización de cómo cambia la vigilancia
    vigilancia_data = {'Vigilancia Baja': 100 - arrestos, 'Vigilancia Alta': arrestos}
    df = pd.DataFrame(list(vigilancia_data.items()), columns=["Estado de Vigilancia", "Cantidad"])

    st.bar_chart(df.set_index("Estado de Vigilancia"))

    # Relación con el presente: Conexión con PredPol y tecnologías modernas
    st.write("""
    **Reflexión moderna:**  
    Este fenómeno de **vigilancia predictiva** no es algo nuevo. Hoy en día, **algoritmos como PredPol** se utilizan en muchas ciudades del mundo para predecir patrones de criminalidad. Sin embargo, como en los ejemplos históricos, estas **tecnologías** **perpetúan sesgos**, especialmente en comunidades marginadas, lo que puede generar un círculo vicioso de **vigilancia y criminalización**.
    
    **PredPol** se basa en el análisis de datos históricos sobre crímenes para predecir dónde ocurrirán futuros delitos. Sin embargo, este modelo ha sido criticado por **reforzar estereotipos raciales** y **discriminar a ciertas comunidades**, especialmente aquellas que ya están sobrevigiladas.
    
    Así como los periódicos **realistas** de la época ayudaron a **moldear la percepción pública** a favor del orden colonial, hoy en día, **PredPol** y otros modelos similares **moldean la percepción de criminalidad** y perpetúan la **discriminación estructural**.
    """)

# Función principal para ejecutar la aplicación de Streamlit
def run():
    st.sidebar.title("📝 Navegar entre Secciones")
    option = st.sidebar.selectbox("Elige la sección que deseas ver:", 
                                  ("📰 Introducción", 
                                   "📜 Herramientas Metodológicas", 
                                   "📰 Los Periódicos Monárquicos", 
                                   "📊 Simulación de Opinión Pública", 
                                   "📈 Evolución de los Temas en los Periódicos", 
                                   "🔴 Criminalización de la Pobreza y PredPol", 
                                   "📝 Conclusión"))
    if option == "Introducción":
        slide_intro()
    elif option == "Herramientas Metodológicas":
        slide_hsc_metodologia()
    elif option == "Los Periódicos Monárquicos":
        slide_periodicos_monarquicos()
    elif option == "Simulación de Opinión Pública":
        slide_slider_opinion()
    elif option == "Evolución de los Temas en los Periódicos":
        slide_grafica_temporal()
    elif option == "¿Por qué es importante entenderlo hoy en día?":
        slide_criminalizacion()
    else:
        slide_conclusion()

if __name__ == "__main__":
    run()
