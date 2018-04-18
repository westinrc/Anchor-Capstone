import React, { Component } from 'react';
import AnchorRow from './anchor_row';
import 'react-bootstrap-table/dist/react-bootstrap-table-all.min.css';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';
// import BootstrapTable from 'react-bootstrap-table-next';
// import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';
import '../css/current_anchors.css';

class CurrentAnchors extends Component {
	constructor() {
		super();
		this.state = {
			rowAnchor: [{name: 'car'}, {name: 'truck'}, {name: 'tori'}, {name: 'vehicle'}, {name: 'westin'}, {name: 'dhalton'}, {name: 'richard'}]
		};
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
		return (
			<div className='panel panel-default'>
				<div className='panel-heading text-left'>
					<h3 className='no-margin'>Current Anchors</h3>
				</div>
				<div className='panel-body fixed-anchor-body text-left'>
				<BootstrapTable data={this.state.rowAnchor}
					hover
					selectRow={selectRow}
					condenced
					bordered={false}
					height='110px'
				>
					<TableHeaderColumn isKey dataField='name'>Anchor Name</TableHeaderColumn>
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
