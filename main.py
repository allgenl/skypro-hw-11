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


@app.route("/search/<candidate_name>/") # поиск по имени
def search(candidate_name):
    candidates_name = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates_name, count=len(candidate_name))


@app.route("/skills/<skill>/") # поиск по скиллу
def have_skills(skill):
    candidate_name = get_candidates_by_skill(skill)
    return render_template('skill.html', candidates=candidate_name, count=len(candidate_name), skill=skill)


app.run(debug=True)