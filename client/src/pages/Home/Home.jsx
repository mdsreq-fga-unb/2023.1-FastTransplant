import DragAndDropInput from "../../components/DragAndDropInput/DragAndDropInput";
import Navbar from "../../components/Navbar/Navbar";
import "./index.css";

function Home() {
  return (
    <div className="PageContainer">
      <Navbar />
      <div className="HomeContainer">
        <h1 className="Title">Home</h1>
        <div className="InputContainer">
          <DragAndDropInput/>
        </div>
      </div>
    </div>
  );
}

export default Home;
