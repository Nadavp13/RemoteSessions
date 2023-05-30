from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='html')
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

code_map = {
    'code1': 'codeblocks/HelloWorld.js',
    'code2': 'codeblocks/fibonacci.js',
    'code3': 'codeblocks/BubbleSort.js',
    'code4': 'codeblocks/DFS.js'
}
code_strings = {code_id: '' for code_id in code_map}
mentor_present = False
student_count = 0


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/codeblockpage", methods=["GET"])
def codeblock():
    global mentor_present, student_count

    code_id = request.args.get('code_id')
    code_file = code_map.get(code_id)

    if code_file:
        file_path = code_map.get(code_id)  # Get the file path based on code_id

        # Extract the file name from the file path
        file_name = file_path.split('/')[-1]
        if not mentor_present:
            with open(code_file, 'r') as file:
                code_string = file.read()
                code_strings[code_id] = code_string
            return render_template("codeblockpage.html", code_preview=code_string, code_id=code_id, user_type='mentor', file_name=file_name)
        else:
            student_count += 1
            return render_template("codeblockpage.html", code_preview=code_strings[code_id], code_id=code_id, user_type='student', file_name=file_name)
    else:
        return "Invalid code ID"


@socketio.on('connect')
def handle_connect():
    global mentor_present

    if not mentor_present:
        user_type = 'mentor'
        mentor_present = True
    else:
        user_type = 'student'

    emit('user_type', user_type)
    emit('code_update', code_strings, broadcast=True)


@socketio.on('code_update')
def handle_code_update(data):
    code_id = data['code_id']
    code_content = data['code_content']
    if code_strings[code_id] != code_content:  # Only emit update if content has changed
        code_strings[code_id] = code_content
        emit('code_update', {code_id: code_content}, broadcast=True, include_self=False)


@socketio.on('save_code')
def handle_save_code(data):
    code_id = data['code_id']
    code_content = data['code_content']
    code_file = code_map.get(code_id)
    if code_file:
        with open(code_file, 'w') as file:
            file.write(code_content)
        code_strings[code_id] = code_content
        emit('code_update', {code_id: code_content}, broadcast=True)


@socketio.on('disconnect')
def handle_disconnect():
    global mentor_present, student_count

    if mentor_present:
        if student_count >= 1:
            student_count -= 1
        else:
            mentor_present = False


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80)
