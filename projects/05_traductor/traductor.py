"""
    para poder realizar esta practica debes instalar la libreria 'deep_translator'
    'pip install deep_translator'
"""

from deep_translator import GoogleTranslator;

# traducir texto
traductor = GoogleTranslator(source='es', target='en');
texto = traductor.translate('Hola, soy Ronaldo Jimenez trabajo como desarrolador web.');
print(texto);

# leer un archivo de texto.
traductor = GoogleTranslator(source='en', target='es');
texto = traductor.translate_file(r'C:\TMP\perfil.txt');
print(texto);

# lista de elementos
lista = ['Easy', 'Programación', 'Python', 'Saludar'];
traductor = GoogleTranslator(source='auto', target='uk');
texto = traductor.translate_batch(lista);
print(texto);