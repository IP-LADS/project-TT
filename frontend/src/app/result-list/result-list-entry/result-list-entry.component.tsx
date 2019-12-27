import React from 'react';
import { Card, Row, Col } from 'antd';

import { Result } from '../../../stores/resultStore';

interface IProps {
  result: Result;
}

export class ResultListEntry extends React.Component<IProps> {
  public render() {
    return(
      <Card>
        <Row gutter={24}>
          <Col span={8}>
            {this.props.result.rank}
          </Col>

          <Col span={8}>
            {this.props.result.location}
          </Col>

          <Col span={8}>
            {this.props.result.popularityScore}
          </Col>
        </Row>
      </Card>
    );
  }
}