# 🐧 Site / Sistema Usando Linux  

Site usado como base para um projeto interno e fonte de inspiração para outros projetos semelhantes.

## 📥 Clonando o Repositório  

Para obter o projeto, execute:  

```sh
git clone https://github.com/wopgan/usandolinux.com.br.git
cd usandolinux.com.br
```

## ⚙️ Configurando o Ambiente

Antes de rodar o projeto, siga os passos abaixo para configurar o ambiente virtual e instalar as dependências.

## 🔹 Criar e ativar ambiente virtual
No Linux/macOS:

```sh
python -m venv .venv
source .venv/bin/activate
```
No Windows (PowerShell):
```pwsh
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 📦 Instalando dependências
```sh
pip install -r requirements.txt
```

## 🔧 Configurando variáveis de ambiente
```sh
cp .env.example .env
```
Edite o .env e defina suas credenciais e configurações.

## 🗄️ Configurando o Banco de Dados
Se for necessário rodar migrações antes de iniciar o projeto:

```sh
python manage.py migrate
```

## 🚀 Rodando o Projeto
Após configurar o ambiente, inicie o servidor com:

```sh
python manage.py runserver
```

O sistema estará disponível em: http://127.0.0.1:8000/