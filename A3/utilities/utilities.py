from flask import Blueprint, request, render_template, redirect, url_for, session

import A3.adapters.repository as repo
import A3.utilities.services as services


# Configure Blueprint.
utilities_blueprint = Blueprint(
    'utilities_bp', __name__)


