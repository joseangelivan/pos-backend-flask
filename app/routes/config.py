from flask import Blueprint, request, jsonify
from app.utils import decode_token

bp = Blueprint('config', __name__, url_prefix='/api')

@bp.route('/config', methods=['GET'])
def get_config():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Missing token'}), 401

    token = auth_header.split(' ')[1]
    payload = decode_token(token)
    if not payload:
        return jsonify({'error': 'Invalid or expired token'}), 401

    # Retornar configuración de ejemplo
    return jsonify({
        'theme': 'dark',
        'language': 'es',
        'currency': 'USD'
    })
