from srcs.httpParser import httpParser
from srcs.env import IP

class SignInView:
    def __init__(self, env, start_fn):
        self._env = env
        self._start_fn = start_fn
    
    def do_GET(self):
        print("SignIn GET")
        status = '200 OK'
        with open("templates/signin.html", "r") as index:
            response_body = index.read()
        response_headers = [
            ('Content-Type', 'text/html'),
            ('Content-Length', str(len(response_body)))
        ]

        self._start_fn(status, response_headers)
        return [response_body.encode()]

    def do_POST(self):
        print("SignIn POST")
        status = '303 See Other'

        post_arg = httpParser(self._env)
        with open("templates/signup.html", "r") as html:
            response_body = html.read()
        # On creer une connection a la base de donnee

        conn = psycopg2.connect(
            host="postgres",
            port="5432",
            database="postgres",
            user="postgres",
            password="postgres"
        )

        sql_query = "select * from camagru_user"
        cursor = conn.cursor()
        cursor.execute(sql_query)
        print(cursor.fetchall())

        cursor.close()
        conn.close()

        # On sanitize les credentials

        # On fait la requete pour recuperer le mot de passe associe a l'email 

        # On fait la comparaison des mots de passe

        response_headers = [
            ('Content-Type', 'text/html'),
            ('Content-Length', str(len(response_body))),
            ('Location', f"http://{IP}:8051/signup")
        ]

        self._start_fn(status, response_headers)
        return [response_body.encode()]