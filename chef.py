import ollama

# A simple test message
response = ollama.chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Say hello like a tired sloth.',
  },
])

print(response['message']['content'])