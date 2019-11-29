import { TestStore } from './testStore';

interface IGenericObject<T> {
  [key: string]: T;
}

class RootStore {
  public stores: IGenericObject<Object> = {};

  public constructor() {
    this.stores['testStore'] = new TestStore();
  }
}

export const rootStore = new RootStore();
