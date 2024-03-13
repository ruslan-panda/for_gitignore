from flask import Flask, render_template, redirect, request, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restful import Api

from data import db_session, jobs_api
from data.users_resours import UsersResource, UsersListResource
from data.users import User
from data.jobs import Jobs
from forms.registr import RegisterForm
from forms.user import LoginForm
from forms.add_jobs import AddJobForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
@app.route('/index')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    users = db_sess.query(User).all()
    names = {name.id: name.surname + " " + name.name for name in users}
    return render_template("index.html", jobs=jobs, names=names, title='Работы')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            email=form.email.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/add_job', methods=['GET', 'POST'])
def add_job():
    add_form = AddJobForm()
    if add_form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs(
            job=add_form.job.data,
            team_leader=add_form.team_leader.data,
            work_size=add_form.work_size.data,
            collaborators=add_form.collaboretors.data,
            is_finished=add_form.is_finished.data
        )
        db_sess.add(job)
        db_sess.commit()
        return redirect("/")
    return render_template("add_job.html", title="Добавить Работы", form=add_form)


@app.route('/editjob/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_job(id):
    edit_form = AddJobForm
    if request == "GET":
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id,
                                         (Jobs.team_leader == current_user.id) | (current_user.id == 1)).first()
        if job:
            edit_form.job.data = job.data
            edit_form.team_leader.data = job.team_leaderdata,
            edit_form.work_size.data = job.work_size.data
            edit_form.collaborators.data = job.collaboretors.data
            edit_form.is_finished.data = job.is_finished.data
        else:
            abort(404)
    if edit_form.validate_on_submit():
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id,
                                         (Jobs.team_leader == current_user.id) | (current_user.id == 1)).first()
        if job:
            job.job = edit_form.job.data
            job.team_leader = edit_form.team_leader.data
            job.work_size = edit_form.work_size.data
            job.collaborators = edit_form.collaboretors.data
            job.is_finished = edit_form.is_finished.data
            db_sess.commit()
            return redirect("/")
        else:
            abort(404)
    return render_template("add_job.html", title="Редактировать работу", form=edit_form)


@app.route('/deletejob/<int:id>', methods=['GET', 'POST'])
@login_required
def delet_job(id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == id,
                                     (Jobs.team_leader == current_user.id) | (current_user.id == 1)).first()
    if job:
        db_sess.delete((job))
        db_sess.commit()
    else:
        abort(404)
    return redirect("/")



if __name__ == '__main__':
    db_session.global_init("db/jobs.db")
    app.register_blueprint(jobs_api.blueprint)
    api.add_resource(UsersListResource, "/api/v2/users")
    api.add_resource(UsersResource, "/api/v2/users/<int:user_id>")
    app.run(port=8080, host='127.0.0.1')
