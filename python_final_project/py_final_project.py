from flask import Flask, render_template, request, redirect
app= Flask(__name__)
from textblob import TextBlob
def sentiment(text):
    if type(text) == float:
        text = str(text)
    analysis = TextBlob(text)
    score = round(analysis.sentiment.polarity,2)
    if score > 0:
        score_text = 'positive'
    elif score  < 0:
        score_text = 'negative'
    else:
        score_text = 'neutral'
    score_percent = (str(int(abs(score) * 100)))
    if score_percent == '0':
	return("The sentiment is neutral.")
    else:
	return("The sentiment of this text is " + score_percent + "% " + score_text+".")

@app.route("/", methods=['GET', 'POST'])
def index():
    text_inputs=""
    text_outputs=""
    if request.method == 'POST':
        text_inputs=request.form["text_area"]
    score = sentiment (text_inputs)
    return render_template("index2.html", text_input=text_inputs, text_output=score)

if __name__== '__main__':
   #app.run(host='0.0.0.0',port=80, debug=True)
   app.run()
		