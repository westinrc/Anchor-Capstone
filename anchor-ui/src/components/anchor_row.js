import React, { Component } from 'react';
import '../css/anchor_row.css';

class AnchorRow extends Component {
	constructor() {
		super();
		this.state = {
			anchor: ''
		};
	}
	
	render() {
		return (
			<tr>
				<td></td>
			</tr>
		);
	}
}

export default AnchorRow;
