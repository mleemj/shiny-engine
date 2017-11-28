import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AlgoDataReaderComponent } from './algo-data-reader.component';

describe('AlgoDataReaderComponent', () => {
  let component: AlgoDataReaderComponent;
  let fixture: ComponentFixture<AlgoDataReaderComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AlgoDataReaderComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AlgoDataReaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
