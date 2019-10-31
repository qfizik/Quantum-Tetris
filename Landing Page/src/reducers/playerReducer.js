import { ActionTypes } from '../actions';

const PlayerReducer = (state = {
  user: {
    username: 'Oliver',
    hiscore: 7,
  },
}, action) => {
  switch (action.type) {
    case ActionTypes.CREATE_PLAYER:
      return Object.assign({}, state, { user: action.payload });
    case ActionTypes.GET_PLAYER:
      return Object.assign({}, state, { user: action.payload });
    case ActionTypes.INCREMENT:
      return state + 1;
    case ActionTypes.DECREMENT:
      return state - 1;
    default:
      return state;
  }
};

export default PlayerReducer;
