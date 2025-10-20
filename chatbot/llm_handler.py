

import requests
import json
from typing import List, Dict, Optional

class LLMHandler:
    """
    Wrapper for Groq chat API (Groq chat models)
    """

    def __init__(self, config):
        self.api_key = config.GROQ_API_KEY
        self.model = config.GROQ_MODEL
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def generate(
        self,
        messages: List[Dict],
        max_tokens: int = 512,
        temperature: float = 0.0,
        stop: Optional[List[str]] = None
    ) -> tuple[str, Dict]:
        """
        Sends messages to Groq LLM and returns the answer text and raw response.
        """
        body = {
            "model": self.model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature
        }

        if stop:
            body["stop"] = stop

        try:
            resp = requests.post(
                self.base_url,
                headers=self.headers,
                data=json.dumps(body),
                timeout=60
            )
        except requests.exceptions.RequestException as e:
            return f"Request Error: {str(e)}", {}

        if resp.status_code != 200:
            # Return error and raw response
            return f"Groq API error ({resp.status_code}): {resp.text}", resp.json() if resp.text else {}

        try:
            data = resp.json()
        except json.JSONDecodeError:
            return f"Error decoding API response: {resp.text}", {}

        # Extract text from choices
        try:
            content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        except Exception:
            content = ""

        return content, data
