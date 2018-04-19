import React, { Component } from 'react';
import AnchorRow from './anchor_row';
import 'react-bootstrap-table/dist/react-bootstrap-table-all.min.css';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';
// import BootstrapTable from 'react-bootstrap-table-next';
// import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';
import '../css/current_anchors.css';
import '../patients.txt'

class CurrentAnchors extends Component {
	constructor() {
		super();
		this.state = {
			passedData: [],
			rowAnchor: [],
			patients: []
		};
	}

	componentWillReceiveProps(nextProps) {
		console.log(JSON.stringify(nextProps));
		this.setState({
			rowAnchor: nextProps.passingAnchors
		}, () => {
				this.setState({
					rowAnchor: this.state.passingAnchors
				});
				return 0;
		});
	}

	render() {
		const cols=[{dataField: 'name', text:'Anchor Name', title: false}];
		const selectRow = {
			mode: 'radio',
			clickToSelect: true,
			className: 'selected',
			hideSelectColumn: true,
			dataShowHeader: false
		};

		const options = {
			onRowClick: function(row) {
				let varPatients = row.patients;
				console.log('VAR PATIENTS: '+varPatients);
				// This is not waiting for the value to be set, this needs to be chained in some way.
				this.setState({
					patients: varPatients
				}, () => {
					this.props.patientsFromChild(this.state.patients); // This line needs to wait until state is for sure set
				});
			}.bind(this)
		};

		return (
			<div className='panel panel-default'>
				<div className='panel-heading text-left'>
					<h3 className='no-margin'>Current Anchors</h3>
				</div>
				<div className='panel-body fixed-anchor-body text-left'>
				<BootstrapTable data={this.state.rowAnchor}
					hover
					selectRow={selectRow}
					options={options}
					condenced
					bordered={false}
					height='110px'
				>
					<TableHeaderColumn isKey dataField='anchorName'>Anchor Name</TableHeaderColumn>
				</BootstrapTable>
				</div>
				<div className='panel-footer'>
					<div className='btn-group'>
						<button className='btn btn-default'>Remove Anchor</button>
						{/* <button className='btn btn-default'>Add Anchor</button> */}
					</div>
				</div>
			</div>
		);
	}
}

export default CurrentAnchors;
