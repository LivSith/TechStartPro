# Descrição
Sistema web para cadastrar produtos e importar categorias de um arquivo CSV.


# Instruções de instalação (configuração)
1. Clone o repositório
1. Criar uma maquina virtual;
2. Acessar a maquina virtual;
3. Instalar os requisitos do ambiente;
    pip install -r requirements.txt
4. Banco de dados (estamos usando o padrão do Django, o sqlite);
5. Criar usuario (caso seja necessario acessar o admin);
6. Abrir o navegador e acessar 'http://127.0.0.1:8000/'
7. E começar a usar \0/


# Testes
...

# Breve descrição do ambiente de trabalho utilizado para executar este projeto

Computador: Lenovo G470, Core i5, 4Gib de Memória, 
sistema operacional: Linux Ubuntu 20.4
IDE: VSCode 1.50.1
Bibliotecas: 
 - dj-database-url: Auxilia no gerenciamento de banco de dados local e em rodando remoto.
 - dj-static: Para servir os statics file.
 - Django:
 - python-decouple: Permite separar as instancias DEBUG e SECRET_KEY do projeto.
 - pytz:
 - sqlparse:
 - static3:
 - gunicorn: servidor do heroku
 - psycopg2-binary: drive do banco PostgreSQL, q será usado no heroku.



Foi bem divertido ^_^