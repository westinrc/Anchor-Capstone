import React, { Component } from 'react';
import PatientRow from './patient_row';
import '../css/patient_list.css';

class PatientList extends Component {
	constructor() {
		super();
		this.state = {
			patients: [
				{ num: 1, age: 23, sex: 'M', name: 'Westin Christensen'},
				{ num: 2, age: 21, sex: 'F', name: 'Tori Ottenheimer'},
				{ num: 3, age: 26, sex: 'F', name: 'Alli Jacobson'},
				{ num: 4, age: 19, sex: 'M', name: 'Cadin Christensen'},
				{ num: 5, age: 18, sex: 'F', name: 'Jessie Christensen'},
				{ num: 6, age: 22, sex: 'F', name: 'Megan Jacobson'}
			]
		};
	}
	render() {
		return (
			<div className='panel panel-default'>
				<div className='panel-heading text-left'>
					<h3 className='no-margin'>Patient List</h3>
				</div>
				<div className='panel-body fixed-panel-list'>
					<table className='table table-hover'>
						<thead>
							<tr className='text-left'>
								<th className='col-md-1'>#</th>
								<th className='col-md-1'>Age</th>
								<th className='col-md-1'>Sex</th>
								<th className='col-md-9'>Name</th>
							</tr>
						</thead>
						<tbody>
							{this.state.patients.map((val, index) => <PatientRow key={index} patient={val}></PatientRow>)}
						</tbody>
					</table>
				</div>
			</div>
		);
	}
}

export default PatientList;
