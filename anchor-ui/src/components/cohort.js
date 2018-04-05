import React, { Component } from 'react';
import CohortRow from './cohort_row';
import BootstrapTable from 'react-bootstrap-table-next';
import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';
import '../css/cohort.css';

	class Cohort extends Component {
		constructor() {
			super();
			this.state = {
				rowTerm: [{name: 'car'}, {name: 'truck'}, {name: 'tori'}, {name: 'vehicle'}, {name: 'westin'}, {name: 'dhalton'}, {name: 'richard'}]
			};
		}

		render() {
			const cols=[{dataField: 'name', text:'Cohort Name', title: false}];
			const selectRow = {
				mode: 'radio',
				clickToSelect: true,
				classes: 'selected',
				hideSelectColumn: true
			};
			return (
				<div className='panel panel-default'>
				<div className='panel-heading text-left'>
				<h3 className='no-margin'>Cohort Selection</h3>
				</div>
				<div className='panel-body fixed-cohort-body text-left'>
				<BootstrapTable
					keyField='name' data={this.state.rowTerm} columns={cols}
					hover
					condenced
					bordered={false}
					selectRow={selectRow}
				/>
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
