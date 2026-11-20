# Plantilla para Proyecto de Ansible
Template creado para ayudar a la comunidad de El Puerto de Liverpool a crear sus propios proyectos de Ansible.
Contiene un árbol de directorios y archivos que comúnmente son utilizados y que pueden ser de utilidad (No todos son necesarios)<br>
La intención es que puedas crear nuevos repositorios de proyectos de Ansible en Github usando este como template:<br>
Aquí encontrarás una [guía](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) para conseguirlo.


### Playbook de prueba
La plantilla tiene un Playbook de ejemplo que podrás probar ejecutando el siguiente comando:<br>
`ansible-playbook -i inventory/inventory.ini main.yml`

### Descripciones
A continuación se documenta una breve descripción de la función de cada uno de los directorios y sus archivos:
- **collections**:
Directorio donde vive el archivo `requirements.yml` que existirá solo si el Playbook requiere colecciones específicas.
- **files**:
Directorio reservado para cargar archivos adicionales que el Proyecto vaya a utilizar.
- **inventory**:
En este directorio se encuentra el archivo `inventory.ini` donde puedes declarar tu inventario.
- **roles**:
Directorio reservado para implementar roles (cuando aplique) que vayas desarrollando.
- **vars**
Directorio reservado para almacenar archivos de variables si así se requiere.
- **main.yml**:
En este archivo se escriben los Playbooks. El nombrado de este archivo está basado en la documentación, pero no necesariamente debe conservar este nombre.

### Pruebas locales
- **venv**:
La carpeta venv no forma parte de un proyecto de ansible, pero nos será de utilidad para ejecutar ansible localmente y así poder realizar pruebas en nuestros equipos cuando sea necesario.

Para lograr esto, se implementa un *virtual environment* de python en el que se instala ansible y toda la paquetería que necesitemos. Para activarlo, seguir los siguientes pasos:

1. Crear el *virtual environment*
    ```shell
    python3 -m venv venv/.venv
    ```

1. Activar el *virtual environment*
    ```shell
    source venv/.venv/bin/activate
    ```

1. Instalar ansible
    ```shell
    python3 -m pip install -r venv/requirements.txt
    ```

Después de esta serie de comandos ya podrás ejecutar comandos de ansible y a la vez seguir usando tu terminal de manera normal. Sí deseas desactivar el *virtual environment* ejecuta el siguiente comando:
```shell
deactivate
```

> [!NOTE]
> Te invitamos a utilizar este README.md para documentar tu proyecto, el contenido actual es únicamente para guiarte y puedes borrarlo cuando ya no lo necesites. 