from flask import Flask, request
from models.task import Task

# __name__ = "main"
app = Flask(__name__)

# CRUD
# CREATE READ UPDATE and DELETE
# CRIAR, LER/VISUALIZAR, ATUALIZAR e DELETAR
# Tabela: Tarefa

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    print(data)
    return 'Test'

if __name__ == "__main__":
    app.run(debug=True)
