import streamlit as st
import time

st.set_page_config(page_title="Funny Chat Prank", layout="centered")

if "state" not in st.session_state:
    st.session_state.state = "start"

def reset():
    st.session_state.state = "start"

st.title("😂 Funny Chat Prank")
st.write("Choose your reply and see what happens...")

if st.session_state.state == "start":
    st.write("What's up bro bro?")
    if st.button("a) Nothing much :("):
        st.session_state.state = "a1"
        st.experimental_rerun()
    if st.button("b) Just chilling"):
        st.session_state.state = "b"
        st.experimental_rerun()
    if st.button("c) I'm good"):
        st.session_state.state = "c"
        st.experimental_rerun()

elif st.session_state.state == "a1":
    st.write("Do you have something in mind?")
    if st.button("a) Yes"):
        st.session_state.state = "a_yes"
        st.experimental_rerun()
    if st.button("b) No"):
        st.session_state.state = "a_no"
        st.experimental_rerun()

elif st.session_state.state == "a_yes":
    st.write("What is it?")
    if st.button("a) NVM"):
        st.write("Inamo 😂")
        if st.button("Play again"):
            reset()
            st.experimental_rerun()
    if st.button("b) I like you"):
        st.write("Badinggg 😳")
        if st.button("Play again"):
            reset()
            st.experimental_rerun()

elif st.session_state.state == "a_no":
    st.write("Bro why so secretive 😏")
    if st.button("Back to start"):
        reset()
        st.experimental_rerun()

elif st.session_state.state == "b":
    st.write("Just chilling? Nice bro 😎")
    if st.button("Back to start"):
        reset()
        st.experimental_rerun()

elif st.session_state.state == "c":
    st.write("Good to hear that! 👍")
    if st.button("Back to start"):
        reset()
        st.experimental_rerun()
