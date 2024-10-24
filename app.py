from flask import Flask, request
from model.LoginModel import LoginDto, LoginDao

app = Flask(__name__)

@app.route('/api/v1/user/login', methods=['POST'])
def user_verify_auth():
    resp = {"cd": "000", "sms": "Success!"}
    payload = request.json
    dto = LoginDto()
    dto.UName = payload['uname']
    dto.UPass = payload['upass']
    dao = LoginDao()
    if dao.verify_auth(dto):
        resp = {"cd": "000", "sms": "Success!"}
    else:
        resp = {"cd": "888", "sms": "Failed!"}
    return resp

@app.route('/api/v1/user/confirm', methods=['POST'])
def user_confirm_code():
    resp = {"cd": "000", "sms": "Success!"}
    payload = request.json
    dto = LoginDto()
    dto.UName = payload['uname']
    dto.UPass = payload['upass']
    dto.ConfirmCode = payload['confirm_code']
    dao = LoginDao()
    if dao.confirm_code(dto):
        resp = {"cd": "000", "sms": "Success!"}
    else:
        resp = {"cd": "888", "sms": "Failed!"}
    return resp

if __name__ == "__main__":
    app.run(port=9091, debug=True)
