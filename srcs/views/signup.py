from srcs.httpParser import httpParser

class SignUpView:
    def __init__(self, env, start_fn):
        self._env = env
        self._start_fn = start_fn
    
    def do_GET(self):
        status = '200 OK'
        with open("templates/signup.html", "r") as index:
            response_body = index.read()
        response_headers = [
            ('Content-Type', 'text/html'),
            ('Content-Length', str(len(response_body)))
        ]

        self._start_fn(status, response_headers)
        return [response_body.encode()]

    def do_POST(self):
        print("SignUp POST")
        status = '200 OK'

        post_arg = httpParser(self._env)
        # On sanitize / trim les input
        
        # On regarde si le nom d'utilisateur et / ou l'adresse mail existe deja dans la base de donnee
        # Si oui on renvoie un message d'erreur
        # Si non on cree le profil dans la table temporaire, on envoie le mail et on notifie l'utilisateur
        # qu'il doit valider son compte sur son adresse mail
        response_body = f"{post_arg['login']} vous etes bien connecte."

        response_headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(response_body))),
        ]

        self._start_fn(status, response_headers)
        return [response_body.encode()]