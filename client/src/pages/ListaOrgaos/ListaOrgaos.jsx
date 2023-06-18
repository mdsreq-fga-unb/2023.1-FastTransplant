import Navbar from "../../components/Navbar/Navbar";
import Table from "../../components/Table/Table";
import "./index.css";

function ListaOrgaos() {
  return (
    <div className="PageContainer">
      <Navbar />
      <div className="ListaOrgaosContainer">
        <h1>Lista de Orgãos</h1>
        <Table topics={["Nome","", ""]}/>
      </div>
    </div>
  );
}

export default ListaOrgaos;
