import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.health_agent import get_health_agent

st.set_page_config(page_title="Health AI Assistant", page_icon="🩺", layout="wide")

st.markdown("""
<style>
    .stChatFloatingInputContainer {
        padding-bottom: 20px;
    }
    .main {
        background-color: #f8f9fa;
    }
    .stChatMessage {
        border-radius: 15px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("🩺 AI Health Agent")
    st.divider()
    st.markdown("### Patient Profile (Optional)")
    age = st.number_input("Age", min_value=1, max_value=120, value=25)
    weight = st.number_input("Weight (kg)", min_value=1, max_value=500, value=70)
    height = st.number_input("Height (cm)", min_value=1, max_value=300, value=175)
    gender = st.selectbox("Gender", ["Male", "Female"])
    
    st.divider()
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
        
    st.info("I am an AI, not a doctor. Please consult a healthcare professional for medical advice.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if "agent_executor" not in st.session_state:
    st.session_state.agent_executor = get_health_agent()

if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            enhanced_input = f"I am a {age} year old {gender}, weight {weight}kg, height {height}cm. {prompt}"
            
            with st.spinner("Thinking..."):
                response = st.session_state.agent_executor.invoke({"input": enhanced_input})
                full_response = response["output"]
            
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            import traceback
            st.error(f"Error: {str(e)}")
            st.code(traceback.format_exc())
            st.info("Check if your GROQ_API_KEY is correct in the .env file and ensure all langchain packages are installed correctly.")
