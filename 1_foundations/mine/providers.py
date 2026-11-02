ANTHROPIC_API_URL = "https://api.anthropic.com/v1"
ANTHROPIC_API_MODEL = "claude-haiku-4-5-20251001"
GOOGLE_AI_API_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GOOGLE_AI_API_MODEL = "gemini-3.7-flash"
GOOGLE_AI_API_MODELS = {
    "gemini-3.6": "gemini-3.6-flash",
    "gemma-4": "gemma-4-31b-it",
}
OPENROUTER_API_URL = "https://openrouter.ai/api/v1"
# OPENROUTER_API_MODEL = "google/gemma-4-26b-a4b-it:free"
# OPENROUTER_API_MODEL = "google/gemma-4-31b-it:free"
OPENROUTER_API_MODEL = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"
OPENROUTER_API_MODELS = {
    "poolside": "poolside/laguna-s-2.1:free",
    "nvidia": "nvidia/nemotron-3-ultra-550b-a55b:free",
    "cohere": "cohere/north-mini-code:free",
}
