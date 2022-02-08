from main import app

@app.route('/')
def index():
    return "Hooray"

@app.route('/fish<id>')
def get_fish(id):
    print(id)
    return "my fish is georgeus"


@app.route("/fish")
def get_all_fish():
    return "all fish is"

@app.route("fish", methods=["POST"])
def create_fish():
    print("fish_created")