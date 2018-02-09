import React, { Component } from 'react';
import '../css/patientview.css';

class PatientView extends Component {
	render() {
		return (
				<div className='panel panel-default panel-custom'>
					<div className='panel-heading text-left'>
						<h2 className='no-margin'>Detailed Patient View</h2>
					</div>
					<div className='panel-body fixed-panel'>
						<textarea name='patient-area'></textarea>
					</div>
				</div>
		);
	}
}
export default PatientView;