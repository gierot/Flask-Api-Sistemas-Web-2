from flask import (
    Blueprint, request, jsonify
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('cursos', __name__)

@bp.route('/cursos')
def list_cursos():
    db = get_db()
    cursos = db.execute(
        'SELECT * FROM cursos'
    )
    return {'cursos':
            [dict(zip([column[0] for column in cursos.description], row))
             for row in cursos.fetchall()]}

@bp.route('/cursos/create', methods=(['POST']))
def create_cursos():
    try:
        json = request.json
        nome = json['nome']
        descricao =json['descricao']
        link =json['link']
        if not nome or not descricao or not link:
            raise Exception()
        db = get_db()
        db.execute(
            'INSERT INTO cursos (nome, descricao, link)'
            ' VALUES (?, ?, ?)',
            (nome, descricao, link)
        )
        db.commit()
        return jsonify({"status": True, "message": "Curso inserido com sucesso"})
    except:
        return jsonify({"status":False,"message": "Não foi possível inserir o curso"})

@bp.route('/cursos/update/<int:id>/', methods=(['PUT']))
def update_cursos(id):
    try:
        json = request.json
        nome = json['nome']
        descricao =json['descricao']
        link =json['link']
        db = get_db()
        db.execute(
            'UPDATE cursos SET nome = ?, descricao = ?, link = ?'
            ' WHERE id = ?',
            (nome, descricao, link, id)
        )
        db.commit()
        return jsonify({"status": True, "message": "Curso alterado com sucesso"})
    except:
        return jsonify({"status":False,"message": "Não foi possível alterar o curso"})

@bp.route('/cursos/delete/<int:id>/', methods=('DELETE',))
def delete_cursos(id):
    try:
        db = get_db()
        db.execute('DELETE FROM cursos WHERE id = ?', (id,))
        db.commit()
        return jsonify({"status": True, "message": "Curso deletado com sucesso"})
    except:
        return jsonify({"status":False,"message": "Não foi possível deletar o curso"})