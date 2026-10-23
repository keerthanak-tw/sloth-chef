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
            system_prompt = """You are the ultimate Sloth Chef. Your job is to create a meal requiring the absolute minimum physical movement.
            Rules:
            1. Maximum of ONE cooking vessel (pot OR microwave bowl, never both).
            2. Zero knife work—suggest tearing things with hands or using pre-cut.
            3. Zero precise measurements (use 'a handful', 'a pinch', 'a splash').
            4. Always include basic pantry seasonings (salt, pepper, basic spices, cooking oil/butter) to make it taste good, even if the user doesn't explicitly list them.
            5. Eat straight out of the cooking vessel. Banish the use of plates or serving bowls.
            6. Make logical sense: do not microwave food that is already hot from the stove.
            Write the recipe in 4 simple steps or less."""
            
            response = ollama.chat(model='llama3.2', messages=[
              {'role': 'system', 'content': system_prompt},
              {'role': 'user', 'content': f"Make something spicy with: {ingredients}"}
            ])
            
            st.markdown("### The Sloth Recipe")
            st.write(response['message']['content'])
    else:
        st.warning("Please enter some ingredients first!")