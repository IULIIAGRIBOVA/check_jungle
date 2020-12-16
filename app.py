from flask import Flask, render_template, url_for, request, jsonify
from jj import my_jj, my_jj_jungle
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")



@app.route("/process", methods=['POST'])
def process():
    Search_url = request.form['SearchPage']
    AuthorName = request.form['AuthorName']
    TrackName = request.form['TrackName']

    if (Search_url and AuthorName and TrackName):
        if Search_url.find("//audiojungle.net") != -1:
           PageText, PageURL = my_jj_jungle(Search_url, AuthorName, TrackName)
        else:
           PageText = 'Вы ввели неверный адрес))'
           PageURL = ''
        #PageText, PageURL = my_jj_jungle(Search_url, AuthorName, TrackName)
        return jsonify({'PageText' : PageText, 'PageURL': PageURL, 'PageURLLink':PageURL, 'Error':False})
    Missing = 'Вы не заполнили одно или несколько полей))'
    PageURL = ''
    return jsonify({'PageText' : Missing, 'PageURL':PageURL, 'PageURLLink':PageURL,'Error' : True})


@app.route("/contact")
def contact_me():
    return render_template("contact.html")

if __name__ == '__main__':
	app.run(debug=True)