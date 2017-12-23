import { DemoGuardPage } from './app.po';

describe('demo-guard App', function() {
  let page: DemoGuardPage;

  beforeEach(() => {
    page = new DemoGuardPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
