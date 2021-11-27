from setuptools import setup


setup(
    name='requerimientos',
    description='Instalación de módulos necesarios',
    license="MIT",
    author='Juan Carlos González Quesada',
    install_requires=['numpy', 'pybind11', 'Cython', 'pyTest', 'googletrans', 'invoke', 'scipy', 'nltk', 'sklearn']
)