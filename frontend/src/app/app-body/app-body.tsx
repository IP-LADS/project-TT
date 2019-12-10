import React from 'react';
import { Row, Col, Button, Select } from 'antd';
import { action } from 'mobx';
import { observer, inject } from 'mobx-react';

import { TestStore } from '../../stores';

const { Option } = Select;

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
        <Col span={8}>
          <div
            style={{ color: this.props.testStore.colourActive ? 'red' : '' }}
          >
            Toggle the colour of this teasaxt NEW!
          </div>
        </Col>

        <Col span={8}>
          <Select
            showSearch
            style={{ width: 200 }}
            placeholder='Select a person'
            optionFilterProp='children'
          >
            <Option value='jack'>Jack</Option>
            <Option value='lucy'>Lucy</Option>
            <Option value='tom'>Tom</Option>
          </Select>
        </Col>

        <Col span={8}>
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
