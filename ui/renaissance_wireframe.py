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

# Configuración estructural
st.set_page_config(
    page_title="NuevaMente Renaissance",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================================
# DESIGN SYSTEM BASE (CSS Tokens & Typography)
# =====================================================================
st.markdown("""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Lora:ital,wght@0,400;0,600;1,400&display=swap');

    :root {
        /* Color Palette */
        --canvas: #FCFCF9; /* Claro, ligeramente cálido */
        --surface: #FFFFFF;
        --surface-alt: #F4F4F1;
        
        --ink: #111110;
        --ink-muted: #555552;
        --ink-faint: #999995;
        
        --brand: #2E5C8A;
        --brand-subtle: #E6F0FA;
        --brand-strong: #1A3A5C;
        
        --success: #287A4F;
        --warning: #B37700;
        --critical: #C92A2A;
        --info: #0066CC;
        
        --source: #6B4C9A;
        --source-subtle: #F3EEFA;
        
        --border: #E5E5E2;
        --focus: rgba(46, 92, 138, 0.4);
        
        /* Typography */
        --font-ui: 'Inter', sans-serif;
        --font-editorial: 'Lora', serif;
        
        --spacing-4: 0.25rem;
        --spacing-8: 0.5rem;
        --spacing-16: 1rem;
        --spacing-24: 1.5rem;
        --spacing-32: 2rem;
        --spacing-48: 3rem;
        --spacing-64: 4rem;
        
        --radius-sm: 4px;
        --radius-md: 8px;
        --radius-lg: 12px;
    }

    /* Global Overrides for Streamlit */
    .stApp {
        background-color: var(--canvas);
        color: var(--ink);
        font-family: var(--font-ui);
    }

    /* Typography Hierarchy */
    h1, .display { font-family: var(--font-editorial); font-weight: 600; color: var(--ink); letter-spacing: -0.02em; }
    h2 { font-family: var(--font-editorial); font-weight: 600; color: var(--ink); }
    h3 { font-family: var(--font-ui); font-weight: 600; color: var(--ink); }
    p, .body-text { font-family: var(--font-ui); line-height: 1.6; color: var(--ink-muted); max-width: 70ch; }
    
    /* Cards */
    .rn-card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: var(--spacing-32);
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    
    /* CTA */
    .stButton > button {
        border-radius: var(--radius-md) !important;
        font-family: var(--font-ui) !important;
        font-weight: 500 !important;
    }
</style>
""", unsafe_allow_html=True)

# Estado de Navegación
if "ren_view" not in st.session_state:
    st.session_state.ren_view = "HOME"
if "ren_doc_uploaded" not in st.session_state:
    st.session_state.ren_doc_uploaded = False
if "ren_show_flashcards" not in st.session_state:
    st.session_state.ren_show_flashcards = False
if "ren_show_source" not in st.session_state:
    st.session_state.ren_show_source = False
if "ren_flashcard_shown" not in st.session_state:
    st.session_state.ren_flashcard_shown = False
if "ren_flashcard_graded" not in st.session_state:
    st.session_state.ren_flashcard_graded = False

# Estados de Creación Persistentes
if "cf_nivel" not in st.session_state:
    st.session_state.cf_nivel = "Fundamentos"
if "cf_formato" not in st.session_state:
    st.session_state.cf_formato = "Guía"
if "cf_prof" not in st.session_state:
    st.session_state.cf_prof = "Esencial"

def nav_to(view: str):
    st.session_state.ren_view = view

# --- GLOBAL NAVIGATION ---
with st.container():
    col_brand, col_nav, col_spacer = st.columns([2, 6, 2])
    with col_brand:
        st.markdown("<div style='font-family: var(--font-editorial); font-size: 1.2rem; font-weight: 600; padding-top: 6px; cursor: pointer;'>NuevaMente</div>", unsafe_allow_html=True)
        if st.button("Inicio", key="nav_home"):
            nav_to("HOME")
            st.rerun()
    with col_nav:
        st.markdown(
            "<div style='padding-top: 12px; font-family: var(--font-ui); color: var(--ink-muted);'>"
            "<span style='color: var(--ink-faint); font-size: 0.85em; text-transform: uppercase; letter-spacing: 0.05em;'>Modo actual:</span> <span style='font-weight: 600; color: var(--ink); margin-left: 8px;'>Estudio</span>"
            "</div>", 
            unsafe_allow_html=True
        )
st.markdown("<hr style='margin: 0; border-color: var(--border);'>", unsafe_allow_html=True)

view = st.session_state.ren_view

# =====================================================================
# 1. HOME
# =====================================================================
if view == "HOME":
    st.markdown("<div style='padding-top: var(--spacing-64); padding-bottom: var(--spacing-32);'>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 3rem;'>Convierte cualquier documento técnico<br>en material que realmente puedas estudiar.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.25rem; color: var(--ink-muted); margin: 0 auto; max-width: 600px;'>Sube tu documento, elige cómo quieres aprender y recibe material adaptado a tu nivel, vinculado a la fuente original.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    col_spacer1, col_action, col_spacer2 = st.columns([4, 3, 4])
    with col_action:
        if st.button("Subir un documento", use_container_width=True, type="primary"):
            nav_to("CREATION_FLOW")
            st.rerun()
        # CTA Secundario "Ver cómo funciona" eliminado temporalmente (evita control muerto)

    st.markdown("<div style='padding-top: var(--spacing-64);'></div>", unsafe_allow_html=True)
    
    col_feat1, col_feat2, col_feat3 = st.columns(3)
    with col_feat1:
        st.markdown("<div class='rn-card'><h3 style='margin-top:0;'>Aprende a tu nivel</h3><p class='body-text'>El sistema adapta la profundidad técnica y el tono según tu perfil.</p></div>", unsafe_allow_html=True)
    with col_feat2:
        st.markdown("<div class='rn-card'><h3 style='margin-top:0;'>Estudia como prefieras</h3><p class='body-text'>Flashcards, guías paso a paso o resúmenes ejecutivos a demanda.</p></div>", unsafe_allow_html=True)
    with col_feat3:
        st.markdown("<div class='rn-card'><h3 style='margin-top:0;'>Comprueba de dónde salió</h3><p class='body-text'>Trazabilidad absoluta. Cada concepto está anclado a un fragmento de tu documento.</p></div>", unsafe_allow_html=True)

# =====================================================================
# 2. CREATION FLOW
# =====================================================================
elif view == "CREATION_FLOW":
    st.markdown("<div style='padding-top: var(--spacing-32);'>", unsafe_allow_html=True)
    st.markdown("<h2>¿Qué quieres estudiar hoy?</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='rn-card'>", unsafe_allow_html=True)
    st.markdown("<h3>Documento</h3>", unsafe_allow_html=True)
    uploaded = st.file_uploader("", type=["pdf", "txt", "md"])
    if uploaded:
        st.session_state.ren_doc_uploaded = True
        st.success(f"Documento cargado: {uploaded.name}")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div style='padding-top: var(--spacing-24);'></div>", unsafe_allow_html=True)
    
    if st.session_state.ren_doc_uploaded:
        st.markdown("<div class='rn-card'>", unsafe_allow_html=True)
        col_nivel, col_formato, col_prof = st.columns(3)
        with col_nivel:
            st.markdown("<h3>¿Para quién es?</h3>", unsafe_allow_html=True)
            st.session_state.cf_nivel = st.radio("Nivel", ["Fundamentos", "Intermedio", "Avanzado"], index=["Fundamentos", "Intermedio", "Avanzado"].index(st.session_state.cf_nivel), label_visibility="collapsed")
        with col_formato:
            st.markdown("<h3>¿Cómo quieres estudiarlo?</h3>", unsafe_allow_html=True)
            st.session_state.cf_formato = st.radio("Formato", ["Guía", "Flashcards", "Resumen"], index=["Guía", "Flashcards", "Resumen"].index(st.session_state.cf_formato), label_visibility="collapsed")
        with col_prof:
            st.markdown("<h3>¿Qué profundidad necesitas?</h3>", unsafe_allow_html=True)
            st.session_state.cf_prof = st.radio("Profundidad", ["Esencial", "Equilibrada", "Profunda"], index=["Esencial", "Equilibrada", "Profunda"].index(st.session_state.cf_prof), label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='padding-top: var(--spacing-32);'></div>", unsafe_allow_html=True)
        col_space, col_cta = st.columns([7, 3])
        with col_cta:
            if st.button("CREAR MI MATERIAL", type="primary", use_container_width=True):
                nav_to("PROCESSING")
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================================
# 3. PROCESSING
# =====================================================================
elif view == "PROCESSING":
    st.markdown("<div style='padding-top: var(--spacing-64); max-width: 600px; margin: 0 auto; text-align: center;'>", unsafe_allow_html=True)
    st.markdown("<h2>Procesando tu documento</h2>", unsafe_allow_html=True)
    st.info("Estado estructural: Conexión a pipeline inactiva en wireframe")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Ir al Workspace (Transición Manual del Prototipo)", type="primary"):
        nav_to("STUDY_WORKSPACE")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================================
# 4. STUDY WORKSPACE (incluye Flashcards y Source Panel opcional)
# =====================================================================
elif view == "STUDY_WORKSPACE":
    
    if st.session_state.ren_show_source:
        col_mat, col_content, col_source = st.columns([2, 5, 3])
    else:
        col_mat, col_content = st.columns([2, 8])
        col_source = None

    with col_mat:
        st.markdown("### Materiales")
        st.markdown("- **Guía conceptual**\n- Resumen")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if not st.session_state.ren_show_flashcards:
            if st.button("Repasar Flashcards", use_container_width=True):
                st.session_state.ren_show_flashcards = True
                st.rerun()
        else:
            if st.button("Volver al documento", use_container_width=True):
                st.session_state.ren_show_flashcards = False
                st.rerun()

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
                    st.info("Calificación registrada. Fin del mazo de prueba.")
                    if st.button("Reiniciar mazo"):
                        st.session_state.ren_flashcard_shown = False
                        st.session_state.ren_flashcard_graded = False
                        st.rerun()
        else:
            st.markdown(f"## {WIREFRAME_SAMPLE_DATA['study_title']}")
            st.markdown(f"<p class='body-text'>{WIREFRAME_SAMPLE_DATA['study_text_1']}</p>", unsafe_allow_html=True)
            
            if st.button("Ver fuente", key="btn_src_doc"):
                st.session_state.ren_show_source = not st.session_state.ren_show_source
                st.rerun()
                
            st.markdown(f"<p class='body-text'>{WIREFRAME_SAMPLE_DATA['study_text_2']}</p>", unsafe_allow_html=True)

    if col_source is not None:
        with col_source:
            st.markdown("### Fuente")
            st.info(f"**Archivo:** {WIREFRAME_SAMPLE_DATA['source_file']}  \n**Sección:** {WIREFRAME_SAMPLE_DATA['source_section']}  \n\n*Fragmento:*  \n{WIREFRAME_SAMPLE_DATA['source_fragment']}")
            if st.button("Cerrar fuente", key="btn_close_src"):
                st.session_state.ren_show_source = False
                st.rerun()
