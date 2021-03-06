from api import API

app = API()


@app.route("/home")
def home(request, response):
    response.text = "This is HOME."


@app.route("/about")
def about(request, response):
    response.text = "This is ABOUT."


@app.route("/hello/{name}")
def home(request, response, name):
    response.text = f"Bonjour {name}!"


@app.route("/class")
class MyClass:
    def get(self, request, response):
        response.text = f"GET method"

    def post(self, request, response):
        response.text = f"POST method"

