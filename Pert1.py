from openai import OpenAI
import streamlit as st
import time


assistant_id ='asst_4KJkQ5Kh2g0gGdO44erxMv0k'
thread_id = ""


with st.sidebar:
    st.header("미토콘드리아 AiXpert Ver.1.0 ")
    st.subheader("GPT 4/ assitant", divider = "rainbow")
    st.text("by Won Hur, wonhurk@gmail.com")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")

    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

    client = OpenAI(api_key=openai_api_key)
    
#    thread = client.beta.threads.create()
#    thread_id = thread.id
    thread_id ="thread_CNDqQBZr0Dm9tZmbkXAglXna"
    st.text("start a new thread")
    st.info(thread_id)


st.title("💬 미토콘드리아 AiXpert")
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)


#     if not openai_api_key:
#         st.info("Please add your OpenAI API key to continue.")
#         st.stop()

#     if not thread_id:
#         st.info("Please add your Thread ID to continue.")
#         st.stop()


    thread_message = client.beta.threads.messages.create(
        thread_id,
        role="user",
        content=prompt,
        )
#       print(thread_message)

    run = client.beta.threads.runs.create(
        thread_id = thread_id,
        assistant_id = assistant_id
        )
#    print(run)

    run_id = run.id

    while True:
        run = client.beta.threads.runs.retrieve(
            thread_id = thread_id,
            run_id = run_id
            ) 
        if run.status == "completed":
            break
        else:
            time.sleep(3)
            
    print(run)


    thread_message = client.beta.threads.messages.list(thread_id)
    print(thread_message.data)

    msg = thread_message.data[0].content[0].text.value
    print(msg)

    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)