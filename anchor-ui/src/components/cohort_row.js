import React, { Component } from 'react';
import '../css/cohort_row.css';

class CohortRow extends Component {
	constructor() {
		super();
		this.state = {
			cohortText: '',
			selected: false
		};
		this.clicked = this.clicked.bind(this);
	}

	select() {
		this.setState({
			cohortText: this.props.term,
			selected: true
		});
	}
	deselect() {
		this.setState({
			selected: false
		});
	}

	clicked() {
		const isSelected = this.state.selected;
		if(!isSelected) {
			this.select();
			// this.props.callbackFromParent(this.state.cohortText);
		} else {
			this.deselect();
		}
	}

	render() {
		return (
			<tr className={this.state.selected ? 'selected' : 'deselected'} onClick={this.clicked.bind(this)}>
				<td className=''>{this.props.term}</td>
			</tr>
		);
	}
}

export default CohortRow;
