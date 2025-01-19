from flask import Flask, render_template, request
import  requests
from datetime import datetime
import smtplib

year = datetime.now().year

response = requests.get('https://api.npoint.io/81949f3184514fc0e328')
posts = response.json()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', all_posts=posts)

@app.route('/post.html')
def post():
    return render_template('post.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login("EMAIL", "PASSWORD")
            connection.sendmail(
                from_addr="EMAIL",
                to_addrs=data['email'],
                msg=f"Subject: New Email\n\nName: {data['name']}\n"
                    f"Email: {data['email']}\n"
                    f"Phone: {data['phone']}\n"
                    f"Message:\n{data['message']}"
            )
        # print(data['name'])
        # print(data['email'])
        # print(data['phone'])
        # print(data['message'])
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)

@app.context_processor
def inject_year():
    return {'year': datetime.now().year}

# @app.route('/form_entry', methods=['POST'])
# def receive_data():
#     return "Successfully sent your message"



@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == '__main__':
    app.run(debug=True)

