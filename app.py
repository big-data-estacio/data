# from client.src.pages.👻_Login import login_page
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'client', 'src', 'pages')))
# from login import login_page
# from client.pages.login import login_page
from client.src.pages.login import *
import streamlit as st
import client.setup as setup
import plotly.express as px


if __name__ == '__main__':
  df = px.data.iris()

  if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

  if not st.session_state.logged_in:
    logged_in = login_page()

    if logged_in:
        st.session_state.logged_in = True
        st.experimental_rerun()
  else:
    st.empty()
    setup.mainLogin()
    if st.button("Logout"):
      st.session_state.logged_in = False
      st.experimental_rerun()
      