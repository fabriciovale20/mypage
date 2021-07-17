# TABELA DE NOMENCLATURAS TCM TELECOM

*Página Web que contém todos os Padrões MAC/SN detalhados com Categoria, Marca, Modelo, Valor e Informações adicionais*

## Como rodar o projeto:
1. Clone o repositório;
```
git clone https://github.com/fabriciovale20/sitetcm.git
```
2. Acesse a pasta do projeto;
```
cd sitetcm
```
3. Crie um ambiente virtual com Python 3;
```
python -m venv .venv
```
4. Ative o Virtualenv;
```
.venv\Scripts\activate
```
5. Instale as dependências;
```
pipenv install
```
6. Rode as migrações;
```
python manage.py migrate
```
7. Rode o servidor.
```
python manage.py runserver
```
