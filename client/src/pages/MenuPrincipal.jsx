import { useState } from "react";

function App() {
  const [counter, setCounter] = useState(0);

  function Count() {
    if (counter == 0) {
      return <p>I have not been pressed yet</p>;
    } else if (counter == 1) {
      return <p>I have been pressed 1 single time!</p>;
    } else {
      return <p>I have been pressed {counter} times!</p>;
    }
  }

  return (
    <div>
      <button onClick={() => setCounter(counter + 1)}>Press me</button>
      {Count()}
    </div>
  );
}

export default App;
