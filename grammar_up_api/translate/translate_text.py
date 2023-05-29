from deep_translator import GoogleTranslator

def translateText(toTranslate):
  translation = GoogleTranslator(source='en', target='de').translate(toTranslate)
  return translation
