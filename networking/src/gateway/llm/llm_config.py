# src/networking/gateway/llm/llm_config.py
# LLM Model Paths
CURRENT_MODELS = {
    'athena_q4': "app/models/athena-v4.Q4_K_M.gguf",
    'athena_q5': "app/models/athena-v4.Q5_K_S.gguf",
    'bloke_llama_2_q4': "app/models/llama2_7b_chat_uncensored.Q4_K_M.gguf",
    'bloke_llama_2_q8': "app/models/llama2_7b_chat_uncensored.Q8_0.gguf",
    'llama_2_q4': "app/models/llama-2-7b-chat.Q4_K_M.gguf",
    'llama_2_q5': "app/models/llama-2-7b-chat.Q5_K_S.gguf",
}

# LLM Settings
conversational_llm = 'athena_q4'
action_llm = 'llama_2_q4'
