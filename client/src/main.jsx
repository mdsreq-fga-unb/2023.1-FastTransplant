import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./main.css";

import Home from "./pages/Home/Home.jsx";
import Dados from "./pages/Dados/Dados.jsx";
import PainelControle from "./pages/PainelControle/PainelControle.jsx";
import ListaOrgaos from "./pages/ListaOrgaos/ListaOrgaos.jsx";
import ListaPacientes from "./pages/ListaPacientes/ListaPacientes.jsx";
import ListaReceptores from "./pages/ListaReceptores/ListaReceptores.jsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },
  {
    path: "/dados",
    element: <Dados />,
  },
  {
    path: "/painel",
    element: <PainelControle />,
  },
  {
    path: "/orgaos",
    element: <ListaOrgaos />,
  },
  {
    path: "/pacientes",
    element: <ListaPacientes />,
  },
  {
    path: "/receptores",
    element: <ListaReceptores />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
