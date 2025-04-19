import { useEffect, useState } from "react";
// import axios from "axios";
import "./addEditTasks.css";

interface Task {
  _id: string;
  text: string;
  completed: boolean;
  dueDate?: string;
}

function App() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [newTask, setNewTask] = useState<string>("");
  const [dueDate, setDueDate] = useState<string>("");

  useEffect(() => {

    // axios.get<Task[]>("http://localhost:5000/tasks").then((res) => setTasks(res.data));
  }, []);

  const addTask = () => {
    setTasks((tasks) => [
      ...tasks,
      { _id: Date.now().toString(), text: newTask, completed: false, dueDate: dueDate || undefined },
    ]);
    // if (!newTask.trim()) return;

    // axios
    //   .post<Task>("http://localhost:5000/tasks", {
    //     text: newTask,
    //     dueDate: dueDate || undefined,
    //   })
    //   .then((res) => {
    //     setTasks((prev) => [...prev, res.data]);
    //     setNewTask("");
    //     setDueDate("");
    //   });
  };

  const toggleTask = (id: string) => {
    // axios.put<Task>(`http://localhost:5000/tasks/${id}`).then((res) => {
    //   setTasks((prev) => prev.map((task) => (task._id === id ? res.data : task)));
    // });
    setTasks((prev) =>
      prev.map((task) => (task._id === id ? { ...task, completed: !task.completed } : task))
    );
    setNewTask("");
    setDueDate("");
  };

  const deleteTask = (id: string) => {
    // axios.delete(`http://localhost:5000/tasks/${id}`).then(() => {
    //   setTasks((prev) => prev.filter((task) => task._id !== id));
    // });
    setTasks((prev) => prev.filter((task) => task._id !== id));
    setNewTask("");
    setDueDate("");
  };

  return (
    <div className="addEditTasks">
      <div className="left-panel">
        <h1>Create Task</h1>
        <input
          type="text"
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}
          placeholder="Enter a task..."
        />
        <input
          type="date"
          value={dueDate}
          onChange={(e) => setDueDate(e.target.value)}
        />
        <button onClick={addTask}>Add Task</button>
      </div>
  
      <div className="right-panel">
        <h1>Task List</h1>
        <ul>
          {tasks.map((task) => (
            <li key={task._id}>
              <span>
                {task.text}
                {task.dueDate && (
                  <small>Due: {new Date(task.dueDate).toLocaleDateString()}</small>
                )}
              </span>
              <div>
                <button onClick={() => toggleTask(task._id)}>✔</button>
                <button onClick={() => deleteTask(task._id)}>❌</button>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
  
}

export default App;
