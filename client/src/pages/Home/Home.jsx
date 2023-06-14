import Navbar from "../../components/Navbar/Navbar";
import "./index.css";

function Home() {
  return (
    <div className="PageContainer">
      <Navbar />
      <div className="HomeContainer">
        <h1>Home</h1>
      </div>
    </div>
  );
}

export default Home;
