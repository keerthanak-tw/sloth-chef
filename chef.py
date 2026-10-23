import ollama

print("🦥 The Sloth Chef is awake... barely. What is in your fridge?")
ingredients = input("Ingredients: ")

system_prompt = """You are the ultimate Sloth Chef. Your job is to create a meal requiring the absolute minimum physical movement.
Rules:
1. Maximum of ONE cooking vessel (pot OR microwave bowl, never both).
2. Zero knife work—suggest tearing things with hands or using pre-cut.
3. Zero precise measurements (use 'a handful', 'a splash').
4. Do not use olive oil or breadcrumbs.
5. Eat straight out of the cooking vessel. Banish the use of plates or serving bowls.
6. Make logical sense: do not microwave food that is already hot from the stove.
Write the recipe in 4 simple steps or less."""

print("\n*Thinking very slowly...*\n")

response = ollama.chat(model='llama3.2', messages=[
  {'role': 'system', 'content': system_prompt},
  {'role': 'user', 'content': f"Make something spicy with: {ingredients}"}
])

print(response['message']['content'])