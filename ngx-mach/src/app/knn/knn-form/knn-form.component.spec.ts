import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { KnnFormComponent } from './knn-form.component';

describe('KnnFormComponent', () => {
  let component: KnnFormComponent;
  let fixture: ComponentFixture<KnnFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ KnnFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(KnnFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
