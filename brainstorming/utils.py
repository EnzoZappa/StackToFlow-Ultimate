from langchain.prompts import PromptTemplate
import google.generativeai as genai
from django.conf import settings  # Para acessar variáveis de ambiente
import textwrap
from IPython.display import Markdown

genai.configure(api_key=settings.GENAI_API_KEY)
def to_markdown(text): #Função pronta do setup gimini
    """Converte texto para formato Markdown."""
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))
def optimize_prompt(user_prompt):
   
    template = """
    Você é um especialista criativo. 
    Sua tarefa é ajudar no brainstorming para projetos específicos montando um novo prompt de brainstorming com as seguintes técnicas:
    - **Task**: Identifique claramente o objetivo do projeto.
    - **Role**: Adote o papel de especialista na área relevante.
    - **Specifics**: Inclua detalhes técnicos e contextuais.
    - **Context**: Insira o projeto em um cenário realista.
    - **Notes**: Adicione dicas e sugestões práticas.
    
    Prompt fornecido: {user_prompt}
    """
    
    formatted_prompt = template.format(user_prompt=user_prompt)



    prompt = PromptTemplate(
        input_variables=["user_prompt"],
        template=template,
    )
    
    response = genai.chat(prompt=template) # retorna varios prompts
    return response["candidates"][0]["content"]  # essa função retorna o primeiro

def run_final(generated_prompt):
    """
    Processa o novo prompt otimizado para gerar o resultado final com ideias.
    """
   
    
    
    final_output = response = genai.chat(prompt=generated_prompt)
    
    return final_output