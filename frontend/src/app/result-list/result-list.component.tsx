import React from 'react';
import { Button, Result as ResultContent} from 'antd';
import { inject, observer } from 'mobx-react';

import { ResultStore, Result } from '../../stores/resultStore';
import { ResultListEntry } from './';

interface IProps {
  resultStore?: ResultStore;
}

@inject('resultStore')
@observer
export class ResultList extends React.Component<IProps> {
  public render() {
    const results = this.props.resultStore.dummyResults;
    // const results: Result[] = [];

    const emptyResultContent = <ResultContent
        status='500'
        title='500'
        subTitle='Sorry, no results found.'
        extra={<Button type='primary'>Back Home</Button>}
      />;

    return (
      <>
        {
          results.length ?
            results.map((r: Result) => <ResultListEntry result={r}/>) :
            emptyResultContent
        }
      </>
    );
  }
}