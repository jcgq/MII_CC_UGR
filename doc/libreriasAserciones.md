# Librerías de Aserciones
## Grappe

Es una librería ligera orientada al comportamiento, autodeclarativam expresiva y amigable. Tiende a acercarse al idioma natural, por lo que lo aleja del leguaje de Python, y puede tener una alta rampa de aprendizaje.
Un ejemplo:
```python
  from grappa import should

  True | should.be.true
  False | should.be.false
  None | should.be.none

  '' | should.be.empty
  [] | should.be.empty
  'foo' | should.exists
```
## Verify
Es una librería similar a Unitest, pero que no ofrece tantas funcionalidades como UnitTest. Tiene un estilo bastante similar:
```python
def is_just_right(value):
    assert value == 'just right', 'Not just right!'
```
Sin embargo, está dejando de tener ciertas actualizaciones que hacen que pierda importancia al poder decirdir su uso.
