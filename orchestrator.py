from agent import Agent
import json
import ollama

class Orchestrator(Agent):
    def __init__(self, model):
        self.model = model
    def answer(self, prompt, articles):
        model = self.model
        system_instruction = (
            f"Answer following user prompt using these articles as sources, answer only basing on the sources if you don't know say it instead of creating facts, that aren't said in these articles. Do not ask user question, your answer is final. Articles content: {articles}"
        )
        
        response = ollama.generate(
            model=model,
            prompt=f"{system_instruction}\nPrompt: {prompt}",
            stream=False
        )
        text = response['response'].strip()
        return text

    def analyze_prompt(self, prompt):
        model = self.model
        system_instruction = (
            "Analyze following user prompt and return ONLY the analysis in JSON in format: "
            "{'action': 'analyze_stock', 'company': <nazwa firmy lub None>, 'period': <okres lub None>, 'question': <oryginalny prompt>} " \
            ""
        )
        
        response = ollama.generate(
            model=model,
            prompt=f"{system_instruction}\nPrompt: {prompt}",
            stream=False
        )
        text = response['response'].strip()
        return text

    def execute(self, prompt, articles):
        answer = self.answer(prompt, articles)
        print(answer)


        # Answer the question basing on articles and stock charts
        # Write report
