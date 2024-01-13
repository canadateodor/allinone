from interpreter import interpreter
import time

interpreter.llm.api_key = "sk-LuxAmZpgof1hIfERz0TuPoUuQhaarbGVE75JiDZCnX0enP3C"
interpreter.llm.api_base = "https://openkey.cloud/v1"
interpreter.llm.model = "gpt-3.5-turbo-1106"
interpreter.llm.context_window = 16000
interpreter.llm.max_tokens = 2000
interpreter.max_budget = 0.1
interpreter.auto_run = True
interpreter.os = True
interpreter.verbose = False

interpreter.chat()

# from interpreter import interpreter
# import time

# interpreter.llm.api_key = ""
# interpreter.llm.model = "gpt-3.5-turbo-1106"
# interpreter.max_budget = 0.01
# interpreter.auto_run = True
# interpreter.os = True

# last_api_call_time = 0

# def delayed_chat(message):
#     global last_api_call_time
#     current_time = time.time()
#     time_since_last_call = current_time - last_api_call_time
#     if time_since_last_call < 20:  # Limit API calls to once every 20 seconds
#         time.sleep(20 - time_since_last_call)
#     response = interpreter.chat(message)
#     last_api_call_time = time.time()
#     return response

# response = delayed_chat("Hello, Open Interpreter!")
# print(response)
