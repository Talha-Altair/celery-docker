from flask import *
import tasks

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def start():

    if request.method == 'POST':

        result = tasks.do_task.delay()

        return render_template('index.html')

    return render_template('index.html') 

if __name__ == "__main__":

    app.run(debug=True,host="0.0.0.0",port=8500)
