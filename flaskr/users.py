from flask import (
    Blueprint, request, jsonify
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('user', __name__)

@bp.route('/user')
def list_user():
    db = get_db()
    user = db.execute(
        'SELECT * FROM user'
    )
    return {'user':
            [dict(zip([column[0] for column in user.description], row))
             for row in user.fetchall()]}

@bp.route('/user/create', methods=(['POST']))
def create_user():
    try:
        json = request.json
        username = json['username']
        password =json['password']
        if not username or not password:
            raise Exception()
        db = get_db()
        db.execute(
            'INSERT INTO user (username, password)'
            ' VALUES (?, ?)',
            (username, password)
        )
        db.commit()
        return jsonify({"status": True, "message": "Usuário inserido com sucesso"})
    except:
        return jsonify({"status":False,"message": "Não foi possível inserir o usuário"})

@bp.route('/user/update/<int:id>/', methods=(['PUT']))
def update_user(id):
    try:
        json = request.json
        username = json['username']
        password =json['password']
        if not username or not password:
            raise Exception()
        db = get_db()
        db.execute(
            'UPDATE user SET username = ?, password = ?'
            ' WHERE id = ?',
            (username, password, id)
        )
        db.commit()
        return jsonify({"status": True, "message": "Usuário alterado com sucesso"})
    except:
        return jsonify({"status":False,"message": "Não foi possível alterar o usuário"})

@bp.route('/user/delete/<int:id>/', methods=('DELETE',))
def delete_user(id):
    try:
        db = get_db()
        db.execute('DELETE FROM user WHERE id = ?', (id,))
        db.commit()
        return jsonify({"status": True, "message": "Usuário deletado com sucesso"})
    except:
        return jsonify({"status":False,"message": "Não foi possível deletar o usuário"})