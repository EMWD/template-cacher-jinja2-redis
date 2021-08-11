from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template(
        'template.html',
        string_param="Test String Param!",
        list_param=[1, 2, 3]
    )


if __name__ == '__main__':
    app.run(debug=True)
