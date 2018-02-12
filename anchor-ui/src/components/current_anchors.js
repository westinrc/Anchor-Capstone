import React, { Component } from 'react';
import '../css/current_anchors.css';

class CurrentAnchors extends Component {
	render() {
		return (
			<div className='panel panel-default'>
				<div className='panel-heading text-left'>
					<h3 className='no-margin'>Current Anchors</h3>
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
