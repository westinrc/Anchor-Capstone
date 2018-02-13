import React, { Component } from 'react';
import AnchorRow from './anchor_row';
import '../css/current_anchors.css';

class CurrentAnchors extends Component {
	constructor() {
		super();
		this.state = {
			rowAnchor: ['car', 'truck', 'tori', 'vehicle', 'westin', 'dhalton', 'richard', 'truck', 'tori', 'vehicle', 'westin', 'dhalton', 'richard']
		};
	}

	render() {
		return (
			<div className='panel panel-default'>
				<div className='panel-heading text-left'>
					<h3 className='no-margin'>Current Anchors</h3>
				</div>
				<div className='panel-body fixed-anchor-body'>
					<table className='table table-hover'>
						<tbody>
							{this.state.rowAnchor.map((val, index) => <AnchorRow key={index} anchorterm={val}></AnchorRow>)}
						</tbody>
					</table>
				</div>
				<div className='panel-footer'>
					<div className='btn-group btn-block'>
						<button className='btn btn-default'>Remove Anchor</button>
						<button className='btn btn-default'>Add Anchor</button>
					</div>
				</div>
			</div>
		);
	}
}

export default CurrentAnchors;
