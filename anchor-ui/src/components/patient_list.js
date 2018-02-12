import React, { Component } from 'react';
import '../css/patient_list.css';

class PatientList extends Component {
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
								<th>Name</th>
							</tr>
						</thead>
						<tbody>
							<tr className='text-left'>
								<td>1</td>
								<td>13</td>
								<td>M</td>
								<td>Westin Christensen</td>
							</tr>
							<tr className='text-left'>
								<td>2</td>
								<td>18</td>
								<td>F</td>
								<td>Tori Ottenheimer</td>
							</tr>
							<tr className='text-left'>
								<td>3</td>
								<td>23</td>
								<td>M</td>
								<td>Cadin Christensen</td>
							</tr>
							<tr className='text-left'>
								<td>3</td>
								<td>23</td>
								<td>M</td>
								<td>Cadin Christensen</td>
							</tr>
							<tr className='text-left'>
								<td>3</td>
								<td>23</td>
								<td>M</td>
								<td>Cadin Christensen</td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>
		);
	}
}

export default PatientList;
