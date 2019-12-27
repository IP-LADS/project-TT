import { TestStore } from './testStore';
import { ResultStore } from './resultStore';

interface IGenericObject<T> {
  [key: string]: T;
}

class RootStore {
  public stores: IGenericObject<Object> = {};

  public constructor() {
    this.stores.testStore = new TestStore();
    this.stores.resultStore = new ResultStore();
  }
}

export const rootStore = new RootStore();
