import requests
from config import Config


class AIServiceError(Exception):
    pass


class AIService:
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.business_context = Config.BUSINESS_CONTEXT

    def sistem_mesaji(self):
        return self.business_context

    def yanit_uret(self, mesaj, gecmis=None):
        if not self.api_key:
            return "Demo modu aktif. Yapay zeka servisi için API anahtarı bulunamadı."

        if gecmis is None:
            gecmis = []

        messages = [
            {
                "role": "system",
                "content": self.sistem_mesaji()
            }
        ]

        messages.extend(gecmis)

        messages.append(
            {
                "role": "user",
                "content": mesaj
            }
        )

        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "openai/gpt-oss-20b",
                    "messages": messages
                },
                timeout=30
            )

            response.raise_for_status()

            data = response.json()

            return data["choices"][0]["message"]["content"]

        except requests.RequestException as error:
            raise AIServiceError(
                "Yapay zeka servisine bağlanırken bir hata oluştu."
            ) from error


ai_service = AIService()