# ECR Amazon Elastic Container Registry
Es una buena opción, aunque se aleja de la automatización con workflows de GitHub a lo que se añade que tiene una alta dificultad de usar con el cliente Docker, debido a que es necesario la creación de un token temporal, hay un gasto adicional de ocste si los contenedores no se implementan en AWS y hay poca información para el uso del registro.

# JFrog
Es un administrador de repositorios que admite registros de Docker seguros, agrupados y de alta disponibilidad. Sin embargo, aunque es bastante fácil de utilizar la versión local debe ser siempre administrada y actualizada por el usuario final y suele ser más costoso que otras posibilidades.

# GCR
AParte de que el registro de contenedores es gratuito, está enlazado con Github y presenta unas características, aparte de la actualización automática con workflows, como una lista de permisos muy detallada, el acceso seguro a contenedores a tarvés de GITHUB_TOKEN, acceso anónimo a los contenedores públicos publicados y publicados de manera limpia en ghcr.io