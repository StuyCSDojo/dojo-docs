import flask
import os.path

from lib.security import AuthManager
from lib.security import security
from lib.security import security_utils
from lib.utils import utils

docs_views = flask.Blueprint('docs_views', __name__)
auth_manager = AuthManager.AuthManager('dojo_website')

@docs_views.route('/testing/docs/')
@docs_views.route('/testing/docs/<path:filename>')
@utils.log_name
@security_utils.nocache
@security.login_required(developer_required=True)
def render_documentation(filename='index.html'):
    path = os.path.join('docs/build/html', filename)
    return flask.current_app.send_static_file(path)
