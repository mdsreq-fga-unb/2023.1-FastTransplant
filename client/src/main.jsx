import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

import MenuPrincipal from "./pages/MenuPrincipal.jsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <MenuPrincipal />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
