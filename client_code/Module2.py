import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing
from .main_form import MainForm
from .login_page import LoginPage
from .signup_page import SignupPage

# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module2
#
#    Module2.say_hello()
#


def say_hello():
  print("Hello, world")

routing.router.routes = {
    '': MainForm,         # Default route, loads MainForm initially
    'main': MainForm,     # Route for MainForm
    'login': LoginPage,   # Route for LoginPage
    'signup': SignupPage  # Route for SignupPage
}
