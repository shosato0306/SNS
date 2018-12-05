from datatime import datatime
from flask import render_template, session, redirect, url_for
from .import main
from .forms import NameForm
from ..import db
from ..models imoport User


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'NEW USER',
                    'mail/new_user', user=user)
            flash('User registration to database is succeeded')
        else: 
            session['known'] = True
            flash('Your name is already registerd')
        session['name'] = form.name.data
        form.name.data = ""
        return redirect(url_for('.index'))
    return render_template('index.html',
                            form=form, 
                            name=session.get('name'),
                            known=session.get('known', False),
                            current_time=datetime.utcnow())
