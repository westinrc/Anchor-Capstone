import React, { Component } from 'react';
import PatientRow from './patient_row';
// import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';
import 'react-bootstrap-table/dist/react-bootstrap-table-all.min.css';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';

import '../css/patient_list.css';

class PatientList extends Component {
	constructor() {
		super();
		this.state = {
			buttons: <div><button className='btn btn-xs btn-success' type='button' onClick={this.clickedPlus.bind(this)}>+</button> <button className='btn btn-xs btn-danger'>-</button> <button className='btn btn-xs btn-info'>x</button></div>,
			displayPatient: '',
			patients: [
				{ index: 1, Age: '?', Sex: 'M', Diagnosis: 'aaaa', Note: 'note here'},
				{ index: 2, Age: 26, Sex: 'F', Diagnosis: 'aaaa', Note: 'note here'},
				{ index: 3, Age: 21, Sex: 'F', Diagnosis: 'aaaa', Note: 'note here'},
				{ index: 4, Age: 19, Sex: 'M', Diagnosis: 'aaaa', Note: 'note here'},
				{ index: 5, Age: 18, Sex: 'F', Diagnosis: 'aaaa', Note: 'note here'},
				{ index: 6, Age: 22, Sex: 'F', Diagnosis: 'aaaa', Note: 'note here'}
			],
			anchorPatients: []
		};
		this.clickedPlus = this.clickedPlus.bind(this);
	}

	componentWillReceiveProps(nextProps) {
		console.log(JSON.stringify(nextProps));
		this.setState({
			anchorPatients: nextProps.passingPatients
		}, () => {
				this.setState({
					anchorPatients: this.state.passingPatients
				});
				return 0;
		});
	}

	clickedPlus() {
		// alert("you clicked plus");
		console.log('plus button clicked');
	}

	render() {
		const selectRow = {
			mode: 'radio',
			clickToSelect: true,
			className: 'selected',
			hideSelectColumn: true,
			dataShowHeader: false
		};
		const options = {
			onRowClick: function(row) {
				// alert(`You click row id: ${row.name}`);
				let diagnosis = row.Diagnosis;
				let age = row.Age;
				let sex = row.Sex;
				// let diagnosises = row.diagnosis;
				let note = row.Note;
				// This is not waiting for the value to be set, this needs to be chained in some way.
				this.setState({
					displayPatient: age + ' ' + sex + ' ' + 'Diagnosis:' + diagnosis +
					'\n----------------------------\n' +
					'\nnote: ' + note
				}, () => {
					this.props.callbackFromParent(this.state.displayPatient); // This line needs to wait until state is for sure set
				});
			}.bind(this)
		}

		function buttonFormatter(cell, row){
			return (<div><button className='btn btn-xs btn-success'>+</button> <button className='btn btn-xs btn-danger'>-</button> <button className='btn btn-xs btn-info'>x</button></div>);
		}
		return (
			<div className='panel panel-default'>
				<link rel="stylesheet" href="https://npmcdn.com/react-bootstrap-table/dist/react-bootstrap-table-all.min.css"></link>
				<div className='panel-heading text-left'>
					<h3 className='no-margin'>Patient List</h3>
				</div>
				<div className='panel-body fixed-panel-list text-left'>

				<BootstrapTable data={this.state.anchorPatients}
					hover
					selectRow={selectRow}
					options={options}
					condenced
					bordered={false}
					height='170px'
				>
					<TableHeaderColumn isKey dataField='index' headerAlign='center' dataAlign='center' width='100'>#</TableHeaderColumn>
					<TableHeaderColumn dataField="buttons" dataFormat={buttonFormatter} headerAlign='center' dataAlign='center' width='90'>Buttons</TableHeaderColumn>
					<TableHeaderColumn dataField='Age' headerAlign='center' dataAlign='center' width='50'>Age</TableHeaderColumn>
					<TableHeaderColumn dataField='Sex' headerAlign='center' dataAlign='center' width='50'>Sex</TableHeaderColumn>
					<TableHeaderColumn dataField='Diagnosis'>Diagnosis</TableHeaderColumn>
				</BootstrapTable>
				</div>
			</div>
		);
	}
}

export default PatientList;
