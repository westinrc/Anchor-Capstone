import React, { Component } from 'react';
import '../css/anchorinput.css';

class AnchorInput extends Component {
	render() {
		return (
			<div className='input-section'>
				<div className='input-group'>
					<input type='text' className='form-control' placeholder='Anchor Input'></input>
					<span className='input-group-btn'>
						<button className='btn btn-success' type='button'>LEARN!</button>
					</span>
				</div>
			</div>
		);
	}
}
export default AnchorInput;
