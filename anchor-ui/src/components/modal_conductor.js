import React from 'react';

import CohortModal from './modals/cohort_modal';

const ModalConductor = props => {
	switch (props.currentModal) {
	case 'ADD_COHORT':
		return <CohortModal {...props} />;
	default:
		return null;
	}
};

export default ModalConductor;
