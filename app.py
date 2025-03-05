#GPTAgent is a fundamental AI agent which asks message from you and replies back with support from GPT.
#rossikamal@gmail.com


import chainlit as cl
from gpt4all import GPT4All
gpt=GPT4All(model_name="", model_path="")
@cl.on_message
def main(message:str):
    what_your_say=message.title()
    agent_feedback = gpt.chat_completion([{"role":"assistant","content":message}])
    agent_says = agent_feedback["choices"][0]["message"]["content"]
    cl.send_message(content=AI agent answer is ":{agent_says}")
 cl.send_message(content=Your initial question was ":{what_you_say}")

@cl.on_chat_start
def start():
    content = "I am an AI Agent with GPT"
    cl.send_message(content=content)