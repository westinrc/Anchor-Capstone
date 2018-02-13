import React, { Component } from 'react';
import '../css/patient_row.css';

class PatientRow extends Component {
	render() {
		return (
			<tr className='text-left'>
				<td>{this.props.patient.num}</td>
				<td>{this.props.patient.age}</td>
				<td>{this.props.patient.sex}</td>
				<td>{this.props.patient.name}</td>
			</tr>
		);
	}
}

export default PatientRow;
