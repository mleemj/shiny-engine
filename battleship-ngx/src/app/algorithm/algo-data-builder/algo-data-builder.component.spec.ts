import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AlgoDataBuilderComponent } from './algo-data-builder.component';

describe('AlgoDataBuilderComponent', () => {
  let component: AlgoDataBuilderComponent;
  let fixture: ComponentFixture<AlgoDataBuilderComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AlgoDataBuilderComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AlgoDataBuilderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
