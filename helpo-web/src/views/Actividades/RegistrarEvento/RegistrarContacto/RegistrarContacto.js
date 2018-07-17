import React from 'react';
import PropTypes from 'prop-types';


const inputPropTypes = {
  contactNum: PropTypes.number.isRequired,
  onClickRemove: PropTypes.func.isRequired,
  contactId: PropTypes.number.isRequired,
  onContactChange: PropTypes.func.isRequired,
  onPhoneChange: PropTypes.func.isRequired,
  contactValues: PropTypes.shape({
    nombre: PropTypes.string,
    email: PropTypes.string,
    telefono: PropTypes.number,
  }).isRequired,
};

function ContactoInput({
  contactNum, onClickRemove, contactId, onContactChange, onPhoneChange, contactValues,
}) {
  return (
    <div className="form-group">
      <h6>Contacto {contactNum}</h6>
      <label htmlFor={`nombre-contacto${contactId}`}>
        Nombre<br />
        <input
          type="text"
          placeholder="Nombre Apellido"
          id={`nombre-contacto${contactId}`}
          className="form-control"
          name="nombre"
          onChange={e => onContactChange(e, contactId)}
          value={contactValues.nombre}
        />
      </label> <br />
      <label htmlFor={`email-contacto${contactId}`}>
        email<br />
        <input
          type="email"
          placeholder="ejemplo@email.com"
          id={`email-contacto${contactId}`}
          className="form-control"
          name="email"
          onChange={e => onContactChange(e, contactId)}
          value={contactValues.email}
        />
      </label> <br />
      <label htmlFor={`telefono-contacto${contactId}`}>
        Telefono<br />
        <input
          type="telefono"
          placeholder="543515000555"
          id={`telefono-contacto${contactId}`}
          className="form-control"
          name="telefono"
          onChange={e => onPhoneChange(e, contactId)}
          value={contactValues.telefono}
        />
      </label> <br />
      <input
        type="button"
        value="Remover Contacto"
        className="btn btn-danger"
        onClick={() => onClickRemove(contactId)}
      />
    </div>
  );
}
ContactoInput.propTypes = inputPropTypes;

const registerPropTypes = {
  contacts: PropTypes.arrayOf(PropTypes.object).isRequired,  
  onClickAdd: PropTypes.func.isRequired,
  onClickRemove: PropTypes.func.isRequired,
  onContactChange: PropTypes.func.isRequired,
  onPhoneChange: PropTypes.func.isRequired,
};

class RegistrarContacto extends React.Component {
  displayInputs() {
    const inputs = [];
    for (let i = 1; i <= this.props.contacts.length; i += 1) {
      inputs.push(<ContactoInput
        contactNum={i}
        onClickRemove={this.props.onClickRemove}
        contactId={this.props.contacts[i - 1].contactId}
        onContactChange={this.props.onContactChange}
        onPhoneChange={this.props.onPhoneChange}
        contactValues={this.props.contacts[i - 1]}
      />);
    }
    return inputs || null;
  }

  render() {
    return (
      <div className="row">
        {this.displayInputs()}
        <input
          type="button"
          className="btn btn-secondary"
          value="Agregar Contacto"
          onClick={this.props.onClickAdd}
        />
      </div>
    );
  }
}
RegistrarContacto.propTypes = registerPropTypes;

export default RegistrarContacto;



import React, { Component } from 'react';
import { Button, Table, Card, CardHeader, CardBody } from 'reactstrap';
import './RegistrarContactos.css';
import SelectorItem from './SelectorItem/SelectorItem';
import NumericInput from 'react-numeric-input';
import api from '../../../api';
import ModalEliminarItem from '../../common/ModalEliminarItem/ModalEliminarItem';
import ModalEditarItem from './ModalEditarItem/ModalEditarItem';


class RegistrarContactos extends Component {
  constructor(props){
    super(props);
    const urlParams = new URLSearchParams(this.props.location.search)
    const parametro = urlParams.get('evento');
    let evento;
    if (parametro) {
      evento = parametro;
    } else {
      this.props.history.push({ pathname: '/dashboard' });
    }
    this.state = {
      evento: evento,
      contactos: [],
      contacto: undefined,      
      contactId: '1',    
      nextId: '2',
      showModalEliminar: false,
      contactoModificado: undefined,
      contactoModificadoId: undefined
    };
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleItemChange = this.handleItemChange.bind(this);
    this.handleInputChange = this.handleInputChange.bind(this);
    this.saveCntacto = this.saveCntacto.bind(this);
    this.confirmDeleteContacto = this.confirmDeleteContacto.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();
    if (this.handleValidation()) {
      const contacto = {        
        nombre: this.state.nombre,
        email: this.state.email,
        telefono: this.state.telefono,
        evento: this.state.evento
      }
      this.contactos.push(contacto); // Agregamos elcontactos al array
    }
  }

  addContacto(contacto) {
    api.post('/actividades/contactos/', contacto)
      .then(res => {
        console.log(res);
        console.log(res.data);
        this.cleancontacto();
        this.loadContactos();
      }).catch(function (error) {
        if (error.response){ console.log(error.response.status) }
        else { console.log('Error: ', error.message)}
        this.setState({ error: "Hubo un problema al cargar su información." });
      });
  }

  saveCntacto(telefono) {
    if (telefono) {
      const nuevoContacto = {
        id: this.state.contactoModificado.id,
        email: this.state.contactoModificado.recurso.id,
        nombre: this.state.contactoModificado.nombre,
        telefono: telefono,
        evento: this.state.evento
      };
      api.put("/actividades/contactos/" + nuevoContacto.id + "/", nuevoContacto) //atento aca elcontacto tiene id?
        .then(res => {
          console.log(res);
          console.log(res.data);
          this.cleancontacto();
          this.loadContactos();
        }).catch(function (error) {
          if (error.response){ console.log(error.response.status) }
          else { console.log('Error: ', error.message)}
          this.setState({ error: "Hubo un problema al cargar su información." });
        });
    }
    this.setState({
      showModalEditar: false,
      contactoModificado: undefined
    });    
  }

  handleValidation() { //DONE
    let formIsValid = true;
    var error = this.state.error;    
    if (this.state.nombre === "") {
        error = 'No puede ingresar un contacto sin nombre';        
        formIsValid = false;
      }
    if (contactos[i].mail === "" && contactos[i].telefono === "") {
        error += ' Debe ingresar un mail o un telefono';        
        formIsValid = false;
      }
    if (contactos[i].mail !== "" && !validateEmail(contactos[i].mail)) {
        error += ' Debe ingresar un mail valido';        
        formIsValid = false;
    }
    this.setState({error: error});
    return formIsValid;      
  }

  

  editContacto(id) { //hace falta id
    const contacto = this.state.contactos.filter(n => n.id === id)[0];
    this.setState({ 
      showModalEditar: true,
      contactoModificado: contacto
    });
  }

  cleancontacto() {
    this.setState({
      nombre: undefined,
      telefono: undefined,
      email: undefined,
      contacto: undefined
    });
  }

  // Delete contacto

  deleteContacto(id) {
    const contacto = this.state.contactos.filter(n => n.id === id)[0];
    this.setState({ 
      showModalEliminar: true,
      contactoModificado: contacto
    });
    
  }

  confirmDeleteContacto() {
    contactoModificado = contactos.splice(contactoModificadoId, 1);
  }

  /*
    if (res) {
      api.delete('/actividades/contactos/' + this.state.contactoModificado.id + '/') //atento con el id
      .then(res => {
        console.log(res);
        console.log(res.data);
        this.loadContactos();
      }).catch(function (error) {
        if (error.response){ console.log(error.response.status) }
        else { console.log('Error: ', error.message)}
      });
    }
    this.setState({
      contactoModificado: undefined,
      showModalEliminar: false
    })
  */


  // Carga de contactos 

  componentDidMount() {
    this.loadContactos();
  }

  loadContactos() {
    api.get('/actividades/contactos/?evento=' + this.state.evento + '/') // ver si esta bien
      .then(res => {
        const contactosData = res.data;
        this.setState({ contactos: contactosData});
      })
      .catch((error) => {
        if (error.response){ console.log(error.response.status) }
        else { console.log('Error: ', error.message)}
        this.setState({ error: "Hubo un problema al cargar su información." });
      })
  }

  /*handleItemChange(r) {
    // eslint-disable-next-line
    this.setState({ email: parseInt(r) });
  }*/

  handleInputChange(event) {
    const target = event.target;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;
    this.setState({
        [name]: value
    });
  }

  render() {
    const tablaContactos = undefined;
    for (let c = 0; c <= this.props.contacts.length; c += 1) {
      tablaContactos +=
      <tr>
        <td>{c.nombre}</td>
        <td>{c.email}</td>
        <td>{c.telefono}</td>
      {contactoModificadoId == c}
        <td><Button onClick={() => this.editContacto(contactoModificadoId)} outline // Atento a que no falle acá, porqu puede que tome elvalorde c para todas las filas y siempre edite el mismo contacto
          disabled={this.state.contacto} color="warning">Editar</Button></td>
        <td><Button onClick={() => this.deleteContacto(contactoModificadoId)} outline 
          disabled={this.state.contacto} color="danger">Eliminar</Button></td>
      </tr>
    }

    return (
      <div className="animated fadeIn">
        <Card>
          <CardHeader>
            <i className="fa fa-align-justify"></i> Agregue las personas a las que se pueda contactar por el evento
          </CardHeader>
          <CardBody>
            <div className="form-group">
              <form onSubmit={this.handleSubmit}>
                <div className="row">
                  <div className="col-md-3">
                  <input type="text" 
                      name="nombre" className="form-control"
                      placeholder="Nombre"
                      value={this.state.nombre} 
                      onChange={this.handleInputChange}
                    />
                  </div>
                  <div className="col-md-3">
                  <input type="text" 
                      name="email" className="form-control"
                      placeholder="email"
                      value={this.state.email} 
                      onChange={this.handleInputChange}
                    />
                  </div>
                  <div className="col-md-3">
                    <input type="text" 
                      name="telefono" className="form-control"
                      placeholder="Teléfono"
                      value={this.state.telefono} 
                      onChange={this.handleInputChange}
                    />
                  </div>
                  <div className="col-md-3">
                    <Button outline type="submit" color="success">Agregar</Button>
                  </div>
                </div>
                <span style={{color: "red"}}>{this.state.error}</span>
              </form>
            </div>
            <Table responsive striped>
              <thead>
                <tr>
                  <th>Nombre</th>
                  <th>email</th>
                  <th>Teléfono</th>                  
                  <th></th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                {tablaContactos}
              </tbody>
            </Table>
            {/*<Button onClick={() => this.props.history.push('dashboard')} 
              color="primary">Guardar contactos</Button>*/}
          </CardBody>
        </Card>
        <ModalEliminarItem open={this.state.showModalEliminar} contactoId={this.state.contactoModificadoId} contactos={this.state.contactos}
          closeModal={this.confirmDeleteContacto}/>
        <ModalEditarItem open={this.state.showModalEditar} contacto={this.state.contactoModificado}
          closeModal={this.saveCntacto}/>
      </div>
    )
  }
}  
export default RegistrarContactos;