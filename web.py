import streamlit as st
import function_file

todos = function_file.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function_file.write_todos(todos)

st.title("TO-DO App")
st.subheader("A interactive todo app")
st.write("Todos improves productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function_file.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label = "To enter new-todo's:", placeholder="Add todo...", key="new_todo"
              , on_change = add_todo)

