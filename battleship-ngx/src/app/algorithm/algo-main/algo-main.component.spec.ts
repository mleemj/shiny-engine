import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AlgoMainComponent } from './algo-main.component';

describe('AlgoMainComponent', () => {
  let component: AlgoMainComponent;
  let fixture: ComponentFixture<AlgoMainComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AlgoMainComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AlgoMainComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
