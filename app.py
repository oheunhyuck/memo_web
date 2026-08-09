from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient 
app = Flask(__name__)

client = MongoClient('localhost', 27017)  
db = client.dbjungle  


@app.route('/')
def home():
   return render_template('index.html')


@app.route('/memo', methods=['POST'])
def post_memo():
  
    title = request.form['title']  
    context = request.form['context']  

  
   

    data = {'title': title, 'context': context,'likes':0}
    db.memos.insert_one(data)

    return jsonify({'result': 'success'})


@app.route('/memo', methods=['GET'])
def read_memos():
    result = list(db.memos.find({}, {'_id': False}).sort('likes', -1))
    return jsonify({'all_memos': result})

@app.route('/memo/like', methods=['POST'])
def like_memo():
    title = request.form['title']
    db.memos.update_one(
        {'title': title},           
        {'$inc': {'likes': 1}}      
        
    )
    return jsonify({'result': 'success'})

@app.route('/memo/delete', methods=['POST'])
def delete_memo():
    title = request.form['title']
    
    db.memos.delete_one({'title':title})
    return jsonify({'result': 'success'})

@app.route('/memo/update', methods=['POST'])
def update_memo():
    old_title = request.form['old_title']      
    new_title = request.form['new_title']      
    new_context = request.form['new_context']  
    db.memos.update_one(
        {'title': old_title},
        {'$set': {'title': new_title, 'context': new_context}}
    )
    return jsonify({'result': 'success'})
    


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)