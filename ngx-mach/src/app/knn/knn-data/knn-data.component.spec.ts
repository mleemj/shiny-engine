import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { KnnDataComponent } from './knn-data.component';

describe('KnnDataComponent', () => {
  let component: KnnDataComponent;
  let fixture: ComponentFixture<KnnDataComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ KnnDataComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(KnnDataComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
