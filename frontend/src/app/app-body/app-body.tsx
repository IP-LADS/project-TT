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
      <Row gutter={32} style={{width: '1366px'}}>
        <Col span={6}>
          <div style={{backgroundColor: 'red', height:'100vh'}}>
            Filter area
          </div>
        </Col>

        <Col span={18} style={{padding: '0px', backgroundColor: 'blue', height:'100vh'}}>
          <Card style={{margin: '2vh', height: '96vh'}}>
            <ResultList/>
          </Card>
        </Col>
      </Row>
    );
  }
}
