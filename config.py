import os

# API 密钥  (请替换成你的实际密钥)
CEREBRAS_API_KEY = os.environ.get("CEREBRAS_API_KEY")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# 默认文件夹路径
DEFAULT_FOLDER_PATH = r"C:\Users\Lingyun Chen\OneDrive\文档\TMSpeechLogs"

# 可用模型列表
AVAILABLE_MODELS = [
    "[Cerebras] llama3.1-70b",
    "[Cerebras] llama3.1-8b",
    "[Groq] mixtral-8x7b-32768",
    "[Groq] llama-3.1-70b-versatile",
    "[Groq] llama-3.1-8b-instant",
    "[Groq] llama-3.2-90b-vision-preview",
    "[Gemini] gemini-1.5-flash",
    "[Gemini] gemini-1.5-flash-002",
    "[Gemini] gemini-1.5-flash-8b"
]

# 默认模型
DEFAULT_MODEL = AVAILABLE_MODELS[0]

# 默认温度
DEFAULT_TEMPERATURE = "1.0"