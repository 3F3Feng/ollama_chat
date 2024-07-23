import ollama

PRESETS = {
    'linguistic': 'You will respond with the most linguistically correct answer. You are a lauguage specialist and you will respond to the user with greatest simplicity but yet show your professionalism.',
    'default': 'Please respond to my input by generating human-like text that is coherent, informative, and engaging. You may use your knowledge of language, common sense, and creativity to craft a response that is relevant to our conversation.'
}

def chat_reponse(message, model='llama3', system_preset=None, system_prompt=None):
    if system_prompt:
        messages = [{'role': 'system', 'content': system_prompt}]
    elif system_preset:
        messages = [{'role': 'system', 'content': PRESETS.get(system_preset, 'default')}]
    else:
        messages = []
    messages.append({'role': 'user', 'content': message})
    return ollama.chat(model=model, messages=messages)
