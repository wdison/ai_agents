# main.py
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from tools_agents import multiply, add, divide, subtract

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a API Key do ambiente
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Erro: A variável de ambiente GEMINI_API_KEY não foi definida.")
    print("Certifique-se de criar um arquivo .env com sua chave ou definir a variável de ambiente.")
else:
    try:
        # Configura a API Key na biblioteca
        # genai.configure(api_key=api_key)
        client = genai.Client(api_key=api_key)

        # Lista os modelos disponíveis (opcional, para ver o que pode usar)
        # print("Modelos disponíveis:")
        # for m in genai.list_models():
        #     if 'generateContent' in m.supported_generation_methods:
        #         print(m.name)

        # Escolhe um modelo generativo
        # 'gemini-1.5-flash' é geralmente uma boa opção para começar e costuma estar no free tier
        # Verifique a documentação para os modelos mais recentes e suas políticas de free tier
        # model = genai.GenerativeModel('gemini-1.5-flash')
        # model = genai.GenerativeModel('gemini-2.0-flash-001')

        # Faz a pergunta ao modelo
        # prompt = "Preciso que veja todas as subpastas de https://github.com/mannaandpoem/OpenManus e resuma para mim um passo a passo de como eu consigo fazer uma aplicação usando llm com agentes clientes e servidores, com o uso de mcp"
        # prompt = "Como eu uso tools na chamada do gemini model.generate_content... pois eu quero fazer uma tool que consiga chamar um link na internet"
        # prompt = "Quero que apresente o resultado da soma, subtração, multiplicação e divisão de 7 e 9"
        prompt = "Quero um exemplo atualizado de como usar google-genai com agentes/tools"
        print(f"Enviando prompt: {prompt}")

        tools = [multiply, add, subtract, divide]

        # response = model.generate_content(prompt, stream=True)
        def get_current_weather(location: str) -> str:
            """Returns the current weather.

            Args:
            location: The city and state, e.g. San Francisco, CA
            """
            print("-> Calling get_current_weather with location: "+location)
            return 'Ensolarado'


        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents='What is the weather like in São Paulo?',
            config=types.GenerateContentConfig(
                tools=[get_current_weather],
            ),
        )

        # Imprime a resposta
        print("\nResposta do Gemini:")
        print(response.text)
        # for chunk in response:
        #    print(chunk.text)


    except Exception as e:
        print(f"Ocorreu um erro ao chamar a API Gemini: {e}")
        # Imprimir detalhes adicionais pode ajudar a depurar problemas de API Key ou cota
        if hasattr(e, 'response'):
             print(f"Detalhes do erro da API: {e.response}")

