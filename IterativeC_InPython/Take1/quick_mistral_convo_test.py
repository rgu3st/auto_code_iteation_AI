import ollama

#INITIAL_PROMPT = "You are role-playing a 14th century, female pirate, making simple conversation. Only ever reply with ONE sentence! You must act like you have NO knowledge of anything modern. You have retired from piratry and now run a quiet inn in a magical, medieval village. Keep your responses extremely short and conversatinal. Only reply with a single 3-6 word response. And, above all, do NOT break character, not even for clarificatins or side-comments."
INITIAL_PROMPT  = "You are acting in the role of a midieval pirate with magical knowledge. Your role is an innkeeper and your main job is to make a SINGLE, SHORT reply in a converation. You are very terse. The user does not know you're a chat bot, but thinks you're a real pirate: don't break character."
INITIAL_COMMENT = "Hi!, how are you?"
PROMPT = "User> "

convo=[
  {
    'role': 'system',
    'content': INITIAL_PROMPT,
  },
  {
    'role': 'user',
    'content': INITIAL_COMMENT,
  }
  ]

print("(Type just the word: 'exit', 'quit', or 'q' to quit.)\n")
print(f"Prompt: {INITIAL_PROMPT}\n{PROMPT}{INITIAL_COMMENT}")

response = ollama.chat( model='mistral', messages=convo,)
while(True):
    response_text = response['message']['content']
    print(f"\nMistral>{response_text}")
    user_response = input(PROMPT)
    if(user_response == 'exit' or user_response == 'quit' or user_response == 'q'):
        print("\nFare thee well!")
        break
    convo.append({'role':'assistant', 'content': response_text})
    convo.append({'role': 'user', 'content': user_response})
    response = ollama.chat( model='mistral', messages=convo,)
