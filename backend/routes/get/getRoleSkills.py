from flask import Flask, Blueprint, jsonify, request
from backend.models.staff import Staff
from backend.models.roleskills import RoleSkills

getRoleSkillsBP = Blueprint('getRoleSkills', __name__)
@getRoleSkillsBP.route('/api/roleskills', methods=['GET'])
def getRoleSkills():
    try:
        email = request.args.get('email')
        user = Staff.query.filter_by(Email=email).first()
        if user:
            sid = user.Staff_ID

            skills = StaffSkills.query.filter_by(Staff_ID = sid).all()
            skill_list = [skills.serialize() for skill in skills]

            return jsonify({'skills': skill_list}), 200

        
    except Exception as error:
        return jsonify({'error': str(error)}), 500