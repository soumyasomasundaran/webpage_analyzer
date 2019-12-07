from flask import Flask, render_template,request
import page_analyze
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', )

@app.route('/report.html')
def report():
    url_input= request.args.get('address')
    report=page_analyze.page_analyze(url_input)
    mostcommon=report[0]
    m_common=[]
    for i in mostcommon:
        m_common.append(i[0])
    linecount=report[1]
    wordcount=report[2]
    u_words=report[3]
    return(render_template('report.html',m_common=m_common,linecount=linecount,wordcount=wordcount,u_words=u_words))

if __name__ == '__main__':
    app.run(debug=True)