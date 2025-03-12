from flask import Flask 
app = Flask(__name__) 

#root of application 
@app.route("/")       
def hello(): 
    return "Hello, Welcome to Antsomi" 
 
if __name__ == "__main__": 
    app.run() 
