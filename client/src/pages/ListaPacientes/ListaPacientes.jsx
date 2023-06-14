import Navbar from "../../components/Navbar/Navbar";
import "./index.css";

function ListaPacientes() {
  return (
    <div className="PageContainer">
      <Navbar />
      <div className="ListaPacientesContainer">
        <h1>Lista de Pacientes</h1>
      </div>
    </div>
  );
}

export default ListaPacientes;
