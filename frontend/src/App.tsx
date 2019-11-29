import React from 'react';
import { Layout, Menu } from 'antd';
import { Provider } from 'mobx-react';

import { AppBody } from './app/app-body';
import { rootStore } from './stores';

import './App.css';

const { Header, Content } = Layout;

const App: React.FC = () => {
  return (
    <div className='App'>
      <Provider {...rootStore.stores}>
        <Layout>
          <Header>
            <Menu
              theme='dark'
              mode='horizontal'
              defaultSelectedKeys={['2']}
              style={{ lineHeight: '64px' }}
            >
              <Menu.Item key='1'>nav 1</Menu.Item>
              <Menu.Item key='2'>nav 2</Menu.Item>
              <Menu.Item key='3'>nav 3</Menu.Item>
            </Menu>
          </Header>
          <Content style={{ height: '90vh' }}>
            <AppBody />
          </Content>
        </Layout>
      </Provider>
    </div>
  );
};

export default App;
