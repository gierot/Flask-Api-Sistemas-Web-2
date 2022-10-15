from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify, json
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('comentarios', __name__)

@bp.route('/comentarios')
def list_comentarios():
    db = get_db()
    comments = db.execute(
        'SELECT * FROM comentarios'
        ' ORDER BY created DESC'
    )
    return {'comments':
            [dict(zip([column[0] for column in comments.description], row))
             for row in comments.fetchall()]}

@bp.route('/comentarios/create', methods=(['POST']))
def create_comentarios():

    json = request.json
    user_id = json['user_id']
    curso_id =json['curso_id']
    body =json['body']
    if not body or not user_id or not curso_id:
        raise Exception("Preencha os campos")
    db = get_db()
    db.execute(
        'INSERT INTO comentarios (body, curso_id, user_id)'
        ' VALUES (?, ?, ?)',
        (body, curso_id, user_id)
    )
    db.commit()
    return jsonify({"status": True, "message": "Comentario inserido com sucesso"})

@bp.route('/comentarios/update/<int:id>/', methods=(['PUT']))
def update_comentarios(id):
    try:
        json = request.json
        user_id = json['user_id']
        curso_id =json['curso_id']
        body =json['body']
        db = get_db()
        db.execute(
            'UPDATE comentarios SET user_id = ?, curso_id = ?, body = ?'
            ' WHERE id = ?',
            (user_id, curso_id, body, id)
        )
        db.commit()
        return jsonify({"status": True, "message": "Comentario alterado com sucesso"})
    except:
        return jsonify({"status":False,"message": "Não foi possível alterar o comentario"})

@bp.route('/comentarios/delete/<int:id>/', methods=('DELETE',))
def delete_comentarios(id):
    try:
        db = get_db()
        db.execute('DELETE FROM comentarios WHERE id = ?', (id,))
        db.commit()
        return jsonify({"status": True, "message": "Comentario deletado com sucesso"})
    except:
        return jsonify({"status":False,"message": "Não foi possível deletar o comentario"})