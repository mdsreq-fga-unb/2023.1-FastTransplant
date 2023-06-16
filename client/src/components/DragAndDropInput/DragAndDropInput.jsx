import { useRef, useState } from "react";
import "./index.css";

function DragAndDropInput() {
  const [ dragActive, setDragActive ] = useState(false);
  const [ data, setData ] = useState([]);
  const [ type, setType ] = useState("paciente");
  const inputRef = useRef(null);

  const handleFiles = (filesArray) => {
    setData(filesArray);
  };

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };
  
  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFiles(e.dataTransfer.files);
    }
  };
  
  const handleFileChange = (e) => {
    e.preventDefault();
    if (e.target.files && e.target.files[0]) {
      let files = []
      for(let i = 0; i < e.target.files.length; i++){
        const file = e.target.files[i];
        files.push(file);
      }
      handleFiles(files);
    }
  };

  const handleRadioChange = (e) => {
    setType(e.target.value)
  }

  const handleSubmit = () => {
    console.log(type);
    console.log(data)
  }

  const onButtonClick = () => {
    inputRef.current.click();
  };
    
  return (
    <form id="form-file-upload" onDragEnter={handleDrag} onSubmit={(e) => e.preventDefault()}>
      <input ref={inputRef} type="file" id="input-file-upload" multiple={true} onChange={handleFileChange} />
      <label id="label-file-upload" htmlFor="input-file-upload" className={dragActive ? "drag-active" : "" }>
        <div>
          <p>Arraste um ou mais arquivos aqui ou</p>
          <button className="upload-button" onClick={onButtonClick}>
            Clique para escolher os arquivos
          </button>
        </div> 
      </label>
        { dragActive && <div id="drag-file-element" onDragEnter={handleDrag} onDragLeave={handleDrag} onDragOver={handleDrag} onDrop={handleDrop}></div> }
      <div className="inputs">
        <div className="radio-inputs">
          <div>
            <label htmlFor="paciente" id="paciente">
              <input type="radio" name="type" value="paciente" onChange={handleRadioChange} checked={true} id="paciente" className="radio"/>  
              <span id="paciente">Paciente</span>
            </label>
          </div>
          <div>
            <label htmlFor="rim" id="rim">
              <input type="radio" name="type" value="rim" onChange={handleRadioChange} id="rim" className="radio"/>
              <span>Rim</span>
            </label>
          </div>
        </div>
        <button className="submit-button" onClick={handleSubmit}>Enviar</button>
      </div>
    </form>
  );
}

export default DragAndDropInput;
