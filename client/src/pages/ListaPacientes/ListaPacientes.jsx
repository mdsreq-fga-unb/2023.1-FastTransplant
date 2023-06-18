import Navbar from "../../components/Navbar/Navbar";
import Table from "../../components/Table/Table";
import "./index.css";

function ListaPacientes() {
  return (
    <div className="PageContainer">
      <Navbar />
      <div className="ListaPacientesContainer">
        <h1>Lista de Pacientes</h1>
        <Table topics={["Nome", "", ""]} />
      </div>
    </div>
  );
}

export default ListaPacientes;
