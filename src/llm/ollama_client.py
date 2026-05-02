from langchain_community.llms import Ollama
import os

class OllamaClient:
    def __init__(self, model=None, base_url=None):
        # Utiliser l'URL locale d'Ollama
        self.base_url = base_url or os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.model = model or os.getenv("OLLAMA_MODEL", "llama2")
        self.llm = Ollama(model=self.model, base_url=self.base_url)

    def generate(self, prompt: str, user_id: str = None) -> str:
        """Génère une réponse à partir d'un prompt."""
        try:
            response = self.llm.invoke(prompt)
            return response
        except Exception as e:
            raise

    def generate_with_template(self, template: str, **kwargs) -> str:
        """Génère une réponse à partir d'un template de prompt."""
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_core.output_parsers import StrOutputParser

        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | self.llm | StrOutputParser()
        return chain.invoke(kwargs)