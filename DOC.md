# Descrição
Sistema web para cadastrar produtos e importar categorias de um arquivo CSV.


# Instruções de instalação (configuração)
ESte projeto usa Python 3.5.0

1. Criar uma maquina virtual chamada 'projectvenv';
>```
> $ python3 -m venv projectvenv
>```
2. Ativar maquina virtual;
>```
> $ source projectvenv/bin/activate
>```

3. Ir para a pasta correta;
>```
>$ cd TechStartPro/
>```

4. criar um arquivo, chamado '.env' na pasta do projeto com os dados:
>```
> SECRET_KEY==0sl#i1kf(*e53d7oo9i3-))u^jd3!f!bg2zfem&-@kp39mzl(
> DEBUG=True
>```

5. Instalar os requisitos do ambiente;
>```
>$ pip install -r requirements.txt
>```

6. Banco de dados;
>```
>$ python manage.py migrate
>```

7. Servidor local;
>```
>$ python manage.py runserver
>```

8. Abrir o navegador e acessar o servidor local.

 'http://127.0.0.1:8000/'

9. E começar a usar \0/


# Testes
Não foram finalizados.

# Breve descrição do ambiente de trabalho utilizado para executar este projeto

Computador: Lenovo G470, Core i5, 4Gib de Memória, 
sistema operacional: Linux Ubuntu 20.4
IDE: VSCode 1.50.1
Bibliotecas: 
 - dj-database-url: Auxilia no gerenciamento de banco de dados local e em rodando remoto.
 - dj-static: Para servir os statics file.
 - Django: Framework web
 - python-decouple: Permite separar as instancias DEBUG e SECRET_KEY do projeto.
 - gunicorn: servidor do heroku
 - psycopg2-binary: drive do banco PostgreSQL, q será usado no heroku.



Foi bem divertido ^_^