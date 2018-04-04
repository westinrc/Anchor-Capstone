import React, { Component } from 'react';
import '../css/patient_view.css';

class PatientView extends Component {
	constructor() {
		super();
		this.state = {
			patientReceived: '',
			result: ''
		};
	}

	componentWillReceiveProps(nextProps) {
		console.log(JSON.stringify(nextProps));
		this.setState({
			patientReceived: nextProps.passingPatientToChild
		}, () => {
				this.setState({
					result: this.state.patientReceived + '\n'
				});
				return 0;
		});
	}

	render() {
		return (
			<div className='panel panel-default panel-custom'>
				<div className='panel-heading text-left'>
					<h3 className='no-margin'>Detailed Patient View</h3>
				</div>
				<div className='panel-body fixed-panel'>
					<textarea value={this.state.patientReceived} disabled name='patient-area'></textarea>
				</div>
			</div>
		);
	}
}
export default PatientView;
