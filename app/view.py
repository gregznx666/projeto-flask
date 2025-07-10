from app import app, db
from flask import render_template, url_for, request, redirect
from app.forms import contatoForm
from app.models import Contato

@app.route('/')
def homepage():
    usuario = 'Iagozada'
    idade = 99
    context = {
        'usuario':usuario,
        'idade':idade
    }
    return render_template('index.html', context=context)

@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    form = contatoForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
    return render_template('contato.html', context=context, form=form)

@app.route('/contato/lista/')
def contatoLista():
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')
    dados = Contato.query.order_by('nome')
    if pesquisa != '':
        dados = dados.filter(Contato.nome == pesquisa)
    context = {'dados': dados.all()}

    return render_template('contato_lista.html', context=context)

@app.route('/contato/<int:id>')
def contatoDetail(id):
    obj=Contato.query.get(id)
    return render_template('contato_detail.html', obj=obj)














#@app.route('/contato/', methods=['GET', 'POST'])
#def contato():
#    form = contatoForm()
#    context={}
#
#    #if request.method == 'GET':
#        #pesquisa = request.args.get('pesquisa')
#        #print(pesquisa)
#        #context.update({'pesquisa':pesquisa})
#
#    if request.method == 'POST':
#        nome = request.form['nome']
#        email = request.form['email']
#        assunto = request.form['assunto']
#        mensagem = request.form['mensagem']
#
#        contato = contatoForm(
#            nome = nome,
#            email = email,
#            assunto = assunto,
#            mensagem = mensagem
#        )
#
#        db.session.add(contato)
#        db.session.commit
#        #pesquisa = request.form['pesquisa']
#        #print('POST', pesquisa)
#        #context.update({'pesquisa':pesquisa})
#    return render_template('contato.html', context=context, form = form) 