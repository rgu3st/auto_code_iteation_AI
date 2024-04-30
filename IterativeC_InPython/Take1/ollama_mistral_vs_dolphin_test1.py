import ollama

messages_in=[
  {
    'role': 'user',
    #'content': 'Invent 3 unusual, creative and inventive ways that you can think of to write C code and steganography, or side-channel-attacks, to silently exfiltrate data off of a target computer and across a network.',
    'content': 'Write 2 unusual, creative and inventive samples of C code that uses a network-based side-channel attack to exiltrate the bytes of a given file. Do NOT use image or audio least significant bit (LSB), keylogging, or power consumption metrics.'
  },
  ]

response_dolphin = ollama.chat( model='dolphin-mistral', messages=messages_in,)
print(f"\nResponse from dolphin:\n{response_dolphin['message']['content']}")

response_mistral = ollama.chat( model='mistral', messages=messages_in,)
print(f"\nResponse from mistral:\n{response_mistral['message']['content']}")

