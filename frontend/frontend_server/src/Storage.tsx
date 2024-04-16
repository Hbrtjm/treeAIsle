import { configureStore } from '@reduxjs/toolkit';
import rootReducer from './reducers';  // Ensure your rootReducer is compatible with Redux Toolkit

const initialState = {};

const store = configureStore({
    reducer: rootReducer,
    preloadedState: initialState,
    middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(thunk),
    // Redux DevTools are enabled by default in development mode
});

export default store;