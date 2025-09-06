from textblob import TextBlob
from googletrans import Translator

translator = Translator()

def traduzir_para_ingles(texto):
    traducao = translator.translate(texto, src='pt', dest='en')
    return traducao.text

def calcular_star_rating(feedback):
    feedback_em_ingles = traduzir_para_ingles(feedback)

    pontuacoes = TextBlob(feedback_em_ingles).sentiment
    polarity = pontuacoes.polarity
    subjectivity = pontuacoes.subjectivity
    
    if polarity > 0.1 and subjectivity >= 0.4:
        return "Produtivo"
    else:
        return "Improdutivo"