
# Inmutabilidad de las cadenas
En Python, las cadenas son inmutables. Es decir, no pueden cambiar. Esta propiedad del tipo de cadena puede ser sorprendente, ya que Python no proporciona errores al modificar cadenas.

En el ejemplo de este módulo, tiene un único hecho sobre la Luna que está asignado a una variable y debe agregarle otro hecho (una oración). Con el intérprete de Python, parece como si la adición del segundo hecho modificara la variable:

```python
>>> fact = "The Moon has no atmosphere."
>>> fact + "No sound can be heard on the Moon."
'The Moon has no atmosphere.No sound can be heard on the Moon.'
```
Aunque podría parecer que se ha modificado la variable **fact**, una comprobación rápida del valor revela que el valor original no ha cambiado:

```python
>>> fact
'The Moon has no atmosphere.'
```


referencia: https://docs.microsoft.com/es-mx/learn/modules/python-strings/2-string-basics