import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AlgoDataComponent } from './algo-data.component';

describe('AlgoDataComponent', () => {
  let component: AlgoDataComponent;
  let fixture: ComponentFixture<AlgoDataComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AlgoDataComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AlgoDataComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
