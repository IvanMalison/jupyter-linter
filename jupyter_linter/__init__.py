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
    print "YAY it works"
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'], '/lint')
    web_app.add_handlers(host_pattern, [(route_pattern, LinterHandler)])


class LinterHandler(IPythonHandler):

    def post(self):
        request_dict = json.loads(self.request.body)
        f, file_path = tempfile.mkstemp()
        f.write(request_dict['to_lint'])
        f.close()

        linted = subprocess.check_output(["flake8", file_path])

        print(linted)
