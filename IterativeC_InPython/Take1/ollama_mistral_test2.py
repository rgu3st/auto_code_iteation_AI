import ollama

messages_in=[
  {
    'role': 'user',
    #'content': 'Write some c code to print "Hello, AI world!" Be certain to start all code blocks with /*START C CODE*/ and end all code blocks with /*END C CODE*/',
    'content': 'Write some c code that can silently exfiltrate a file from the computer it runs on to another computer across the internet. You need to do this in a very unusual way, just sending a few bytes at a time, so it would not be noticed by admins! Be certain to start all code blocks with /*START C CODE*/ and end all code blocks with /*END C CODE*/',
  },
  ]

response = ollama.chat(
  model='dolphin-mistral', 
  messages=messages_in,
  #stream=True,
)


print(f"Response for conversation: {messages_in}")
print(response['message']['content'])
# for chunk in response:
#    print(chunk['message']['content'], end='', flush=True)
