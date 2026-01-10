from agent import Agent
import json
import ollama
import google.genai as genai
import os


class Orchestrator(Agent):
    def __init__(self, model, client, api_key):
        self.client = client
        if client == 'ollama':
            self.model = model  
        if client == 'google':
            self.google_client = genai.Client(api_key=api_key or os.environ.get("GOOGLE_API_KEY"))
            self.model = model

    def answer(self, prompt, articles):
        model = self.model
        system_instruction = (
            f"Answer following user prompt using these articles as sources, answer only basing on the sources if you don't know say it instead of creating facts, that aren't said in these articles. Do not ask user question, your answer is final. Articles content: {articles}"
        )
        
        prompt = f"{system_instruction}\nPrompt: {prompt}"
        
        if self.client =='ollama':
            response = ollama.generate(
                model=model,
                prompt=prompt,
                stream=False
            )
            text = response['response'].strip()
            return text
        if self.client == 'google':
            response = self.google_client.models.generate_content(
                model=self.model,
                contents=prompt,
            )
            return response.text.strip()

    def analyze_prompt(self, prompt):
        model = self.model
        system_instruction = (
            "Analyze following user prompt and return ONLY the analysis in JSON in format: "
            "{'action': 'analyze_stock', 'company': <nazwa firmy lub None>, 'period': <okres lub None>, 'question': <oryginalny prompt>} " \
            ""
        )
        
        prompt=f"{system_instruction}\nPrompt: {prompt}"

        if self.client == 'google':
            response = self.google_client.models.generate_content(
                model=self.model,
                contents=prompt,
            )
            return response.text.strip()

        if self.client == 'ollama':
            response = ollama.generate(
                model=model,
                prompt=prompt,
                stream=False
            )
            text = response['response'].strip()
            return text

    def execute(self, prompt, articles):
        answer = self.answer(prompt, articles)
        
        
        
        
        print(answer)


        # Answer the question basing on articles and stock charts
        # Write report
