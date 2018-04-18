import React, { Component } from 'react';
import CohortRow from './cohort_row';
// import BootstrapTable from 'react-bootstrap-table-next';
// import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';
import 'react-bootstrap-table/dist/react-bootstrap-table-all.min.css';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';
import '../css/cohort.css';

	class Cohort extends Component {
		constructor() {
			super();
			this.state = {
				rowTerm: [{name: 'car'}, {name: 'truck'}, {name: 'tori'}, {name: 'vehicle'}, {name: 'westin'}, {name: 'dhalton'}, {name: 'richard'}]
			};
		}

		render() {
			const selectRow = {
				mode: 'radio',
				clickToSelect: true,
				className: 'selected',
				hideSelectColumn: true,
				dataShowHeader: false
			};
			return (
				<div className='panel panel-default'>
				<div className='panel-heading text-left'>
				<h3 className='no-margin'>Cohort Selection</h3>
				</div>
				<div className='panel-body fixed-cohort-body text-left'>
				<BootstrapTable data={this.state.rowTerm}
					hover
					selectRow={selectRow}
					condenced
					bordered={false}
					height='115px'
				>
					<TableHeaderColumn isKey dataField='name'>Cohort Name</TableHeaderColumn>
				</BootstrapTable>
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
