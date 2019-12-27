import React from 'react';
import { Row, Col, Card } from 'antd';
import { observer, inject } from 'mobx-react';

import { TestStore } from '../../stores';
import ResultList from '../result-list';

interface IProps {
  testStore?: TestStore;
}

@inject('testStore')
@observer
export class AppBody extends React.Component<IProps> {
  public render() {
    return (
      <div style={{minWidth: '1366px', display: 'flex'}}>
        <div style={{width: '25%'}}>
          <div style={{backgroundColor: 'red', height:'100vh'}}>
            Filter area
          </div>
        </div>
        <div style={{width: '2vh'}}/>
        <div style={{width: '100%', padding: '0px', backgroundColor: 'blue', height:'100vh'}}>
          <Card style={{width: 'auto', margin: '2vh', height: '96vh'}}>
            <ResultList/>
          </Card>
        </div>
      </div>
    );
  }
}
