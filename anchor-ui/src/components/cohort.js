import React, { Component } from 'react';
import CohortRow from './cohort_row';
import '../css/cohort.css';

class Cohort extends Component {
	constructor() {
		super();
		this.state = {
			rowTerm: ['car', 'truck', 'tori', 'vehicle', 'westin', 'dhalton', 'richard', 'truck', 'tori', 'vehicle', 'westin', 'dhalton', 'richard']
		};
	}
	
	render() {
		return (
			<div className='panel panel-default'>
				<div className='panel-heading text-left'>
					<h3 className='no-margin'>Cohort Selection</h3>
				</div>
				<div className='panel-body fixed-cohort-body'>
					<table className='table table-hover'>
						<tbody>
							{this.state.rowTerm.map((val, index) => <CohortRow key={index} term={val}></CohortRow>)}
						</tbody>
					</table>
				</div>
				<div className='panel-footer'>
					<div className='btn-group btn-block'>
						<button className='btn btn-default'>Remove Cohort</button>
						<button className='btn btn-default'>Add Cohort</button>	
					</div>
				</div>
			</div>
		);
	}
}

export default Cohort;
