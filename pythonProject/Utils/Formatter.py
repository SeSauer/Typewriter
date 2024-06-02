from typing import Protocol

import Utils.Utils
from Utils.Utils import add_newlines_to_string
from openai import OpenAI


class BaseFormatter(Protocol):
    def format(self, string: str) -> str:
        raise NotImplementedError("Cant invoke Interface")


class DefaultFormatter(BaseFormatter):
    def format(self, string: str) -> str:
        string = add_newlines_to_string(string)
        if string == "" or string[-1] != "\n":
            string = string + "\n"
        return string


class NullFormatter(BaseFormatter):
    def format(self, string: str) -> str:
        return string


class OpenAiFormatter(DefaultFormatter):
    def __init__(self):
        self.openai = OpenAI(api_key=open("key.txt").read())
        Utils.Utils.log("Connected to OpenAI", color=Utils.Utils.Colors.OKCYAN)
        self.messages = []
        self.messages.append({"role": "system", "content": "You are a Chatbot who lives in a Typewriter'"})

    def format(self, string: str) -> str:
        self.messages.append({"role": "user", "content": string})
        Utils.Utils.log("Querying OpenAI...", 1)
        output = self.openai.chat.completions.create(messages=self.messages, model="gpt-3.5-turbo")
        outstring = output.choices[0].message.content
        Utils.Utils.log(f"Response from OpenAI: {outstring}", 0)
        outstring = super().format(outstring)
        return outstring
