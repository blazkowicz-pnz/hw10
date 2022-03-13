from flask import Flask
from utils import load_data_from_json

data = load_data_from_json()
app = Flask(__name__)

candidates = load_data_from_json()

@app.route("/")
def page_index():
    str_candidates = "<pre>"
    for candidate in candidates.values():
        str_candidates += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n\n"
    str_candidates += "</pre>"
    return str_candidates


@app.route("/candidate/<int:id>")
def profile(id):
    candidate = candidates[id]
    str_candidates = f"<img src={candidate['picture']}> <br>{candidate['name']} <br>{candidate['position']}<br>{candidate['skills']}<br><br>"
    return str_candidates


@app.route("/skills/<skill>")
def skills(skill):
    str_candidates = "<pre>"
    for candidate in candidates.values():
        candidate_skills = candidate["skills"].split(", ")
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill in candidate_skills:
            str_candidates += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n\n"
    str_candidates += "</pre>"
    return str_candidates


app.run(debug=True)



# @app.route("/skills/")
# def page_skills():
#     return "Скиллзы"
#
# app.run()
#
# candidates = load_data_from_json()
#     str_candidates = "<pre>"
#     for canditate in candidates.value():
#         str_candidates += f"{canditate['name']} \n {canditate['position']} \n {canditate['skills']} \n\n"
#     str_candidates += "</pre>"
#     print(str_candidates)