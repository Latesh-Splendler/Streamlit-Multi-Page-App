import streamlit as st

st.title('🎈 App Name')
about_page = st.Page(
  page="views/about_me.py",
  title="About Me",
  icon=":material/account_circle:",
  default=True,
)
project_1_page = st.Page(
  page = "views/sales_dashboard.py",
  title="Sales Dashboard",
  icon=":material/bar_chart:",
)
project_2_page = st.Page(
  page="views/chatbot.py",
  title="Chat Bot"
  icon=":material/smart_toy:",
)

pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

pg.run()
