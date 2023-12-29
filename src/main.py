from extract_html import web_page_extractor
from llm import togetherai_inference
import argparse
import os
import dotenv
import together

dotenv.load_dotenv()
together.api_key = os.getenv("together_key")
debug = os.getenv("debug")

# Configurar el parser de argumentos
parser = argparse.ArgumentParser(
    description="""En un futuro estos argumentos se
                                 rescataran de la url del tweet con el
                                 clickbait, pero por el momento los pasamos
                                 manualmente"""
)
parser.add_argument("--url", dest="url", type=str, help="La URL a consultar por el LLM")
parser.add_argument(
    "--header", dest="header", help="La cabecera del tweet con el clickbait"
)

# select a model from: https://api.together.xyz/playground
parser.add_argument(
    "--model",
    dest="model",
    help="Modelo a utilizar",
    default="mistralai/Mistral-7B-Instruct-v0.2",
)

parser.add_argument(
    "--max_tokens",
    dest="max_tokens",
    help="Número máximo de tokens para el modelo",
    default=1024,
)

parser.add_argument(
    "--temperature", dest="temperature", help="Temperatura", default=0.7
)

parser.add_argument("--top_p", dest="top_p", help="Top_p", default=0.7)
parser.add_argument("--top_k", dest="top_k", help="Top_k", default=50)
parser.add_argument("--repetition_penalty", dest="repetition_penalty", default=2)

args = parser.parse_args()

kwargs = {
    "model": args.model,
    "max_tokens": args.max_tokens,
    "temperature": args.temperature,
    "top_p": args.top_p,
    "top_k": args.top_k,
    "repetition_penalty": args.repetition_penalty,
}

header = args.header
url = args.url

if debug == "True":
    header = "El chiste de Matías Prats sobre los 'probadores' de helados: 'Parece que está...'"
    url = "https://www.antena3.com/noticias/cultura/chiste-matias-prats-probadores-helados-parece-que-esta_2023122465885512d7b0c30001a6bc07.html?so=so&sour=twitter&cn=a3noticias"

# primero parseamos el html
web_text = web_page_extractor(url=url)

# diseñamos el prompt
prompt = (
    "El titular de la siguiente noticia es un 'clickbait'. Redacta un nuevo titular"
    "completo y sin 'clickbaits' a partir del contenido de la web de la noticia."
    f'\n Titular:"""{header}"""\n\n'
    f'Noticia:"""{web_text}"""\n\n'
    f"Nuevo titular:"
)

# enviamos el prompt al modelo
response = togetherai_inference(prompt=prompt, **kwargs)

# printeamos el resultado
print(response)
