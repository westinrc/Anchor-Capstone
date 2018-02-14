// import React, { Component } from 'react';
// import '../../css/modals/cohort_modal.css';

// const display = {
// 	display: 'block',
// 	position: 'absolute',	
// 	width: '50%',
// 	height: '50%',
// 	top: '100px',
// 	left: '0px',
// 	zindex: '9998',
// 	background: 'rgba(0, 0, 0, 0.3)'
// };

// const hide = {
// 	display: 'none'
// };

// class CohortModal extends Component {
// 	constructor() {
// 		super();
// 		this.state = {
// 			toggle: true
// 		};
// 		this.toggle = this.toggle.bind(this);
// 	}

// 	toggle() {
// 		this.setState({toggle: !this.state.toggle});
// 	}

// 	render() {
// 		var modal = [];
// 		modal.push(
// 			<div className="modal" style={this.state.toggle ? display : hide}>
// 				<div className="modal-content">
// 					<h4>Modal Header</h4>
// 					<p>A bunch of text</p>
// 				</div>
// 				<div className="modal-footer">
// 					<button className='btn btn-lg' onClick={this.toggle}>Agree</button>
// 				</div>
// 			</div>
// 		);
// 		return modal;
// 	}
// }

// export default CohortModal;
import React from 'react';

import ModalWrapper from './modal_wrapper.js';

const CohortModal = props => {
	const signIn = provider => {
		props.hideModal();
		props.signIn(provider);
	};

	return (
		<ModalWrapper
			{...props}
			title="Sign in"
			width={400}
			showOk={false}
		>
			<p>Choose your flavor</p>
			<button onClick={() => signIn('facebook')}>Facebook</button>
			<button onClick={() => signIn('google')}>Google</button>
			<button onClick={() => signIn('twitter')}>Twitter</button>
		</ModalWrapper>
	);
};

export default CohortModal;
