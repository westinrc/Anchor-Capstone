import React, { Component } from 'react';
import './App.css';

/* Internal imports */
import AnchorInput from './components/anchor_input';
import Cohort from './components/cohort';
import Filters from './components/filters';
import PatientList from './components/patient_list';
import PatientView from './components/patient_view';
import CurrentAnchors from './components/current_anchors';
import StatsView from './components/stats_view';
// import CohortModal from './components/modals/cohort_modal';

class App extends Component {
	constructor() {
		super();
		this.state = {
			anchoredPatientsCount: 0,
			currentCohort: 'none',
			markedPatientCount: 0,
			selectedAnchor: 'none',
			selectedPatient: 'none',
			jokesArr: [],
			displayPatientData: '',
			anchors: [],
			currentCohort: '',
			anchorPatients: []
		};
		this.searchCallBack = this.searchCallBack.bind(this);
		this.anchorsFromChild = this.anchorsFromChild.bind(this);
		this.cohortFromChild = this.cohortFromChild.bind(this);
		this.patientsFromChild = this.patientsFromChild.bind(this);
	}

	searchCallBack(dataFromChild) {
		console.log('data from child ' + dataFromChild);
		// this.setState({jokesArr: dataFromChild});
		// Use the data from the child here.
		this.setState({displayPatientData: dataFromChild});
	}
	anchorsFromChild(dataFromChild) {
		console.log('data from child ' + dataFromChild);
		// this.setState({jokesArr: dataFromChild});
		// Use the data from the child here.
		this.setState({anchors: dataFromChild});
	}
	cohortFromChild(dataFromChild) {
		console.log('data from child ' + dataFromChild);
		// this.setState({jokesArr: dataFromChild});
		// Use the data from the child here.
		this.setState({currentCohort: dataFromChild});
	}
	patientsFromChild(dataFromChild) {
		console.log('data from child ' + dataFromChild);
		// this.setState({jokesArr: dataFromChild});
		// Use the data from the child here.
		this.setState({anchorPatients: dataFromChild});
	}

	render() {
		return (
			<div>
				<StatsView passingCohort={this.state.currentCohort}></StatsView>
				<br />
				<div className='App container'>
					<div className='row'>
						<div className='col-md-3'>
							<Cohort anchorsFromChild={this.anchorsFromChild} cohortFromChild={this.cohortFromChild}></Cohort>
						</div>
						<div className='col-md-9'>
							<PatientList passingPatients={this.state.anchorPatients} callbackFromParent={this.searchCallBack}></PatientList>
						</div>
					</div>
					<div className='row'>
						<div className='col-md-3'>
							<CurrentAnchors passingAnchors={this.state.anchors} patientsFromChild={this.patientsFromChild}></CurrentAnchors>
							<Filters></Filters>
						</div>
						<div className='col-md-9'>
							<AnchorInput></AnchorInput>
							<br />
							<PatientView passingPatientToChild={this.state.displayPatientData}></PatientView>
						</div>
					</div>
					<br />
					{/* <CohortModal show={true}>Here is some content</CohortModal> */}
				</div>
			</div>
		);
	}
}
export default App;
