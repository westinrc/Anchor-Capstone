import React, { Component } from 'react';
import { ButtonToolbar, Overlay, Popover, Button } from 'react-bootstrap';
import '../css/stats_view.css';

class StatsView extends Component {
	constructor(props, context) {
		super(props, context);

		this.handleClick = e => {
			this.setState({ target: e.target, show: !this.state.show });
		};

		this.state = {
			show: false
		};
	}
	render() {
		return (
			<div>
				<ButtonToolbar>
					<Button className='stats btn-info rotate-text' onClick={this.handleClick}>Stats</Button>
					<Overlay containerPadding={20} placement="left" show={this.state.show} target={this.state.target}>
						<Popover id="popover" title="Stats">
							Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
						</Popover>
					</Overlay>
				</ButtonToolbar>
			</div>
		);
	}
}
export default StatsView;
