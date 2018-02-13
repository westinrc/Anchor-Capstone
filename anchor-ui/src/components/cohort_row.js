import React, { Component } from 'react';
import '../css/cohort_row.css';

class CohortRow extends Component {
	render() {
		return (
			<tr className='text-left'>
				<td>{this.props.term}</td>
			</tr>
		);
	}
}

export default CohortRow;
