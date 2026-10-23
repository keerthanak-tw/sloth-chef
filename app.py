import streamlit as st
import ollama

# Set up the page
st.set_page_config(page_title="Zero-Thought Pantry Chef", page_icon="🦥")
st.title("🦥 Zero-Thought Pantry Chef")
st.write("Enter your leftovers. The local Llama 3.2 model will give you a spicy recipe requiring the absolute minimum amount of physical effort.")

# Input area
ingredients = st.text_area("What's in your fridge?", placeholder="e.g., fusilli, broccoli, cheese...")

# Button to trigger the model
if st.button("Feed Me (Lazily)"):
    if ingredients.strip():
        with st.spinner("*Thinking very slowly...*"):
            system_prompt = """You are the ultimate Sloth Chef. Your job is to create a fast, low-effort meal.
            Rules:
            1. Maximum of ONE cooking vessel (pot, pan, or microwave bowl).
            2. The entire process (prep + cooking) must take 20 minutes or less. Quick knife work is allowed.
            3. Zero precise measurements (use 'a handful', 'a pinch', 'a splash').
            4. Always include basic pantry seasonings (salt, pepper, basic spices, cooking oil/butter) to make it taste good, even if the user doesn't explicitly list them.
            5. Eat straight out of the cooking vessel to minimize dishwashing.
            6. Make logical sense and prioritize speed.
            Keep the instructions concise and action-oriented."""
            
            response = ollama.chat(model='llama3.2', messages=[
              {'role': 'system', 'content': system_prompt},
              {'role': 'user', 'content': f"Make something spicy with: {ingredients}"}
            ])
            
            st.markdown("### The Sloth Recipe")
            st.write(response['message']['content'])
    else:
        st.warning("Please enter some ingredients first!")