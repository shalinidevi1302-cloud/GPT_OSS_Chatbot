@@ -0,0 +1,60 @@
import streamlit as st
from transformers import pipeline

# Page configuration
st.set_page_config(
    page_title="HP AI Text Generator",
    page_icon="🤖",
    layout="centered"
)

# App title
st.title("🤖 HP AI Text Generator")
st.write("✨ Enter a prompt and let AI generate text for you!")

# Load AI model
@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="EleutherAI/gpt-neo-125M"
    )

generator = load_model()

# User input
prompt = st.text_area(
    "✍️ Enter your prompt:",
    placeholder="Artificial Intelligence is..."
)

# Generate button
if st.button("✨ Generate Text"):

    if prompt.strip():

        with st.spinner("🤖 Generating your text..."):

            result = generator(
                prompt,
                max_new_tokens=80,
                num_return_sequences=1,
                do_sample=True,
                temperature=0.7,
                top_p=0.9
            )

        generated_text = result[0]["generated_text"]

        # Remove the original prompt
        new_text = generated_text[len(prompt):].strip()

        st.subheader("📝 Generated Text")

        if new_text:
            st.write(new_text)
        else:
            st.warning("No additional text was generated.")

    else:
        st.warning("⚠️ Please enter a prompt first!")