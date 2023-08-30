from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yurr'
app.debug = True

debug = DebugToolbarExtension(app)

@app.route("/test")
def test():
    return "hi"

@app.route("/form")
def form():
    return render_template("form.html", story = stories.story)

@app.route("/story")
def story():
    args = request.args
    return render_template("story.html", text = stories.story.generate(args))






