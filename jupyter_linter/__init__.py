import json
import tempfile
import subprocess

from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler

def load_jupyter_server_extension(nb_server_app):
    """Called when the extension is loaded.

    Args: nb_server_app (NotebookWebApplication): handle to the Notebook
        webserver instance.

    """
    print("YAY it works")
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'], '/lint')
    web_app.add_handlers(host_pattern, [(route_pattern, LinterHandler)])


class LinterHandler(IPythonHandler):

    def post(self):
        request_dict = json.loads(self.request.body)
        f = tempfile.NamedTemporaryFile(delete=False)

        print(request_dict)

        with f as f_object:
            f_object.write(request_dict['to_lint'].encode('utf-8'))

        process = subprocess.Popen(["flake8", f.name], stdout=subprocess.PIPE)

        print("done")
        linted = process.stdout.read()

        print(linted)
        self.finish(linted)
