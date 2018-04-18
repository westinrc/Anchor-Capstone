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
				{ num: 1, age: '?', sex: 'M', name: 'Westin Christensen', comment: 'lalalallalalalala', diagnosis: 'aaaa', note: 'note here', icd9P: '20', icd9S: '20, 10, 30'},
				{ num: 2, age: 26, sex: 'F', name: 'Alli Jacobson', comment: 'lalalallalalalala', diagnosis: 'aaaa', note: 'note here', icd9P: '20', icd9S: '20, 10, 30'},
				{ num: 3, age: 21, sex: 'F', name: 'Tori Ottenheimer', comment: 'lalalallalalalala', diagnosis: 'aaaa', note: 'note here', icd9P: '20', icd9S: '20, 10, 30'},
				{ num: 4, age: 19, sex: 'M', name: 'Cadin Christensen', comment: 'lalalallalalalala', diagnosis: 'aaaa', note: 'note here', icd9P: '20', icd9S: '20, 10, 30'},
				{ num: 5, age: 18, sex: 'F', name: 'Jessie Christensen', comment: 'lalalallalalalala', diagnosis: 'aaaa', note: 'note here', icd9P: '20', icd9S: '20, 10, 30'},
				{ num: 6, age: 22, sex: 'F', name: 'Megan Jacobson', comment: 'lalalallalalalala', diagnosis: 'aaaa', note: 'note here', icd9P: '20', icd9S: '20, 10, 30'}
			]
		};
		this.clickedPlus = this.clickedPlus.bind(this);
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
				let name = row.name;
				let age = row.age;
				let sex = row.sex;
				let comment = row.comment;
				let diagnosis = row.diagnosis;
				let note = row.note;
				let icd9p = row.icd9P;
				let icd9s = row.icd9S;
				// This is not waiting for the value to be set, this needs to be chained in some way.
				this.setState({
					displayPatient: name + ' ' + age + ' ' + sex + ' ' + 'ICD9 Primary:' + icd9p +
					'\n----------------------------\n' +
					'diagnosis: ' + diagnosis +
					'\nICD9 Secondary: ' + icd9s +
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

				<BootstrapTable data={this.state.patients}
					hover
					selectRow={selectRow}
					options={options}
					condenced
					bordered={false}
					height='170px'
				>
					<TableHeaderColumn isKey dataField='num' headerAlign='center' dataAlign='center' width='50'>#</TableHeaderColumn>
					<TableHeaderColumn dataField="buttons" dataFormat={buttonFormatter} headerAlign='center' dataAlign='center' width='90'>Buttons</TableHeaderColumn>
					<TableHeaderColumn dataField='age' headerAlign='center' dataAlign='center' width='50'>Age</TableHeaderColumn>
					<TableHeaderColumn dataField='sex' headerAlign='center' dataAlign='center' width='50'>Sex</TableHeaderColumn>
					<TableHeaderColumn dataField='name'>Name</TableHeaderColumn>
				</BootstrapTable>
				</div>
			</div>
		);
	}
}

export default PatientList;
