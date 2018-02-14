import React, { Component } from 'react';
import '../css/patient_row.css';

class PatientRow extends Component {
	constructor() {
		super();
		this.state = {
			buttons: <div><button className='btn btn-xs btn-success'>+</button> <button className='btn btn-xs btn-danger'>-</button> <button className='btn btn-xs btn-info'>x</button></div>
		};
	}
	render() {
		return (
			<tr className='text-left'>
				<td className='col-md-1 text-center'>{this.props.patient.num}</td>
				<td className='col-md-1 text-center'>{this.state.buttons}</td>
				<td className='col-md-1 text-center'>{this.props.patient.age}</td>
				<td className='col-md-1 text-center'>{this.props.patient.sex}</td>
				<td className='col-md-9'>{this.props.patient.name}</td>
			</tr>
		);
	}
}

export default PatientRow;
