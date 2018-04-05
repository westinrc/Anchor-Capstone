import React, { Component } from 'react';
import '../css/filters.css';

class Filters extends Component {
	render() {
		return (
			<div className='panel panel-default panel-custom'>
				<div className='panel-heading text-left'>
					<h3 className='no-margin'>Filters</h3>
				</div>
				<div className='panel-body text-left'>
					<div className='radio no-margin'>
						<label className='radio no-margin'>
							<input type='radio' className='no-margin' name='filterRadios' id='viewNotAnchored' value='viewNotAnchored'></input>
							View Not Anchored
						</label>
						<label className='radio'>
							<input type='radio' name='filterRadios' id='viewAllAnchored' value='viewAllAnchored'></input>
							View All Anchored
						</label>
						<label className='radio'>
							<input type='radio' name='filterRadios' id='viewSelectedAnchored' value='viewSelectedAnchored'></input>
							View Selected Anchored
						</label>
						<label className='radio'>
							<input type='radio' name='filterRadios' id='viewRecentlyAnchored' value='viewRecentlyAnchored'></input>
							View Recently Anchored
						</label>
					</div>
				</div>
			</div>
		);
	}
}

export default Filters;
