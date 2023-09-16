from flask import jsonify
from flask_jwt_extended import jwt_required

from app.tasks import send_confirmation_mail, send_password_reset_mail, send_verification_mail


@jwt_required()
def test():
    return jsonify({"msg": "Successfully"})


@jwt_required()
def send_confirm_email(email_data):
    username = email_data.get("username")
    email = email_data.get("email")
    verification_link = email_data.get("verification_link")
    send_confirmation_mail.delay(username, email, verification_link)
    return jsonify({"msg": "Send confirmation email successfully"}), 200


@jwt_required()
def send_password_reset_email(email_data):
    username = email_data.get("username")
    email = email_data.get("email")
    reset_link = email_data.get("reset_link")
    send_password_reset_mail.delay(username, email, reset_link)
    return jsonify({"msg": "Send password reset email successfully"}), 200


@jwt_required()
def send_verification_email(email_data):
    username = email_data.get("username")
    email = email_data.get("email")
    verification_link = email_data.get("verification_link")
    send_verification_mail.delay(username, email, verification_link)
    return jsonify({"msg": "Send password reset email successfully"}), 200
