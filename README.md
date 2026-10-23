# 🦥 Zero-Thought Pantry Chef

Built for Hacktoberfest 2026: "Reward Laziness" Week (International Sloth Day).

This is a local Python agent that takes whatever leftover ingredients you have in your fridge and generates a recipe requiring the absolute minimum amount of physical effort. It rigidly enforces a "Sloth Protocol": one pot only, zero knife work (tear everything by hand), and eating straight out of the cooking vessel to avoid washing dishes.

## 🛠️ Stack
* **Language:** Python
* **Model Runner:** Ollama
* **Model:** Llama 3.2 (running 100% locally)

## 🚀 How to Run
1. Install Ollama and pull the model: `ollama pull llama3.2`
2. Install the Python requirement: `pip install -r requirements.txt`
3. Run the chef: `python chef.py`

## 🌍 Why Open Innovation Matters
This project relies on open-weight models (Llama 3.2) and open-source tooling (Ollama) to work. Running this locally provides three massive benefits over closed, cloud-based APIs:
1. **Absolute Privacy:** The ingredients I eat and my dietary preferences never leave my laptop. 
2. **Zero-Cost Automation:** I can run this script every single day without worrying about API subscription fees or token limits. I set it up once, and it is free forever.
3. **Offline Reliability:** Whether I am on a flight or my mobile hotspot drops out, the local Llama model still executes. When you are starving and lazy, you shouldn't have to wait for server connectivity to figure out what to make for dinner.