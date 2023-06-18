import { useEffect, useState } from "react";
import "./index.css";
// import { api } from "../../api";

function Table({ topics }) {
    const [data, setData] = useState({patients:[{name: "João", id: 0},{name: "Pedro", id: 1},{name: "José", id: 2}, {name: "Marcelo", id: 3}]});
    
    useEffect(() => {
        // const getData = async () => {
        //     await api.get("")
        // }

    }, [])

  const headerConstruction = () => {
    const headerList = topics.map((topic) => {
      return (
        <>
          <th id={`coluna-${topic}`}>{topic}</th>
        </>
      );
    });

    return headerList;
  };

  const tableData = () => {
    const dataList = data.patients.map((data) => {
        return (
            <>
                <tr key={data.id}>
                    <td>{data.name}</td>
                </tr>
            </>
        )
    });

    return dataList
  }

  return (
    <table>
      <tbody>
        <tr>{headerConstruction()}</tr>
        {tableData()}
      </tbody>
    </table>
  );
}

export default Table;
