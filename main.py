#!/usr/bin/python3
from flask import Flask, render_template
from config import cfg
from cacher import cacher

app = Flask(__name__)

# Default jinja render example
@app.route("/")
def template_test():
    return render_template(
        'template.html',
        string_param="Test String Param!",
        list_param=[1, 2, 3]
    )


# Cacher class usage
@app.route("/test")
def template_test2():
    #You can cache any template in redis data structure
    cacher.cache_template('templates/template2.html', 'some_keyword')

    # You can get yor cached template by key
    print(cacher.get_cache('some_keyword'))

    return render_template(
        'template2.html',
        string_param="Test String Param!",
        list_param=[4, 5, 6]
    )


if __name__ == '__main__':
    app.run(debug=cfg.FLASK_DEBUG_MODE)
