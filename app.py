import streamlit as st
from ai_service import get_chatbot_response

st.set_page_config(
    page_title="ALI KARYANA STORE",
    page_icon="🛒"
)

st.title("🛒 ALI KARYANA STORE")
st.subheader("Your Smart Grocery Shopping Assistant")

st.write("Ask me about grocery products, prices and availability.")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Customer message input
user_message = st.chat_input("Type your message here...")

if user_message:
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    with st.chat_message("user"):
        st.write(user_message)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer = get_chatbot_response(
                    user_message,
                    st.session_state.messages[:-1]
                )
                st.write(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:
                st.error(f"Something went wrong: {e}")