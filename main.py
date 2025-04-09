import streamlit as st
import os
from groq import Groq
from examples import examples

api_key = os.environ.get("GROQ_API_KEY")

# Check if the API key exists
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set")

# Initialize the client with the API key
client = Groq(
    api_key=api_key
)

st.title("SQL buddy ˶ᵔ ᵕ ᵔ˶")

# Function to find matching query template from examples
def find_matching_query_template(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input_lower = user_input.lower().strip()

    for example in examples:
        if example["input"].lower().strip() in user_input_lower or user_input_lower in example["input"].lower().strip():
            return example["query"]

    # Return None if no match is found
    return None

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Check if the prompt matches any example template
    matching_query_template = find_matching_query_template(prompt)

    # Open website with specific Chrome profile using Selenium
    def open_website():
        try:
            # Prepare the final prompt
            if matching_query_template:
                # If we have a matching template, append the user's prompt to it
                final_prompt = matching_query_template + prompt
                # st.info("Using matching template for the prompt")
            else:
                # Default case - use a basic template
                final_prompt = f"Please respond just funnily negatively to this question: {prompt}"
                # st.info("No matching prompt - using default template for the prompt")

            # Send prompt
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": final_prompt,
                        }
                    ],
                    model="llama3-8b-8192",
                )
                
                # Display AI response in chat message container
                with st.chat_message("assistant"):
                    st.write(chat_completion.choices[0].message.content)
                    st.session_state.messages.append({"role": "assistant", "content": chat_completion.choices[0].message.content})
            except Exception as e:
                st.info(f"Couldn't send the message to Groq: {str(e)}")

            return True
        except Exception as e:
            st.error(f"Error during automation: {str(e)}")
            return False

    with st.spinner("Generating response..."):
        success = open_website()