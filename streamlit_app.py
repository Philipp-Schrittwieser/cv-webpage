import streamlit as st

left, right = st.columns(2)

left.image("picture.jpg", width=250)

right.header("Vorname Nachname")

st.header("IT-Kompetenzen", anchor=False, divider="blue")

st.write("""
            - 🐈 Webentwicklung: Fundierte Grundkenntnisse in HTML, CSS und Streamlit (Fullstack-Framework)
            - 🐈 Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
            - 🐈 Office-Suite: Versierter Umgang mit Microsoft Word, Excel und PowerPoint
            - 🐈 Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
            - 🐈 Erstellung datenbasierter Präsentationen und interaktiver Tabellenkalkulationen
            """)