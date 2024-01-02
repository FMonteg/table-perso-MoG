from flask import Blueprint, render_template, request
from fcp_character import FCP

fcp_bp = Blueprint('fcp', __name__)


@fcp_bp.route('/fcp')
def fcp_gen():
    fcp = FCP()
    return render_template('fcp_fiche_creation_personnage.html', title='Fiche de personnage', character=fcp)

