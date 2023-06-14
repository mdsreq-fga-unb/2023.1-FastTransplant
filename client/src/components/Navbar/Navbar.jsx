import NavbarItem from "../NavbarItem/NavbarItem";
import "./index.css";

function Navbar() {
  return (
    <div className="navbar-container">
      <h1 className="navbar-title">FastTransplant</h1>
      <div className="spacer"></div>
      <NavbarItem address="/" text="Home" />
      <NavbarItem address="/dados" text="Dados" />
      <NavbarItem address="/painel" text="Painel de Controle" />
      <NavbarItem address="/orgaos" text="Lista de Orgãos" />
      <NavbarItem address="/pacientes" text="Lista de Pacientes" />
      <NavbarItem address="/receptores" text="Lista de Receptores" />
      <NavbarItem address="/" text="Opção" />
      <div className="spacer last"></div>
      <p className="credit">Equipe 0011 - 2023</p>
    </div>
  );
}

export default Navbar;
