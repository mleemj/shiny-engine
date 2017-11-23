import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AlgoDetailComponent } from './algo-detail.component';

describe('AlgoDetailComponent', () => {
  let component: AlgoDetailComponent;
  let fixture: ComponentFixture<AlgoDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AlgoDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AlgoDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
