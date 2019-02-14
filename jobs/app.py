from flask import Flask, request, render_template

app=Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    #return "Hello world"
    return render_template('index.html')

if __name__ == '__main__':
   app.debug = True
   app.run()
