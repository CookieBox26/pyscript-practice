"""
このファイルは PyScript デモの TODO App (https://pyscript.net/examples/todo.html)
とほぼ同じでコードを自分にわかりやすいよう最小限にしたものです
自分の改変部分について万全を期しません
"""
tasks = []

# タスクのテンプレート、タスク表示箇所、新規タスク入力欄を取得
task_template = Element("task-template").select(".task", from_content=True)
task_list = Element("list-tasks-container")
new_task_content = Element("new-task-content")


# 新規タスク追加処理
def add_task(*args, **kwargs):
    if not new_task_content.element.value:
        # 新規タスク入力欄が空なら何もしない
        return None

    # 新しいIDを割り当て入力欄の内容で新規タスクを生成
    task_id = f"task-{len(tasks)}"
    task = {
        "id": task_id,
        "content": new_task_content.element.value,
        "done": False,
    }
    tasks.append(task)
    task_html = task_template.clone(task_id)
    task_html_content = task_html.select("p")
    task_html_content.element.innerText = task["content"]

    # チェックボックスクリック時には取り消し線を加えたり除去したりするようにする
    def check_task(evt=None):
        task["done"] = not task["done"]
        if task["done"]:
            task_html_content.element.classList.add("line-through")
        else:
            task_html_content.element.classList.remove("line-through")
    task_html_check = task_html.select("input")
    task_html_check.element.onclick = check_task

    # 生成した新規タスクを表示、入力欄をクリア
    task_list.element.appendChild(task_html.element)
    new_task_content.clear()


# 全リセット（独自に追加）
def remove_all(*args, **kwargs):
    task_list.element.innerHTML = ""
    tasks = []


# 新規タスク入力欄でエンターキーが押下されたときにもタスクを追加するようにする
def add_task_event(e):
    if e.key == "Enter":
        add_task()
new_task_content.element.onkeypress = add_task_event
