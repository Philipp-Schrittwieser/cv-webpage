import streamlit as st

st.title("My new app ❤️", anchor=False)
st.header("Ich bin eine neue Überschrift 🐾", anchor=False)
st.subheader("Noch eine kleinere Überschrift 🐈", anchor=False)
st.write("Das ist meine Streamlit-App ")

st.markdown("<p>Ich bin ein Text</p>", unsafe_allow_html=True)

st.markdown("<a href='https://www.google.at'>Link</a>", unsafe_allow_html=True)

st.header("IT-Kompetenzen", anchor=False, divider="blue")

st.write("""
            - 🐈 Webentwicklung: Fundierte Grundkenntnisse in HTML, CSS und Streamlit (Fullstack-Framework)
            - 🐈 Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
            - 🐈 Office-Suite: Versierter Umgang mit Microsoft Word, Excel und PowerPoint
            - 🐈 Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
            - 🐈 Erstellung datenbasierter Präsentationen und interaktiver Tabellenkalkulationen
            """)