import React, { Component } from 'react';
import '../css/patient_view.css';

class PatientView extends Component {
	constructor() {
		super();
		this.state = {
			jokesReceived: [],
			result: ''
		};
	}

	componentWillReceiveProps(nextProps) {
		console.log(JSON.stringify(nextProps));
		console.log('almost');
		this.setState({
			jokesReceived: nextProps.passingJokeToChild
		}, () => {
			this.state.jokesReceived.map((joke) => {
				console.log('updating');
				this.setState({
					result: this.state.result + joke + '\n'
				});
				return 0;
			});	
		});
	}

	render() {
		return (
			<div className='panel panel-default panel-custom'>
				<div className='panel-heading text-left'>
					<h3 className='no-margin'>Detailed Patient View</h3>
				</div>
				<div className='panel-body fixed-panel'>
					<textarea value={this.state.result} disabled name='patient-area'></textarea>
				</div>
			</div>
		);
	}
}
export default PatientView;
