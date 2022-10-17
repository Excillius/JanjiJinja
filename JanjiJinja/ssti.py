from flask import Flask, request, render_template, render_template_string, url_for, redirect

app = Flask(__name__, template_folder="./")

app.secret_key = "BEECTF{3s_3s_t1_a1_Gg3Z_h3h3_g12l2bi30l}"

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/contact', methods=['POST', 'GET'])
def postContact():
    if request.method == 'POST':
        text = request.form['text']
        if "{{" in text:
            return "I tell you it won't work!"
        else:
            text
        return render_template_string(text)
    return render_template('contact.html')

@app.route('/coffee')
def getCoffee():
    return render_template('coffee.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
