import React from 'react';
import { Provider } from 'mobx-react';

import { AppBody } from './app/app-body';
import { rootStore } from './stores';

import './App.css';

const App: React.FC = () => {
  return (
    <div className='App'>
      <Provider {...rootStore.stores}>
        <AppBody />
      </Provider>
    </div>
  );
};

export default App;
