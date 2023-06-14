import "./index.css";

function NavbarItem({ address, text }) {
  return (
    <>
      <a href={address}>
        <button className="button">{text}</button>
      </a>
    </>
  );
}

export default NavbarItem;
