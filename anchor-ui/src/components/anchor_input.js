import React, { Component } from 'react';
import '../css/anchor_input.css';

class AnchorInput extends Component {
	constructor() {
		super();
		this.state = {
			requestText: '',
			jokes: [],
			anchorText: ''
		};
		this.clickedIt = this.clickedIt.bind(this);
	}

	/* This is an example of a UI call when a button is pressed. We still need to handle passing the data around*/
	clickedIt() {
		// fetch('https://icanhazdadjoke.com/', {
		// 	method: 'GET',
		// 	headers: {
		// 		'Accept': 'application/json'
		// 	}
		// }).then(results => {
		// 	return results.json();
		// }).then(data => {
		// 	let joke = data.joke;
		// 	this.setState({
		// 		jokes: this.state.jokes.concat(joke)
		// 	});
		// }).then(() => {
		// 	this.props.callbackFromParent(this.state.jokes);
		// });
		alert("you clicked learn");
	}

	render() {
		return (
			<div className='input-section'>
				<div className='input-group'>
					<input type='text' className='form-control' placeholder='Anchor Input'></input>
					<span className='input-group-btn'>
						<button className='btn btn-success' type='button' onClick={this.clickedIt.bind(this)}>LEARN!</button>
					</span>
				</div>
			</div>
		);
	}
}

export default AnchorInput;
