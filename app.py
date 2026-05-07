from flask import Flask, render_template, request

app = Flask(__name__)

# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')


# CONTACT FORM
@app.route('/contact', methods=['POST'])
def contact():

    # FORM DATA
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # SAVE DATA INTO TXT FILE
    with open('contacts.txt', 'a', encoding='utf-8') as file:

        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Message: {message}\n")
        file.write("-----------------------------\n")

    return f'''
    <h1>Thank You {name}!</h1>

    <p>Your message has been saved successfully.</p>

    <a href="/">Go Back</a>
    '''


# SEARCH FEATURE
@app.route('/search')
def search():

    query = request.args.get('query')

    return f'''
    <h1>Search Result</h1>

    <p>You searched for: <b>{query}</b></p>

    <a href="/">Go Back</a>
    '''


# RUN SERVER
if __name__ == '__main__':
    app.run(debug=True)