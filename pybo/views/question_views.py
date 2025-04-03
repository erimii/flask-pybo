# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 11:18:11 2025

@author: Admin
"""

from flask import Blueprint, render_template, request, redirect, url_for, g, flash
from pybo import db
from pybo.models import Question, User
from datetime import datetime
from pybo.forms import QuestionForm

from pybo.views.auth_views import login_required
from sqlalchemy import or_

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')

    question_query = Question.query

    if kw:
        search = f"%{kw}%"
        question_query = question_query.join(User).filter(
            or_(
                Question.subject.ilike(search),
                Question.content.ilike(search),
                User.username.ilike(search)
            )
        )

    question_query = question_query.order_by(Question.create_date.desc())
    pagination = question_query.paginate(page=page, per_page=10)

    return render_template(
        'question/question_list.html',
        question_list=pagination,
        pagination=pagination,
        page=page,
        kw=kw
    )

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question) 

@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(
            subject=form.subject.data,
            content=form.content.data,
            create_date=datetime.now(),
            user=g.user
        )
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('question._list'))
    return render_template('question/question_form.html', form=form)

@bp.route('/modify/<int:question_id>', methods=('GET', 'POST'))
@login_required
def modify(question_id):
    question = Question.query.get_or_404(question_id)
    if g.user != question.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('question.detail', question_id=question_id))
    if request.method == 'POST':  # POST 요청
        form = QuestionForm()
        if form.validate_on_submit():
            form.populate_obj(question)
            question.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('question.detail', question_id=question_id))
    else:  # GET 요청
        form = QuestionForm(obj=question)
    return render_template('question/question_form.html', form=form)


@bp.route('/delete/<int:question_id>/')
@login_required
def delete(question_id):
    question = Question.query.get_or_404(question_id)
    if g.user.id != question.user_id:
        flash('삭제 권한이 없습니다.')
        return redirect(url_for('question.detail', question_id=question_id))
    
    db.session.delete(question)
    db.session.commit()
    flash('질문이 삭제되었습니다.')
    return redirect(url_for('question._list'))

@bp.route('/vote/<int:question_id>/')
@login_required
def vote(question_id):
    question = Question.query.get_or_404(question_id)
    if g.user == question.user:
        flash('본인이 작성한 글은 추천할 수 없습니다.')
    elif g.user in question.voter:
        question.voter.remove(g.user)
        db.session.commit()
    else:
        question.voter.append(g.user)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))

