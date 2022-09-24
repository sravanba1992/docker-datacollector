from flask import Flask,render_template, request
#from flask_sqlalchemy import SQLAlchemy



app =Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@127.0.0.1/mydb'
#db=SQLAlchemy(app)

# class Data(db.Model):
#     __tablename__="data"
#     id=db.Column(db.Integer, primary_key=True)
#     email=db.Column(db.String(120),unique=True)
#     height=db.Column(db.Integer)
#
#     def __init__(self, email_,height_):
#         self.height_ = height_
#         self.email_=email_
        


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success_method():
    if request.method=='POST':
        email = request.form['email_name']
        height = request.form['height_name']
        return render_template("success.html")

if __name__=="__main__":
    app.debug=True
    app.run()
