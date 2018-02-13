import React, { Component } from 'react';
import '../css/anchor_row.css';

class AnchorRow extends Component {
	render() {
		return (
			<tr className='text-left'>
				<td>{this.props.anchorterm}</td>
			</tr>
		);
	}
}

export default AnchorRow;
