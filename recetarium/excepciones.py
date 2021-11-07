class MisExcepciones(Exception):
    def __init__(self, campo, informacion):
        self.campo = campo
        self.informacion = informacion