from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_skill, get_candidates_by_name

app = Flask(__name__)

data = load_candidates_from_json("candidates.json")


@app.route("/") # список всех
def index():
    return render_template('list.html', candidates=data)


@app.route("/candidate/<int:uid>/") # страничка кандидата
def profile(uid):
    candidate = get_candidate(uid)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<name>/") # поиск по имени
def search(name):
    candidate_name = get_candidates_by_name(name)
    return render_template('search.html', candidates=candidate_name, count=len(candidate_name))


# @app.route("/skills/<skill>/") # поиск по скиллу
# def search(skill):
#     candidate_name = get_candidates_by_skill(skill)
#     return render_template('skills.html', candidates=candidate_name, count=len(candidate_name))


print(get_candidates_by_name("A"))

app.run(debug=True)