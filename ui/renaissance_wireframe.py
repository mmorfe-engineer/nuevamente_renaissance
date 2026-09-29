import streamlit as st

# Configuración estructural y neutral
st.set_page_config(
    page_title="Renaissance Wireframe",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estado de Navegación
if "ren_view" not in st.session_state:
    st.session_state.ren_view = "HOME"
if "ren_doc_uploaded" not in st.session_state:
    st.session_state.ren_doc_uploaded = False
if "ren_show_flashcards" not in st.session_state:
    st.session_state.ren_show_flashcards = False
if "ren_show_source" not in st.session_state:
    st.session_state.ren_show_source = False

def nav_to(view: str):
    st.session_state.ren_view = view
    st.session_state.ren_show_flashcards = False
    st.session_state.ren_show_source = False

# --- GLOBAL NAVIGATION ---
with st.container():
    col_brand, col_nav, col_spacer = st.columns([2, 6, 2])
    with col_brand:
        if st.button("NuevaMente", key="nav_home", type="tertiary" if hasattr(st, 'button') else "primary"):
            nav_to("HOME")
            st.rerun()
    with col_nav:
        st.markdown(
            "<div style='padding-top: 8px;'><a href='#' style='text-decoration: none; color: inherit;'>Mis materiales</a> &nbsp;&nbsp;|&nbsp;&nbsp; <a href='#' style='text-decoration: none; color: inherit; font-weight: bold;'>Estudiar</a></div>", 
            unsafe_allow_html=True
        )
st.divider()

view = st.session_state.ren_view

# =====================================================================
# 1. HOME
# =====================================================================
if view == "HOME":
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Complejidad afuera. Claridad adentro.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #555;'>De un documento complejo a material de estudio verificable en minutos.</p>", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_spacer1, col_action, col_spacer2 = st.columns([4, 2, 4])
    with col_action:
        if st.button("Subir documento", use_container_width=True, type="primary"):
            nav_to("CREATION_FLOW")
            st.rerun()

# =====================================================================
# 2. CREATION FLOW (Document -> Adapt -> Processing)
# =====================================================================
elif view == "CREATION_FLOW":
    st.header("Preparar material")
    
    # Etapa Documento
    st.subheader("1. Documento", divider="gray")
    uploaded = st.file_uploader("Arrastra tu archivo aquí", type=["pdf", "txt", "md"])
    if uploaded:
        st.session_state.ren_doc_uploaded = True
        st.success(f"Archivo listo: {uploaded.name}")
        
    # Etapa Adaptación
    st.subheader("2. Adaptación", divider="gray")
    col_nivel, col_formato, col_prof = st.columns(3)
    with col_nivel:
        st.selectbox("Nivel", ["Fundamentos", "Técnico intermedio", "Avanzado"])
    with col_formato:
        st.selectbox("Formato de estudio", ["Explicación conceptual", "Guía práctica", "Resumen"])
    with col_prof:
        st.selectbox("Profundidad", ["Esencial", "Detallada", "Exhaustiva"])
        
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Procesar material", type="primary", disabled=not st.session_state.ren_doc_uploaded):
        nav_to("PROCESSING")
        st.rerun()

# =====================================================================
# 3. PROCESSING
# =====================================================================
elif view == "PROCESSING":
    st.header("Transformando Documento")
    
    st.info("Estado del sistema: Ejecutando Ingestión y RAG")
    
    st.markdown("""
    * Representación de estados reales (simulación estructural):
    1. ✅ Extrayendo texto original...
    2. ⏳ Estructurando conceptos...
    3. ⏳ Generando adaptación...
    """)
    
    st.progress(33)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Simular fin de procesamiento (Ir a Workspace)", type="primary"):
        nav_to("STUDY_WORKSPACE")
        st.rerun()

# =====================================================================
# 4. STUDY WORKSPACE (incluye Flashcards y Source Panel opcional)
# =====================================================================
elif view == "STUDY_WORKSPACE":
    
    # 4.A FLASHCARDS (Overlay / Cambio de modo)
    if st.session_state.ren_show_flashcards:
        st.header("Flashcards: Repaso Activo")
        
        st.markdown("---")
        st.markdown("### ¿Cuál es la principal ventaja de la arquitectura Hexagonal?")
        
        if st.checkbox("Mostrar respuesta"):
            st.success("Permite aislar la lógica de dominio de los detalles de infraestructura (bases de datos, APIs externas), facilitando el testing y la intercambiabilidad de componentes.")
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Ver fuente contextual"):
                st.info("Fuente: Architecture.md, sección 3.1.2")
                
            st.markdown("---")
            col_eval1, col_eval2, col_eval3 = st.columns([1, 1, 4])
            with col_eval1:
                st.button("Revisar después")
            with col_eval2:
                st.button("Lo entendí", type="primary")
                
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if st.button("← Volver al Workspace"):
            st.session_state.ren_show_flashcards = False
            st.rerun()
            
    # 4.B MAIN WORKSPACE
    else:
        # Layout responsivo: Materiales | Contenido | Fuente (opcional)
        if st.session_state.ren_show_source:
            col_mat, col_content, col_source = st.columns([2, 5, 3])
        else:
            col_mat, col_content = st.columns([2, 8])
            col_source = None
            
        with col_mat:
            st.markdown("### Materiales")
            st.markdown("- **Guía conceptual**\n- Resumen ejecutivo")
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Repasar Flashcards", use_container_width=True):
                st.session_state.ren_show_flashcards = True
                st.rerun()
                
        with col_content:
            st.markdown("## Arquitectura Hexagonal en Python")
            st.markdown("""
            La arquitectura hexagonal, también conocida como arquitectura de puertos y adaptadores, es un patrón de diseño arquitectónico de software.
            
            El objetivo principal es lograr una estricta separación de responsabilidades. La lógica de negocio principal se aísla en el centro del hexágono.
            """)
            
            if st.button("Ver fuente", key="src_1"):
                st.session_state.ren_show_source = True
                st.rerun()
                
            st.markdown("""
            Los adaptadores externos, como bases de datos o interfaces de usuario, interactúan con el centro a través de puertos. 
            Esto hace que la aplicación sea agnóstica respecto a sus dependencias externas.
            """)
            
        if col_source is not None:
            with col_source:
                st.markdown("### Fuente")
                st.info("""
                **Archivo:** pattern_guide.pdf  
                **Sección:** Introduction to Hexagonal Architecture  
                
                *Fragmento:*  
                "Hexagonal architecture divides the system into loosely-coupled interchangeable components, such as the application core, the database, the user interface..."
                """)
                if st.button("Cerrar fuente"):
                    st.session_state.ren_show_source = False
                    st.rerun()
