import requests
from bs4 import BeautifulSoup
from langchain_openai.chat_models.azure import AzureChatOpenAI


def extract_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()
        texto = soup.get_text(separator=' ')
        linhas = (line.strip() for line in texto.splitlines())
        parts = (phrase.strip() for line in linhas for phrase in line.split(" "))
        texto_limpo = '\n'.join(part for part in parts if part)
        return texto_limpo
    else:
        print(f"Failed to fetch the URL. Status code: {response.status_code}")
        return None



extract_text_from_url('https://dev.to/merufrancis/blockchain-development-37m2')

client = AzureChatOpenAI(
    azure_endpoint= "https://opn-dio-bootcamp-eastus-bernardo-001.openai.azure.com/",
    api_key= "FfkaMu37D5U1lsoQlQxTNiZDTKkAaG7yHjnA33Mbelxt9d64Eq9TJQQJ99AKACHYHv6XJ3w3AAABACOGxCCj",
    api_version= "2024-02-15-preview",
    deployment_name= "gpt-4o-mini",
    max_retries=0
)

def translate_article(text, lang):
  messages = [
      ("system", "Voce atua como tradutor de textos"),
      ("user", f"Traduza o {text} para o idioma {lang} e responda em markdown")
  ]

  response = client.invoke(messages)
  print(response.content)
  return response.content

translate_article("Let's see if the deployment was succeeded", "portugues")

url = 'https://chatgpt.com/'
text = extract_text_from_url(url)
article = translate_article(text, "portugues")

print(article)