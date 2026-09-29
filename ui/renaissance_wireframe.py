import streamlit as st

# =====================================================================
# WIREFRAME_SAMPLE_DATA
# =====================================================================
WIREFRAME_SAMPLE_DATA = {
    "document_name": "pattern_guide.pdf",
    "study_title": "Arquitectura Hexagonal en Python",
    "study_text_1": "La arquitectura hexagonal, también conocida como arquitectura de puertos y adaptadores, es un patrón de diseño arquitectónico de software. El objetivo principal es lograr una estricta separación de responsabilidades. La lógica de negocio principal se aísla en el centro del hexágono.",
    "study_text_2": "Los adaptadores externos, como bases de datos o interfaces de usuario, interactúan con el centro a través de puertos. Esto hace que la aplicación sea agnóstica respecto a sus dependencias externas.",
    "flashcard_question": "¿Cuál es la principal ventaja de la arquitectura Hexagonal?",
    "flashcard_answer": "Permite aislar la lógica de dominio de los detalles de infraestructura (bases de datos, APIs externas), facilitando el testing y la intercambiabilidad de componentes.",
    "source_file": "pattern_guide.pdf",
    "source_section": "Introduction to Hexagonal Architecture",
    "source_fragment": "\"Hexagonal architecture divides the system into loosely-coupled interchangeable components, such as the application core, the database, the user interface...\""
}

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
# Tracking state of dead interactions locally
if "ren_flashcard_shown" not in st.session_state:
    st.session_state.ren_flashcard_shown = False
if "ren_flashcard_graded" not in st.session_state:
    st.session_state.ren_flashcard_graded = False

def nav_to(view: str):
    st.session_state.ren_view = view
    st.session_state.ren_show_flashcards = False
    st.session_state.ren_show_source = False
    st.session_state.ren_flashcard_shown = False
    st.session_state.ren_flashcard_graded = False

# --- GLOBAL NAVIGATION ---
with st.container():
    col_brand, col_nav, col_spacer = st.columns([2, 6, 2])
    with col_brand:
        if st.button("NuevaMente", key="nav_home", type="tertiary" if hasattr(st, 'button') else "primary"):
            nav_to("HOME")
            st.rerun()
    with col_nav:
        st.markdown(
            "<div style='padding-top: 8px;'><span style='color: gray;'>Mis materiales (WIP)</span> &nbsp;&nbsp;|&nbsp;&nbsp; <span style='font-weight: bold;'>Estudiar</span></div>", 
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
    st.header("Procesando tu documento")
    
    st.info("Estado estructural: Conexión a pipeline inactiva en wireframe")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Avanzar a Workspace (Solo para Wireframe)", type="primary"):
        nav_to("STUDY_WORKSPACE")
        st.rerun()

# =====================================================================
# 4. STUDY WORKSPACE (incluye Flashcards y Source Panel opcional)
# =====================================================================
elif view == "STUDY_WORKSPACE":
    
    # 4.A Layout responsivo: Materiales | Contenido | Fuente (opcional)
    if st.session_state.ren_show_source:
        col_mat, col_content, col_source = st.columns([2, 5, 3])
    else:
        col_mat, col_content = st.columns([2, 8])
        col_source = None

    # Panel izquierdo (Materiales)
    with col_mat:
        st.markdown("### Materiales")
        st.markdown("- **Guía conceptual**\n- Resumen (WIP)")
        
        st.markdown("<br>", unsafe_allow_html=True)
        # Cambio: En lugar de un button que re-renderice solo la col, cambia modo
        if st.button("Repasar Flashcards", use_container_width=True, disabled=st.session_state.ren_show_flashcards):
            st.session_state.ren_show_flashcards = True
            st.rerun()
        if st.session_state.ren_show_flashcards:
            if st.button("Volver al documento", use_container_width=True):
                st.session_state.ren_show_flashcards = False
                st.rerun()

    # Contenido principal (Workspace texto o Flashcards)
    with col_content:
        if st.session_state.ren_show_flashcards:
            st.header("Flashcards: Repaso Activo")
            st.markdown("---")
            st.markdown(f"### {WIREFRAME_SAMPLE_DATA['flashcard_question']}")
            
            if not st.session_state.ren_flashcard_shown:
                if st.button("Mostrar respuesta"):
                    st.session_state.ren_flashcard_shown = True
                    st.rerun()
            else:
                st.success(WIREFRAME_SAMPLE_DATA['flashcard_answer'])
                st.markdown("<br>", unsafe_allow_html=True)
                
                if st.button("Ver fuente", key="btn_src_fc"):
                    st.session_state.ren_show_source = not st.session_state.ren_show_source
                    st.rerun()
                    
                st.markdown("---")
                if not st.session_state.ren_flashcard_graded:
                    col_eval1, col_eval2, col_eval3 = st.columns([1, 1, 4])
                    with col_eval1:
                        if st.button("Revisar después"):
                            st.session_state.ren_flashcard_graded = True
                            st.rerun()
                    with col_eval2:
                        if st.button("Lo entendí", type="primary"):
                            st.session_state.ren_flashcard_graded = True
                            st.rerun()
                else:
                    st.info("Calificación registrada (WIP). Fin del mazo de prueba.")
                    if st.button("Reiniciar mazo"):
                        st.session_state.ren_flashcard_shown = False
                        st.session_state.ren_flashcard_graded = False
                        st.rerun()
        else:
            # MAIN STUDY WORKSPACE (Texto normal)
            st.markdown(f"## {WIREFRAME_SAMPLE_DATA['study_title']}")
            st.markdown(WIREFRAME_SAMPLE_DATA['study_text_1'])
            
            if st.button("Ver fuente", key="btn_src_doc"):
                st.session_state.ren_show_source = not st.session_state.ren_show_source
                st.rerun()
                
            st.markdown(WIREFRAME_SAMPLE_DATA['study_text_2'])

    # Panel derecho (Source)
    if col_source is not None:
        with col_source:
            st.markdown("### Fuente")
            st.info(f"""
            **Archivo:** {WIREFRAME_SAMPLE_DATA['source_file']}  
            **Sección:** {WIREFRAME_SAMPLE_DATA['source_section']}  
            
            *Fragmento:*  
            {WIREFRAME_SAMPLE_DATA['source_fragment']}
            """)
            if st.button("Cerrar fuente", key="btn_close_src"):
                st.session_state.ren_show_source = False
                st.rerun()
