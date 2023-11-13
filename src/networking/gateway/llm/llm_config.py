# src/networking/gateway/llm/llm_config.py
# LLM Model Paths
MODEL_PATHS = {
    'athena_q4': "src/networking/gateway/llm/models/athena-v4.Q4_K_M.gguf",
    'athena_q5': "src/networking/gateway/llm/models/athena-v4.Q5_K_S.gguf",
    'bloke_llama_2_q4': "src/networking/gateway/llm/models/llama2_7b_chat_uncensored.Q4_K_M.gguf",
    'bloke_llama_2_q8': "src/networking/gateway/llm/models/llama2_7b_chat_uncensored.Q8_0.gguf",
    'llama_2_q4': "src/networking/gateway/llm/models/llama-2-7b-chat.Q4_K_M.gguf",
    'llama_2_q5': "src/networking/gateway/llm/models/llama-2-7b-chat.Q5_K_S.gguf",
}

# LLM Settings
conversational_llm = 'athena_q4'
action_llm = 'llama_2_q4'
