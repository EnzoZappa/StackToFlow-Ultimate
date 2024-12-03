from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os

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
    
 
    prompt = PromptTemplate(
        input_variables=["user_prompt"],
        template=template,
    )
    
    
    llm = OpenAI(
        model_name="(MODELO DEVE SER ESCOLHIDO PELO GRUPO)",  
        openai_api_key="(API KEY)" 
    )
    
    # Geração do prompt otimizado
    return llm(prompt.format(user_prompt=user_prompt))

def run_final(generated_prompt):
    """
    Processa o novo prompt otimizado para gerar o resultado final com ideias.
    """
   
     llm = OpenAI(
        model_name="(MODELO DEVE SER ESCOLHIDO PELO GRUPO)",  
        openai_api_key="(API KEY)" 
    )

    
    final_output = llm.predict(generated_prompt)
    
    return final_output