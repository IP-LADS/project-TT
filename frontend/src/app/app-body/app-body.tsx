import React from 'react';
import { Row, Col, Button } from 'antd';
import { action } from 'mobx';
import { observer, inject } from 'mobx-react';

import { TestStore } from '../../stores';

interface IProps {
  testStore?: TestStore;
}

@inject('testStore')
@observer
export class AppBody extends React.Component<IProps> {
  @action
  private toggleColour = () => {
    this.props.testStore.fakeServerCall();
  };

  public render() {
    return (
      <Row gutter={16}>
        <Col span={12}>
          <div
            style={{ color: this.props.testStore.colourActive ? 'red' : '' }}
          >
            Toggle my colour!
          </div>
        </Col>

        <Col span={12}>
          <Button
            type='primary'
            loading={this.props.testStore.isMakingServerCall}
            onClick={this.toggleColour}
          >
            Toggle colour
          </Button>
        </Col>
      </Row>
    );
  }
}
