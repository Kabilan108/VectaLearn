"""Home Page for VectaLearn"""

import streamlit as st
import requests

from client import settings, set_user, get_user
from client.schema import NewUser, User
from client.components import nav_page


# --- Definitions --- #


# --- Sidebar --- #


# --- Page Config --- #
st.set_page_config(
    page_title="VectaLearn",
    page_icon="🧊",
)

st.write("# Welcome to VectaLearn! 👋")

st.markdown(
    """\
VectaLearn is a web app that helps you study for classes by givning you
an AI-powered study and research assistant.
"""
)


# --- Login / Register --- #

# redirect to docstore if already logged in
if get_user().user_id:
    nav_page("docstore")

tab_1, tab_2 = st.tabs(["Register", "Log In"])

with tab_1:
    with st.form(key="signup_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        full_name = st.text_input("Full Name")
        submit = st.form_submit_button(label="Sign Up")

        if submit:
            resp = requests.post(
                settings.get_endpoint("/user/signup"),
                json=NewUser(
                    email=email,
                    password=password,
                    full_name=full_name,
                ).model_dump(),
            )

            if resp.ok:
                set_user(resp.json()["user_id"], resp.json()["jwt"])
                st.success(resp.json()["message"])
                nav_page("docstore")
            else:
                st.error(resp.json()["detail"])

with tab_2:
    with st.form(key="signin_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button(label="Sign Up")

        if submit:
            resp = requests.post(
                settings.get_endpoint("/user/login"),
                json=User(
                    email=email,
                    password=password,
                ).model_dump(),
            )

            if resp.ok:
                set_user(resp.json()["user_id"], resp.json()["jwt"])
                st.success(resp.json()["message"])
                nav_page("docstore")
            else:
                st.error(resp.json()["detail"])
