# NuevaMente Renaissance

**Product evolution of NuevaMente focused on clarity, learning, traceability and craft.**

NuevaMente Renaissance es una línea independiente de evolución del producto NuevaMente. Su objetivo es transformar el prototipo inicial en un producto llave en mano, con una arquitectura clara, trazabilidad pedagógica, y una interfaz contemporánea, despojada de "dashboarditis" o métricas sintéticas.

## 🧬 Genealogía Técnica

Este repositorio nace como un fork conceptual y técnico de la línea base ("Shadow"):

- **Origin:** `mmorfe-engineer/nuevamente_g10_latam`
- **Baseline:** `shadow-baseline-2026-09-28`
- **Origin commit:** `a8c04820f49f8afeff33c24f87af09bd69cba3bf`

Renaissance hereda la arquitectura fundamental (ingestión RAG, almacenamiento conmutable local/S3, generación LLM), pero busca la excelencia artesanal (craft) en la interacción humana y la claridad visual.

## 🏛️ Principios de Renaissance

1. **Renovación sin destrucción:** Construir sobre la arquitectura validada sin perder las capacidades fundamentales.
2. **Producto llave en mano:** Entregables sólidos, funcionales y autosuficientes.
3. **Claridad:** Diseño sobrio, estructurado y orientado al contenido.
4. **Aprendizaje:** La interfaz debe asistir al proceso de estudio, no entorpecerlo.
5. **Trazabilidad:** Cada generación y adaptación RAG debe estar conectada a su fuente original de manera auditable.
6. **Craft:** Atención al detalle en la tipografía, los espacios, los estados de carga y la experiencia final del usuario (UX/UI clara y contemporánea).
7. **No "techno oscura" ni "dashboarditis":** Evitar la saturación visual innecesaria. Cero métricas falsas o estados simulados presentados como reales.

## 🚀 Guía de Inicio Rápido

```bash
# 1. Clonar el repositorio Renaissance
git clone https://github.com/mmorfe-engineer/nuevamente_renaissance.git
cd nuevamente_renaissance

# 2. Entorno virtual e instalación de dependencias
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Configuración de entorno
cp .env.example .env

# 4. Ejecutar la suite de pruebas heredada
pytest tests/ -v

# 5. Levantar la aplicación
streamlit run ui/app.py
```
