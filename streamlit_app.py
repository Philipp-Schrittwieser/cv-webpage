import streamlit as st
from pathlib import Path


st.markdown("<style> .stAppHeader {display:none;} ul {list-style-type: none; } </style>", unsafe_allow_html=True)

def get_file_content_as_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()

# Pfad zur PDF-Datei
file_path = 'test.pdf'

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)

left, right = st.columns(2)

left.image("profile-pic.png", width=250)

with right:
    st.markdown("""
                <h3>Philipp Schrittwieser</h3>
                <em>Ich bin davon überzeugt, dass KI die Welt verändern wird
                und ich möchte ein Teil davon sein.</em>
                """, unsafe_allow_html=True)

    st.download_button(
            label="📄 Download Lebenslauf",
            data=file_bytes,
            file_name=file_path,
            mime='application/pdf'
    )

    st.write("📩", "philipp.schrittwieser@edu.magwien.gv.at")

st.header("IT-Kompetenzen", anchor=False, divider="blue")

st.write("""
            - 🐈 Webentwicklung: Fundierte Grundkenntnisse in HTML, CSS und Streamlit (Fullstack-Framework)
            - 🐈 Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
            - 🐈 Office-Suite: Versierter Umgang mit Microsoft Word, Excel und PowerPoint
            - 🐈 Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
            - 🐈 Erstellung datenbasierter Präsentationen und interaktiver Tabellenkalkulationen
            """)