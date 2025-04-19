import "./App.css";
import AddEditTasks from "./components/addEditTasks";

import React from "react";

const App: React.FC = () => {

  return (
    <div>
      <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />

      <AddEditTasks />
    </div>
  );
}

export default App;
