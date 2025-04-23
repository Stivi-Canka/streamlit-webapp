import streamlit as st

configuration_settings = st.Page(
    page=r"C:\Users\stivi\Documents\Python Practice\streamlit_app\pages\configuration_settings.py",
    title="Configuration Settings",
    icon=":material/settings:",
    default=True
)

display_elements = st.Page(
    page=r"C:\Users\stivi\Documents\Python Practice\streamlit_app\pages\display_elements.py",
    title="Display Elements",
    icon=":material/display_settings:",
)

input_elements = st.Page(
    page=r"C:\Users\stivi\Documents\Python Practice\streamlit_app\pages\input_elements.py",
    title="Input Elements",
    icon=":material/input_circle:",
)

application_logic = st.Page(
    page=r"C:\Users\stivi\Documents\Python Practice\streamlit_app\pages\application_logic.py",
    title="Application Logic",
    icon=":material/cognition:",
)

output_elements = st.Page(
    page=r"C:\Users\stivi\Documents\Python Practice\streamlit_app\pages\output_elements.py",
    title="Output Elements",
    icon=":material/output_circle:", ###
)

if "is_adult" not in st.session_state:
    st.session_state.is_adult = False
    
if "old_incident" not in st.session_state:
    st.session_state.old_incident = False

pg = st.navigation(pages= [configuration_settings, display_elements, input_elements, output_elements, application_logic])

pg.run()