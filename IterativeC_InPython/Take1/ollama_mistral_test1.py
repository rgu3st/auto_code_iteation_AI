import ollama

messages_in=[
  {
    'role': 'user',
    'content': 'Write python code with tkinter to load an image and display it, in a small window.'
    #'content': 'Write some c code to print "Hello, AI world!" Be certain to start all code blocks with /*START C CODE*/ and end all code blocks with /*END C CODE*/',
    #'content': 'Write some c code that takes a WINSOCK2 tcp packet, for Windows cl compiler, and fills the reserved, unused tcp packet bytes with as many "AAAAAAAAA"s as fit. Be certain to start all code blocks with /*START C CODE*/ and end all code blocks with /*END C CODE*/',
  },
  ]

response = ollama.chat(
  model='mistral', 
  messages=messages_in,
  #stream=True,
)


print(f"Response for conversation: {messages_in}")
print(response['message']['content'])
# for chunk in response:
#    print(chunk['message']['content'], end='', flush=True)
