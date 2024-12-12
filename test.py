import streamlit as st


left, right = st.columns(2)

with left:
    st.header("Hallo")

with right:
    st.header("Bye")




left, right = st.columns(2)

left.header("Neu Links")
right.header("Neu Rechts")







st.title("Große Überschrift", anchor=False)
st.header("Kleiner", anchor=False, divider=True)
st.subheader("Noch kleiner", anchor=False, divider=True)
st.write("Webseite von Marcel")
st.image("https://cdn.britannica.com/70/234870-050-D4D024BB/Orange-colored-cat-yawns-displaying-teeth.jpg")
st.video("https://www.youtube.com/watch?v=NZBdCPMrIvA")

st.title("Mein Gemütszustand", anchor=False)
st.header("Das ist ein Text", anchor=False, divider=True)
st.subheader("Noch ein Text", anchor=False, divider=True)
st.write("Heute gehts mir gut")

st.title("Ich esse gerne", anchor=False)
st.header("Schokolade", anchor=False, divider=True)
st.subheader("Unterüberschrift", anchor=False, divider=True)
st.write("Ich hab Schokolade")

st.title("Noch eine Überschrift", anchor=False)
st.header("Hallo", anchor=False, divider=True)
st.subheader("Hi", anchor=False, divider=True)
st.write("IT ist manchmal verwirrend")

st.title("Heyjo", anchor=False)
st.header("Hi", anchor=False, divider=True)
st.subheader("Text", anchor=False, divider=True)
st.write("Ich bin gespannt")

st.title("Hallo", anchor=False)
st.header("Hi", anchor=False, divider=True)
st.subheader("Hello", anchor=False, divider=True)
st.write("Cool, dass das so einfach geht")