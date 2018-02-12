import React, { Component } from 'react';
import '../css/cohort.css';

class Cohort extends Component {
	render() {
		return (
			<div className='panel panel-default'>
				<div className='panel-heading text-left'>
					<h3 className='no-margin'>Cohort Selection</h3>
				</div>
				<div className='panel-body'>
					<table className='table table-hover'>
						<tbody>
							<tr className='text-left'>
								<td className='col-md-1'>This is dummy data</td>
							</tr>
							<tr className='text-left'>
								<td className='col-md-1'>This is dummy data</td>
							</tr>
							<tr className='text-left'>
								<td className='col-md-1'>This is dummy data</td>
							</tr>
						</tbody>
					</table>
				</div>
				<div className='panel-footer'>
					<button className='btn btn-default btn-block'>Add New Cohort</button>
				</div>
			</div>
		);
	}
}

export default Cohort;
