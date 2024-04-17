import streamlit as st

html_code = """
<a href="https://slack.com/oauth/v2/authorize?client_id=6905513379156.6888498157463&scope=chat:write,im:write,incoming-webhook&user_scope=admin,identity.basic"><img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcSet="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" /></a>
"""

st.markdown(html_code, unsafe_allow_html=True)