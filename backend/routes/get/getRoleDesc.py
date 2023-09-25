from flask import Blueprint, jsonify, request
from backend.models.role import Role

getRoleDescBP = Blueprint('getRoleDesc', __name__)
# Get role description by role name
@getRoleDescBP.route('/api/roledesc', methods=['GET'])
def getRoleDesc():
    args = request.args
    role_name = args.get('role_name')
    try:
        role = Role.query.filter_by(Role_Name=role_name).first()
        if role:
            return jsonify({'RoleDesc': role.Role_Desc}), 200
        else:
            return jsonify({'error': 'Invalid role name.'}), 404

    except Exception as error:
        return jsonify({'error': str(error)}), 500
