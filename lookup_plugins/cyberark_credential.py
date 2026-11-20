# Ansible lookup plugin para CyberArk CCP (Versión Ligera Local)
from __future__ import (absolute_import, division, print_function)

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
import json
import urllib.request
import urllib.parse
import ssl

class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        # Captura los parámetros enviados desde el playbook
        params = terms[0] if terms else kwargs
        
        base_url = params.get('api_base_url')
        app_id = params.get('app_id')
        safe = params.get('safe')
        obj = params.get('object')
        
        # Validar que los parámetros mínimos existan
        if not all([base_url, app_id, safe, obj]):
            raise AnsibleError("Faltan parámetros requeridos (api_base_url, app_id, safe, object)")
        
        # Construir URL de la API de CyberArk CCP con URL encode para evitar problemas con espacios o caracteres
        url = f"{base_url}/AIMWebService/api/Accounts?AppID={urllib.parse.quote(app_id)}&Safe={urllib.parse.quote(safe)}&Object={urllib.parse.quote(obj)}"
        
        # Configurar contexto SSL (Permitir ignorar certificados si validate_certs=False)
        ctx = ssl.create_default_context()
        if not params.get('validate_certs', True):
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

        try:
            # Realizar la petición HTTP GET de manera nativa sin librerías externas
            req = urllib.request.Request(url, headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req, context=ctx) as response:
                res = json.loads(response.read().decode())
                
                # El campo 'Content' en la respuesta de CyberArk contiene la contraseña
                password = res.get('Content')
                if password is None:
                    raise AnsibleError("CyberArk respondió pero no se encontró el campo 'Content' (Password)")
                
                return [password]
                
        except Exception as e:
            raise AnsibleError(f"Error al conectar con CyberArk CCP en {base_url}: {str(e)}")
