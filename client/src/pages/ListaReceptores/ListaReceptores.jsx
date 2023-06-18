import Navbar from "../../components/Navbar/Navbar";
import Table from "../../components/Table/Table";
import "./index.css";

function ListaReceptores() {
  return (
    <div className="PageContainer">
      <Navbar />
      <div className="ListaReceptoresContainer">
        <h1>Lista de Receptores</h1>
        <Table />
      </div>
    </div>
  );
}

export default ListaReceptores;
