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
				cohorts: [{name: 'car', anchors: [{anchorName: 'Symptom 1'}, {anchorName: 'Symptom 2'}, {anchorName: 'Symptom 3'}]},
									{name: 'truck', anchors: [{anchorName: 'Symptom 4'}, {anchorName: 'Symptom 5'}, {anchorName: 'Symptom 6'}]}],
				CohortAnchors: []
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
			const options = {
				onRowClick: function(row) {
					// alert(`You click row id: ${row.anchors}`);
					let anchors = row.anchors;
					// This is not waiting for the value to be set, this needs to be chained in some way.
					this.setState({
						CohortAnchors: anchors
					}, () => {
						this.props.anchorsFromChild(this.state.CohortAnchors); // This line needs to wait until state is for sure set
					});
				}.bind(this)
			};

			return (
				<div className='panel panel-default'>
				<div className='panel-heading text-left'>
				<h3 className='no-margin'>Cohort Selection</h3>
				</div>
				<div className='panel-body fixed-cohort-body text-left'>
				<BootstrapTable data={this.state.cohorts}
					hover
					selectRow={selectRow}
					condenced
					options={options}
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
