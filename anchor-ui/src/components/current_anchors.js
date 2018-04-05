import React, { Component } from 'react';
import AnchorRow from './anchor_row';
import BootstrapTable from 'react-bootstrap-table-next';
import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';
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
			classes: 'selected',
			hideSelectColumn: true
		};
		return (
			<div className='panel panel-default'>
				<div className='panel-heading text-left'>
					<h3 className='no-margin'>Current Anchors</h3>
				</div>
				<div className='panel-body fixed-anchor-body text-left'>
				<BootstrapTable
					keyField='name' data={this.state.rowAnchor} columns={cols}
					hover
					condenced
					bordered={false}
					selectRow={selectRow}
				/>
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
