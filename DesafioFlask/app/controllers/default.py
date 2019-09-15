from app import app, db, lm
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app.models.forms import LoginForm,CadastroUserForm,CadastroLivroForm,RemoverLivroForm, AlterarLivroForm
from app.models.tables import User, Livro


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET","POST"])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        user= User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Login Efetuado")
            return redirect(url_for("index"))
        else:
            flash("Login Invalido")

    return render_template('login.html',
                            form=form)

@app.route("/removeritens", methods=["GET","POST"])
def removeritens():
    form= RemoverLivroForm()
    if form.validate_on_submit():
        if Livro.query.filter_by(id=form.id.data).first():
            rem = Livro.query.filter_by(id=form.id.data).first()
            if rem.id==form.id.data:
                flash("Removido com sucesso!")
                db.session.delete(rem)
                db.session.commit()
            else:
                flash("Registro Inexistente")
        else:
            flash("Registro Inexistente")
    if current_user.is_authenticated:
        livro= Livro.query.order_by(Livro.id).all()
        return render_template('remover_itens.html',value=livro,form=form)
    else:
        return render_template("index.html",)


@app.route("/alteraritens", methods=["GET","POST"])
def alteraritens():
    form= AlterarLivroForm()
    if form.validate_on_submit():
        if Livro.query.filter_by(id=form.id.data).first():
            alt = Livro.query.filter_by(id=form.id.data).first()
            if alt.id==form.id.data:
                if form.nome.data and form.autor.data and form.categoria.data:
                    alt.nome=form.nome.data
                    alt.autor=form.autor.data
                    alt.categoria=form.categoria.data
                elif form.nome.data and form.autor.data:
                    alt.nome=form.nome.data
                    alt.autor=form.autor.data
                elif form.nome.data and form.categoria.data:
                    alt.nome=form.nome.data
                    alt.categoria=form.categoria.data
                elif form.autor.data and form.categoria.data:
                    alt.autor=form.autor.data
                    alt.categoria=form.categoria.data
                flash("Registros Alterados Com Sucesso!")
                db.session.add(alt)
                db.session.commit()
        else:
            flash("ID Incorreto")
    if current_user.is_authenticated:
        livro= Livro.query.order_by(Livro.id).all()
        return render_template('alterar_itens.html',value=livro, form=form)
    else:
        return render_template("index.html")


@app.route("/visualizaritens")
def visualizaritens():
    if current_user.is_authenticated:
        livro= Livro.query.order_by(Livro.id).all()
        return render_template('visualizar_itens.html', value=livro)
    else:
        return render_template("index.html")
    

@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out")
    return redirect(url_for("index"))

@app.route("/cadastrousuario", methods=["GET","POST"])
def cadastrousuario():
    form= CadastroUserForm()
    if form.validate_on_submit():
        user= User(form.login.data,form.senha.data,form.name.data,form.email.data)
        db.session.add(user)
        db.session.commit()
        flash("Você foi cadastrado com sucesso!")
    return render_template('cadastro_usuario.html',
                            form=form)

@app.route("/cadastroitens", methods=["GET","POST"])
def cadastroitens():
    form= CadastroLivroForm()
    if form.validate_on_submit():
        livro = Livro(form.nome.data,form.autor.data,form.categoria.data,form.idioma.data)
        db.session.add(livro)
        db.session.commit()
        flash("Cadastro Efetuado!")
    if current_user.is_authenticated:
        return render_template('cadastro_itens.html', form=form)
    else:
        return render_template("index.html")




@app.route("/teste/<info>")
@app.route("/teste", defaults={"info":None})
def teste(info):
    r = User.query.filter_by(username="").first()
    
    db.session.delete(r)
    db.session.commit()
    return "ok"