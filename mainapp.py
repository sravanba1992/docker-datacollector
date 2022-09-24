from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy



app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://root:root@127.0.0.1/datacollector'
db=SQLAlchemy(app)

class Data(db.Model):
    """"This is base class """
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120),unique=True)
    height=db.Column(db.Integer)

    def __init__(self, email_,height_):
        self.height = height_
        self.email=email_
        


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success_method():
    if request.method=='POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        data = Data(email,height)
        db.session.add(data)
        db.session.commit()
        return render_template("success.html")

if __name__=="__main__":
    app.debug=True
    app.run()
