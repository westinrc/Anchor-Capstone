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

class App extends Component {
	constructor() {
		super();
		this.state = {
			jokesArr: [],
		};
		this.searchCallBack = this.searchCallBack.bind(this);
	}

	searchCallBack(dataFromChild) {
		console.log('data from child ' + dataFromChild);
		this.setState({jokesArr: dataFromChild});
		// Use the data from the child here.
	}
	
	render() {
		return (
			<div>
				<StatsView></StatsView>
				<br />
				<div className='App container'>
					<div className='row'>
						<div className='col-md-3'>
							<Cohort></Cohort>
						</div>
						<div className='col-md-9'>
							<PatientList></PatientList>
						</div>
					</div>
					<div className='row'>
						<div className='col-md-3'>
							<CurrentAnchors></CurrentAnchors>
							<Filters></Filters>
						</div>
						<div className='col-md-9'>
							<AnchorInput callbackFromParent={this.searchCallBack}></AnchorInput>
							<br />
							<PatientView passingJokeToChild={this.state.jokesArr}></PatientView>
						</div>
					</div>
					<br />
				</div>
			</div>
		);
	}
}
export default App;
