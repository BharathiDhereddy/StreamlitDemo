import streamlit as st
st.title('Day2 Challenge')
st.header('About button')
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('goodbye')