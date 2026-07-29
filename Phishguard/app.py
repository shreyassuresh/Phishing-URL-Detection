from flask import Flask, render_template, request 
import pickle
import re 


app = Flask(__name__)

vector = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle form submission logic here
        url = request.form.get("url")
        #print(url)
        # Validate URL format
        cleaned_url = re.sub(r'^https?://(www\.)?', '', url)
        #print(cleaned_url)

        predict = model.predict(vector.transform([cleaned_url]))[0]
        #print(predict)

        if predict == 'bad':
            predict = "This is a Phishing Website !!"
        elif predict == 'good':
            predict = "This is a Legitimate Website !!"
        else:
            predict = "Unknown Prediction"        

        return render_template("index.html", prediction=predict)
    else:
        # Render the index page
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)