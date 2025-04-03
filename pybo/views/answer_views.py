# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 12:13:34 2025

@author: Admin
"""

from datetime import datetime

from flask import Blueprint, url_for, request, g, flash, render_template
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Question, Answer
from .auth_views import login_required

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=('POST',))
@login_required
def create(question_id):
    question = Question.query.get_or_404(question_id)
    content = request.form['content']
    answer = Answer(content=content, create_date=datetime.now(), user=g.user)
    question.answer_set.append(answer)
    db.session.commit()
    return redirect('{}#answer_{}'.format(
    url_for('question.detail', question_id=question_id), answer.id))


@bp.route('/modify/<int:answer_id>/', methods=('GET', 'POST'))
@login_required
def modify(answer_id):
    answer = Answer.query.get_or_404(answer_id)

    # 작성자 권한 확인
    if g.user.id != answer.user_id:
        flash('수정 권한이 없습니다.')
        return redirect(url_for('question.detail', question_id=answer.question.id))

    if request.method == 'POST':
        answer.content = request.form['content']
        answer.modify_date = datetime.now()
        db.session.commit()
        flash('답변이 수정되었습니다.')
        return redirect('{}#answer_{}'.format(
                url_for('question.detail', question_id=answer.question.id), answer.id))

    return render_template('answer/answer_form.html', answer=answer)

@bp.route('/delete/<int:answer_id>/')
@login_required
def delete(answer_id):
    answer = Answer.query.get_or_404(answer_id)

    if g.user.id != answer.user_id:
        flash('삭제 권한이 없습니다.')
        return redirect(url_for('question.detail', question_id=answer.question.id))

    db.session.delete(answer)
    db.session.commit()
    flash('답변이 삭제되었습니다.')
    return redirect(url_for('question.detail', question_id=answer.question.id))

@bp.route('/vote/<int:answer_id>/')
@login_required
def vote(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    if g.user == answer.user:
        flash('본인이 작성한 글은 추천할 수 없습니다.')
    elif g.user in answer.voter:
        answer.voter.remove(g.user)
        db.session.commit()
    else:
        answer.voter.append(g.user)
        db.session.commit()
    return redirect('{}#answer_{}'.format(
                url_for('question.detail', question_id=answer.question.id), answer.id))
