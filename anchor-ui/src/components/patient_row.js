import React, { Component } from 'react';
import '../css/patient_row.css';

class PatientRow extends Component {
	render() {
		return (
			<tr className='text-left'>
				<td className='col-md-1'>{this.props.patient.num}</td>
				<td className='col-md-1'>{this.props.patient.age}</td>
				<td className='col-md-1'>{this.props.patient.sex}</td>
				<td className='col-md-9'>{this.props.patient.name}</td>
			</tr>
		);
	}
}

export default PatientRow;
