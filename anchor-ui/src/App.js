import React, { Component } from 'react';
import './App.css';

/* Internal imports */
import AnchorInput from './components/anchorinput';
import Filters from './components/filters';
import PatientView from './components/patientview';

class App extends Component {
	render() {
		return (
			<div>
				<div className='page-header container'>
					<h1>Anchor Explorer</h1>
				</div>
				<div className='App container'>
					<Filters></Filters>
					<br />
					<AnchorInput></AnchorInput>
					<br />
					<PatientView></PatientView>
				</div>
			</div>
		);
	}
}

export default App;

// REACT BASIC EXAMPLE: http://moviee.surge.sh/
