import { observable, computed, action } from 'mobx';

export class TestStore {
  @observable
  private isFetchingFromServer: boolean = false;

  @observable
  public colourActive: boolean = false;

  @computed
  public get isMakingServerCall() {
    return this.isFetchingFromServer;
  }

  @action
  public fakeServerCall() {
    this.isFetchingFromServer = true;
    setTimeout(() => {
      this.colourActive = !this.colourActive;
      this.isFetchingFromServer = false;
    }, 500);
  }
}
