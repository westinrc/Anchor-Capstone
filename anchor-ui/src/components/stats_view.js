import React, { Component } from 'react';
import { ButtonToolbar, Overlay, Popover, Button } from 'react-bootstrap';
import '../css/stats_view.css';

class StatsView extends Component {
	constructor(props, context) {
		super(props, context);

		this.handleClick = e => {
			this.setState({ target: e.target, show: !this.state.show });
		};

		this.state = {
			anchoredPatientCount: 0,
			currentCohort: 'none',
			markedPatientCount: 0,
			show: false
		};
	}
	render() {
		return (
			<div>
				<ButtonToolbar>
					<Button className='stats btn-info rotate-text' onClick={this.handleClick}>Stats</Button>
					<Overlay containerPadding={20} placement="left" show={this.state.show} target={this.state.target}>
						<Popover id="popover" title="Stats">
							<div className='no-padding-left text-left'>
								<p>
									Current Cohort is: { this.state.currentCohort}
								</p>
								<p>
									Anchored Patients: {this.state.anchoredPatientCount}
								</p>
								<p>
									Marked Patients: {this.state.markedPatientCount}
								</p>
							</div>
						</Popover>
					</Overlay>
				</ButtonToolbar>
			</div>
		);
	}
}
export default StatsView;
