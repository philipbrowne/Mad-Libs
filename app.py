from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sillypuppytaco99'

story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    ["verb", "noun", "adverb", "verb_past_tense", "second_noun", "verb_with_ing"],
    """O say can you {verb}, by the dawn's early {noun}, what so {adverb} we {verb_past_tense}, at the {second_noun}'s last {verb_with_ing}."""
)

story3 = Story(["name", "animal", "noun", "plural_noun", "second_plural_noun"],  """
    {name} was a mighty {animal}. He would stomp around the jungle with a loud {noun}! The other {plural_noun} thought he was very good at hunting {second_plural_noun}            
    """
               )


@app.route('/')
def homepage():
    """Select a Madlibs Template"""
    return render_template('home.html')


@app.route('/form1')
def madlibs_form1():
    """Madlibs Story Form"""
    prompts = story1.prompts
    promptnum = len(prompts)
    return render_template('form-1.html', prompts=prompts, promptnum=promptnum)


words = {}


@app.route('/story1')
def get_story_1():
    """Returns a story based off the form """
    words['place'] = request.args.get('place')
    words['noun'] = request.args.get('noun')
    words['verb'] = request.args.get('verb')
    words['adjective'] = request.args.get('adjective')
    words['plural_noun'] = request.args.get('plural_noun')
    newstory = story1.generate(words)
    return render_template('story.html', story=newstory)


@app.route('/form2')
def madlibs_form2():
    """Madlibs Story Form"""
    prompts = story2.prompts
    promptnum = len(prompts)
    return render_template('form-2.html', prompts=prompts, promptnum=promptnum)


@app.route('/story2')
def get_story_2():
    """Returns a story based off the form """
    words['verb'] = request.args.get('verb')
    words['noun'] = request.args.get('noun')
    words['adverb'] = request.args.get('adverb')
    words['verb_past_tense'] = request.args.get('verb_past_tense')
    words['second_noun'] = request.args.get('second_noun')
    words['verb_with_ing'] = request.args.get('verb_with_ing')
    newstory = story2.generate(words)
    return render_template('story.html', story=newstory)


@app.route('/form3')
def madlibs_form3():
    """Madlibs Story Form"""
    prompts = story3.prompts
    promptnum = len(prompts)
    return render_template('form-3.html', prompts=prompts, promptnum=promptnum)


@app.route('/story3')
def get_story_3():
    """Returns a story based off the form """
    words['name'] = request.args.get('name')
    words['animal'] = request.args.get('animal')
    words['noun'] = request.args.get('noun')
    words['plural_noun'] = request.args.get('plural_noun')
    words['second_plural_noun'] = request.args.get('second_plural_noun')
    newstory = story3.generate(words)
    return render_template('story.html', story=newstory)
